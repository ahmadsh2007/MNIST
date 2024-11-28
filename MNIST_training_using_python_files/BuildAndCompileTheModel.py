import tensorflow as tf
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten  # type: ignore


def BuildAndCompileModel():
    # Build the model
    model = Sequential([
        Conv2D(16, (3, 3), 1, activation='relu', input_shape=(28, 28, 3)),
        MaxPooling2D(),
        Conv2D(32, (3, 3), 1, activation='relu'),
        MaxPooling2D(),
        Conv2D(16, (3, 3), 1, activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(256, activation='relu'),
        Dense(3, activation='softmax')
    ])

    # Compile the model
    model.compile('adam', loss=tf.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
    model.summary()

    return model

def main() -> None:
    # Build the model
    BuildAndCompileModel()

if __name__ == '__main__':
    main()
