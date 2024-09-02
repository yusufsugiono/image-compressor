from PIL import Image, ImageOps
import numpy as np
import io
import os

INPUT_DIR = os.path.join('images', 'input')
OUTPUT_DIR = os.path.join('images', 'output')
MAX_HEIGHT = 1920
MAX_WIDTH = 1440

IMAGES = os.listdir(INPUT_DIR)

for image in IMAGES:
    img_dir = os.path.join(INPUT_DIR, image)

    img_name = image.split('.')[0]

    # Load the image
    img = Image.open(img_dir)
    img = ImageOps.exif_transpose(img)

    # Check image size
    w, h = img.size

    print(f"ORIGINAL SIZE: {w}x{h}")

    # Check image portrait or landscape
    if h > w:
        new_height = MAX_HEIGHT
        new_width = int(round(MAX_HEIGHT*(w/h), 0))
    else:
        new_width= MAX_WIDTH
        new_height = int(round(MAX_HEIGHT*(h/w), 0))

    print(f"RESIZE TO: {new_width}x{new_height}")

    # Resizing the image
    img.resize((new_width, new_height))
    
    # Convert the image to a byte array
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='JPEG')

    # Compress the image
    compressed_img = Image.open(img_byte_array)

    # Save output file
    img_output_name = os.path.join(OUTPUT_DIR, img_name + '.jpg')
    compressed_img.save(img_output_name, 'JPEG', quality=10)

print("TASK FINISHED SUCCESSFULLY!")
