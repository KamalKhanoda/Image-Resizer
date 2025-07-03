import os
from PIL import Image

def resize_image(img, NewWidth, NewHeight):
    # Resize the image to the specified width while maintaining the aspect ratio.
    width, height = img.size
    if NewHeight is None:
        # If NewHeight is not provided, calculate it to maintain aspect ratio
        NewHeight = int((NewWidth / width) * height)

    resized_image =  img.resize((NewWidth, NewHeight))
    return resized_image

imgFiles = os.listdir("Images")
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']
for file in imgFiles:
    file_ext = os.path.splitext(file)[1].lower()
    if file_ext in image_extensions:
        img_path = os.path.join("Images",file)
        if os.path.exists("ResizedImages"):
            output_path = os.path.join("ResizedImages", file)
        else:
            os.makedirs("ResizedImages")
            output_path = os.path.join("ResizedImages", file)
        img = Image.open(img_path)
        NewWidth = int(input("Enter the new width for the image (or press Enter to use default 800px): "))
        NewHeight = int(input("Enter the new height for the image (or press 0 to maintain aspect ratio):"))

        
        if not NewWidth:
            NewWidth = 800

        if NewHeight == 0:
            NewHeight = None

        print(f"Resizing {file}............")
        resized_img = resize_image(img, NewWidth, NewHeight)
        resized_img.save(output_path) 
        print(f"image resized and saved to {output_path}")



