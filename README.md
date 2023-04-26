# Image Enhancer and Upscaler

This script is designed to enhance and upscale images in a folder using the Python Imaging Library (PIL). The script will take a folder path and a print size multiplier as input, and then it will process all the .jpg files in the folder using the following steps:

1. Enhance the image using the specified brightness, contrast, and sharpness values.
2. Upscale the image by a specified factor.
3. Calculate the best print size for the image based on the current aspect ratio and the specified print size multiplier.
4. Resize the image to the new print size with the specified DPI.
5. Save the processed image to a new folder within the input folder.

## Requirements

- Python 3.x
- Pillow (PIL fork) (install with `pip install Pillow`)

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script by typing `python image_enhancer_upscaler.py`.
4. Enter the folder path containing the images you want to process when prompted.
5. Enter the print size multiplier (1-10) when prompted.
6. Wait for the script to finish processing the images.

Note: The script will create a new folder within the input folder called 'enhancend' to store the processed images.

## Parameters

The script takes the following parameters:

- `folder_path` (string): The path to the folder containing the images to be processed.
- `brightness` (float): The brightness enhancement factor (default=1.0).
- `contrast` (float): The contrast enhancement factor (default=1.0).
- `sharpness` (float): The sharpness enhancement factor (default=1.0).
- `upscale_factor` (int): The factor by which to upscale the image (default=2).
- `dpi` (int): The DPI to use for the processed image (default=1200).
- `multiplier_range` (tuple): The range of print size multipliers to consider (default=(1,10)).

## Output

The script will output the following:

- A new folder called '2.0' within the input folder containing the processed images.
- A print size for each processed image in inches.