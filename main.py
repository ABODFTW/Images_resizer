import os
from PIL import Image
from resizeimage import resizeimage


resize_path_input = "./images_resize_input/"
adjust_path_input = "./images_adjust_input/"
accepted_extensions = ["png" , "jpeg" , "jpg"]
output_extension = "jpg"

# this will change the size so both height and width match the biggest number of both
def adjust():
    progress = 0
    for img in os.listdir(adjust_path_input):
        image_ext = img.split(".")[-1]
        image_name = img.split(".")[0]
        if image_ext in accepted_extensions:
            with open(adjust_path_input + img, 'r+b') as f:
                with Image.open(f) as image:
                    width, height = image.size
                    if height > width:
                        output_size = height
                    else : 
                        output_size = width
                    adjusted = resizeimage.resize_contain(image, [output_size, output_size])
                    adjusted.save(f'output_adjusted/{image_name}' + "." + output_extension, image.format)
        total = len(os.listdir(adjust_path_input))
        progress+=1
        print(f"{progress} of {total} has been adjusted")
    print("Images has been succesfuly adjusted and saved on output_adjusted folder")

# this will make the images height and width exactly as required
def resize(output_size):
    progress = 0
    for img in os.listdir(resize_path_input):
        image_ext = img.split(".")[-1]
        image_name = img.split(".")[0]
        if image_ext in accepted_extensions:
            with open(resize_path_input + img, 'r+b') as f:
                with Image.open(f) as image:
                    resized = resizeimage.resize_contain(image, [output_size,output_size])
                    resized.save(f'output_resized/{image_name}' + "." + output_extension , image.format)
        total = len(os.listdir(adjust_path_input))
        progress+=1
        print(f"{progress} of {total} has been resized")
    print("Images has been succesfuly resized and saved on output_resized folder")


if __name__ == "__main__":
    mode = input("Type 'a' for adjusting mode or 'r' for resize mode:")
    if "r" in mode:
        output_extension = input("Type png or jpg for the images extension :")
        if output_extension == "png" or output_extension == "jpg":
            print("You've chossen Resize mode.")
            # resize images
            output_size = input("Please Enter the desired size of the image e.g 500 : ")
            print("Resizing...")
            output_size = int(output_size)
            resize(output_size=output_size)
        else:
            print("sorry I couldn't identifiy your input please try again.")
    elif "a" in mode:
        output_extension = input("Type png or jpg for the images extension :")
        if output_extension == "png" or output_extension == "jpg":
            print("You've chossen Adjust mode, Adjusting...")
            adjust()
        else:
            print("sorry I couldn't identifiy your input please try again.")
    else :
        print("sorry I couldn't identifiy your input please try again.")
