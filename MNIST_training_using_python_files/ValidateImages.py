import os
import cv2  # type: ignore
import imghdr

def ValidateImages(data_dir):
    # Validate images
    image_exts = ['jpeg', 'jpg', 'bmp', 'png']
    for image_class in os.listdir(data_dir):
        for image in os.listdir(os.path.join(data_dir, image_class)):
            image_path = os.path.join(data_dir, image_class, image)
            try:
                img = cv2.imread(image_path)
                tip = imghdr.what(image_path)
                if tip not in image_exts:
                    print(f'Image not in ext list {image_path}')
                    os.remove(image_path)
            except Exception as e:
                print(f'Issue with image {image_path}')

def main() -> None:
    # Define the directory containing your training data
    data_dir = r'MNIST/mnist_png/training'
    ValidateImages(data_dir)

if __name__ == '__main__':
    main()
