import cv2
import os
from PIL import Image

# Set the source and destination folders
source_folder = "/home/aman/Pictures/segmentation_large/"
destination_folder = "/home/aman/Downloads/sc/"
source_folder1 = "/home/aman/Pictures/images_large/"
destination_folder1 = "/home/aman/Downloads/ic/"

# Iterate over all files in the source folder
for file in os.listdir(source_folder):
    # Open the image
    image = Image.open(os.path.join(source_folder, file))
    image1 = Image.open(os.path.join(source_folder1, file))

    # Convert the image to grayscale
    gray_image = image.convert('L')
    gray_image1 = image1.convert('L')
    # Get the width and height of the image
    width, height = gray_image.size
    width1, height1 = gray_image1.size
    if (height == height1 and width == width1):

        # Initialize counters for the number of white pixels on each quadrant
        top_left_count = 0
        top_right_count = 0
        bottom_left_count = 0
        bottom_right_count = 0

        # Count the number of white pixels on each quadrant
        for y in range(height):
            for x in range(width):
                pixel = gray_image.getpixel((x, y))
                if pixel == 255:
                    if x < width / 2 and y < height / 2:
                        top_left_count += 1
                    elif x < width / 2 and y >= height / 2:
                        bottom_left_count += 1
                    elif x >= width / 2 and y < height / 2:
                        top_right_count += 1
                    else:
                        bottom_right_count += 1

        # Crop the image based on the quadrant with the least white pixels
        if top_left_count <= top_right_count and top_left_count <= bottom_left_count and top_left_count <= bottom_right_count:
            # Crop the top left quadrant
            cropped_image = gray_image.crop((0, 0, width - (width - 799), height - (height - 191)))
            cropped_image1 = gray_image1.crop((0, 0, width - (width - 799), height - (height - 191)))
        elif top_right_count <= top_left_count and top_right_count <= bottom_left_count and top_right_count <= bottom_right_count:
            # Crop the top right quadrant
            cropped_image = gray_image.crop((width - (799), 0, width, height - (height - 191)))
            cropped_image1 = gray_image1.crop((width - (799), 0, width, height - (height - 191)))
        elif bottom_left_count <= top_left_count and bottom_left_count <= top_right_count and bottom_left_count <= bottom_right_count:
            # Crop the bottom left quadrant
            cropped_image = gray_image.crop((0, (height - 191), width - (width - 799), height))
            cropped_image1 = gray_image1.crop((0, (height - 191), width - (width - 799), height))
        else:
            # crop the bottom right quadrant
            cropped_image = gray_image.crop(((width - 799), (height - 191), width, height))
            cropped_image1 = gray_image1.crop(((width - 799), (height - 191), width, height))
        # Save the cropped image to the destination folder with the same name as the source image
        cropped_image.save(os.path.join(destination_folder, file))
        cropped_image1.save(os.path.join(destination_folder1, file))
    else:
        cropped_image.save(os.path.join(destination_folder, file))
        cropped_image1.save(os.path.join(destination_folder1, file))