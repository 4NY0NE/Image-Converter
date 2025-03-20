# ======================================================#
#         ___  _   _ __   __ _____  _   _  _____ 
#        /   || \ | |\ \ / /|  _  || \ | ||  ___|
#       / /| ||  \| | \ V / | | | ||  \| || |__
#      / /_| || . ` |  \ /  | | | || . ` ||  __|
#      \___  || |\  |  | |  \ \_/ /| |\  || |___
#          |_/\_| \_/  \_/   \___/ \_| \_/\____/
#     Follow me on github: https://github.com/4NY0NE                                    
# ======================================================#

import os
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

def convert_image():
    print(Fore.YELLOW + "\n=== Image Converter ===" + Style.RESET_ALL)
    
    image_path = input("Enter the image path (e.g., image.png): ").strip()

    if not os.path.isfile(image_path):
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        return

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(Fore.RED + f"Error opening image: {e}" + Style.RESET_ALL)
        return

    print("\nConversion options:")
    print("1 - JPEG")
    print("2 - PNG")
    print("3 - ICO")
    print("4 - BMP")
    print("5 - GIF")
    print("6 - TIFF")
    print("7 - WEBP")
    option = input("Choose an option (1-7): ").strip()

    formats = {
        "1": "JPEG",
        "2": "PNG",
        "3": "ICO",
        "4": "BMP",
        "5": "GIF",
        "6": "TIFF",
        "7": "WEBP"
    }

    if option not in formats:
        print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
        return

    new_format = formats[option]
    new_name = os.path.splitext(image_path)[0] + "." + new_format.lower()

    try:
        image.save(new_name, new_format)
        print(Fore.GREEN + f"\nImage converted and saved as: {new_name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error saving image: {e}" + Style.RESET_ALL)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1 - Convert Image")
        print("2 - Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            convert_image()
        elif choice == "2":
            print(Fore.CYAN + "\nExiting the program. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option! Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
