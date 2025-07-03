# Image-Resizer
# Image Resizer

A simple Python script to resize images in bulk using the Pillow library.

## Features

- Resizes all images in the `Images/` directory.
- Supports common image formats: JPG, JPEG, PNG, BMP, GIF, WEBP.
- Allows you to specify a new width and height for each image.
- Maintains aspect ratio if height is set to 0.
- Saves resized images to the `ResizedImages/` directory.

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library

## Installation

1. Clone or download this repository.
2. Install Pillow if you haven't already:

    ```sh
    pip install pillow
    ```

## Usage

1. Place the images you want to resize in the `Images/` folder.
2. Run the script:

    ```sh
    python app.py
    ```

3. For each image, enter the desired width (or press Enter for default 800px) and height (or enter 0 to maintain aspect ratio).
4. Resized images will be saved in the `ResizedImages/` folder.

## Project Structure

```
app.py
Images/
    Anime.jpg
    GYM-BOY.jpg
    Runner.jpg
ResizedImages/
```

## License

This project is licensed under the MIT
