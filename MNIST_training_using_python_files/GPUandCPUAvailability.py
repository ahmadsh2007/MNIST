import tensorflow as tf

def GPUAvailability():
    # Check GPU availability
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print("GPUs Available: ", len(gpus))
        print("GPU Details: ", gpus)
    else:
        print("No GPUs Available.")

def CPUAvailability():
    # Check CPU availability
    cpu = tf.config.list_physical_devices('CPU')
    if cpu:
        print("CPUs Available: ", len(cpu))
        print("CPU Details: ", cpu)
    else:
        print("No CPUs Available.")

def main() -> None:
    GPUAvailability()
    CPUAvailability()

if __name__ == '__main__':
    main()