from image_generator import  generate_image
from aws_file_manager import move_file_to_s3
import argparse
from datetime import datetime




def _get_date_string():
    """
    Gets an identifier based on current time so each file generated is unique. Ideally
    more information should be used so several users might create images at the same time

    """
    now = datetime.now()
    return now.strftime("%Y_%m_%d_ %H_%M_%S")



def _parse_args():
    """
    Parses command line arguments.
       --size is the number of pixels in each row and column of the image
       --img-pattern is a positive integer that changes the pattern of the images generated

    """
    parser = argparse.ArgumentParser(
        description="Generate a simple image"
    )


    parser.add_argument(
        "--size",
        type=int,
        default=32,
        help="Image size in pixels"
    )
    parser.add_argument(
        "--img-pattern",
        type=int,
        default=2,
        help="changes pattern of generated image"
    )

    return parser.parse_args()







def main():
    """
    generates an image in EC3 instance and moves it to an S3 bucket
    """

    args = _parse_args()
    filename =  _get_date_string()+"_img.png"

    generate_image(filename, args.size, args.size,
                   args.img_pattern, 220, 0,0)
    move_file_to_s3(filename)


if __name__ == "__main__":
    main()
