from PIL import Image, ImageEnhance
import os

def enhance_image(image_path, brightness=1.0, contrast=1.0, sharpness=1.0):
    with Image.open(image_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness)
        return img

def upscale_image(image, factor=2):
    width, height = image.size
    new_width, new_height = width * factor, height * factor
    image = image.resize((new_width, new_height), resample=Image.LANCZOS)
    return image

def get_best_print_size(img_width, img_height, multiplier_range=(3, 7)):
    current_ratio = img_width / img_height
    best_size = (0, 0)
    best_diff = float('inf')
    for multiplier in range(multiplier_range[0], multiplier_range[1] + 1):
        new_width = multiplier * current_ratio
        new_height = multiplier
        new_diff = abs(new_width - new_height)
        if new_diff < best_diff:
            best_diff = new_diff
            best_size = (new_width, new_height)
    return best_size

def enhance_and_upscale_images(folder_path, brightness=1.0, contrast=1.0, sharpness=1.0, upscale_factor=2, dpi=1200, multiplier_range=(1, 10)):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    output_path = os.path.join(folder_path, 'enhancend')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            input_filepath = os.path.join(folder_path, filename)
            output_filepath = os.path.join(output_path, filename)
            with Image.open(input_filepath) as img:
                current_dpi = img.info.get("dpi", (72, 72))[0]
                width, height = img.size
                best_size = get_best_print_size(width, height, multiplier_range)
                new_width, new_height = int(dpi * best_size[0]), int(dpi * best_size[1])
                new_resolution = (new_width, new_height)
                new_size = (int(new_width * 0.0254 / current_dpi), int(new_height * 0.0254 / current_dpi))
            img = enhance_image(input_filepath, brightness, contrast, sharpness)
            img = upscale_image(img, upscale_factor)
            dpi_new = max(dpi, current_dpi)
            img = img.resize(new_resolution, resample=Image.LANCZOS)
            img.save(output_filepath, dpi=(dpi_new, dpi_new))
            print(f"{filename} processed. Current DPI: {current_dpi}. New print size: {new_size} inches.")

folder_path = input("Enter folder path: ")
multiplier = int(input("Enter print size multiplier (1-10): "))
multiplier_range = (multiplier, multiplier)
enhance_and_upscale_images(folder_path, multiplier_range=multiplier_range)
