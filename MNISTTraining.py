import tensorflow as tf  
import sys
import os

# Get the directory of the current script
scriptDir = os.path.dirname(os.path.abspath(__file__))

# Add this directory to the system path
sys.path.append(scriptDir)

# Import the modules
from MNIST_training_using_python_files.GPUandCPUAvailability import GPUAvailability, CPUAvailability
from MNIST_training_using_python_files.BuildAndCompileTheModel import BuildAndCompileModel
from MNIST_training_using_python_files.ValidateImages import ValidateImages
from MNIST_training_using_python_files.DataSplitter import SplitData

GPUAvailability()
CPUAvailability()

# Define the directory containing your training data
data_dir = os.path.join(scriptDir, "mnist_png", "training")
print(data_dir)

# List the classes (subdirectories)
class_names = os.listdir(data_dir)
print("Class names:", class_names)

ValidateImages(data_dir)

# Load dataset
data = tf.keras.utils.image_dataset_from_directory(
    data_dir, batch_size=8, image_size=(28, 28), label_mode='int'
)

# Scale data
data = data.map(lambda x, y: (x / 255, y))

train_size, val_size, test_size = SplitData(data, 0.75, 0.1, 0.15)
train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size + val_size).take(test_size)

# Build the and Compile the model
model = BuildAndCompileModel()

# Train the model
logDir = os.path.join(scriptDir, "logs")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logDir)
hist = model.fit(train, epochs=4, validation_data=val, callbacks=[tensorboard_callback])