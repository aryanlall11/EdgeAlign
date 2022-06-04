# Install xxd if it is not available
# !apt-get update && apt-get -qq install xxd

from tensorflow import keras
import tensorflow as tf
import numpy as np
import pathlib
import os

#--------------------------------------------------------------
# Helper function to run inference on a TFLite model
def run_tflite_model(tflite_file, state):

  # Initialize the interpreter
  interpreter = tf.lite.Interpreter(model_path=str(tflite_file))
  interpreter.allocate_tensors()

  input_details = interpreter.get_input_details()[0]
  output_details = interpreter.get_output_details()[0]

  # Check if the input type is quantized, then rescale input data to uint8
  if input_details['dtype'] == np.uint8:
    input_scale, input_zero_point = input_details["quantization"]
    state = state / input_scale + input_zero_point

  state = np.expand_dims(state, axis=0).astype(input_details["dtype"])
  interpreter.set_tensor(input_details["index"], state)
  interpreter.invoke()
  output = interpreter.get_tensor(output_details["index"])[0]
  #print(output)
  #action = output[1: ].argmax()  # Find index with max advantage

  return output # 4 values (value and 3 advantages)

# Helper function to test the models on one image
def test_model(tflite_file, state):
  state = np.reshape(state, (1, state.size))
  action = run_tflite_model(tflite_file, state)

  print("Action : ", action)
#--------------------------------------------------------------  

# Remove the last Lambda layer (if any) in the EdgeAlign model as it isn't supported by TFLite
# After removing the lamda layer, save the model weights to a new file (ex, EdgeAlignModel_final)
model = tf.keras.models.load_model('EdgeAlign_Model_w50')
model.summary()

model.compile(
            loss = "categorical_crossentropy",
            optimizer = "adam",
            metrics = ["accuracy"])
states = np.load('states.npy')
#--------------------------------------------------------------

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

tflite_models_dir = pathlib.Path("edgealign_tflite_models/")
tflite_models_dir.mkdir(exist_ok=True, parents=True)

# Save the unquantized/float model:
tflite_model_file = tflite_models_dir/"edgealign_model.tflite"
tflite_model_file.write_bytes(tflite_model)

print(os.path.getsize("edgealign_tflite_models/edgealign_model.tflite"))  # Model size in Bytes

# Test for 1-image (state)
state = states[0]
test_model(tflite_model_file, state)
#--------------------------------------------------------------

# Convert to a C source file, i.e, a TensorFlow Lite for Microcontrollers model
!xxd -i {'edgealign_tflite_models/edgealign_model.tflite'} > {'edgealign_tflite_models/model.cc'}


"""
# For using the quantized version of the TFLite model - 

states = states.astype(np.float32)

def representative_data_gen():
  for input_value in tf.data.Dataset.from_tensor_slices(states).batch(1).take(1000):
    yield [input_value]

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_data_gen
# Ensure that if any ops can't be quantized, the converter throws an error
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
# Set the input and output tensors to uint8 (APIs added in r2.3)
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model_quant = converter.convert()
#--------------------------------------------------------------  

interpreter = tf.lite.Interpreter(model_content=tflite_model_quant)
input_type = interpreter.get_input_details()[0]['dtype']
print('input: ', input_type)
output_type = interpreter.get_output_details()[0]['dtype']
print('output: ', output_type)
#--------------------------------------------------------------  

tflite_model_quant_file = tflite_models_dir/"edgealign_model_quant.tflite"
tflite_model_quant_file.write_bytes(tflite_model_quant)

print(os.path.getsize("/content/edgealign_tflite_models/edgealign_model_quant.tflite"))

"""