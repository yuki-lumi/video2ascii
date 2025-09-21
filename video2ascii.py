#!.venv
import argparse
import cv2
from pathlib import Path
from PIL import Image
import moviepy
import os
import shutil

def image2ascii(pngpath, txtpath):

    folder = Path(f"{pngpath}")
    ImageCount = sum(1 for f in folder.iterdir() if f.is_file())

    for image in range(ImageCount):
        digits = len(str(ImageCount))
        frame_id = str(image).zfill(digits)

        # Open image
        im = Image.open(f"{pngpath}/frame{frame_id}.PNG")

        # Resize
        im = im.resize((120,40))
        pillars, lines = im.size

        ##  Grey scale
        im = im.convert("L")
        # Basic one
        chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

        # F1 (dont worry about this one)
        #chars = ["@", "#", "S", "%", " ", " ", "-", ";", ":", ",", ".", " "]

        pixels = list(im.getdata())
        new_pixels = []
        for pixel in pixels:
            new_pixels.append(chars[pixel//22])

            ## Write to txt
        with open(f"{txtpath}/frame{frame_id}.txt", "w") as file:
            for line in range(lines):
                for pillar in range(pillars):
                    file.write(new_pixels[pillars * line + pillar])
                file.write("\n")

    return 0

def getframes(video, savefolder):
    try:
        with Image.open(f'{video}') as im:
            frame_count = im.n_frames

            for frame in range(frame_count):
                digits = len(str(frame_count))
                frame_id = str(frame).zfill(digits)
                im.seek(frame)
                im.save(f"{savefolder}/frame{frame_id}.PNG", "PNG")
    except:
            ##  Turn into mp4
        filename, file_extension = os.path.splitext(f'{video}')
        clip = moviepy.VideoFileClip(f"{filename}{file_extension}")
        clip.write_videofile(f"{filename}.mp4")

        sourcevid = cv2.VideoCapture(f"{filename}.mp4")
        video_framecount = int(sourcevid.get(cv2.CAP_PROP_FRAME_COUNT))
        video_digits = len(str(video_framecount))
        count = 0
        success = True
        while success:
            if count == video_framecount:
                break
            else:
                frame_id = str(count).zfill(video_digits)
                success, image = sourcevid.read()
                cv2.imwrite(f"{savefolder}/frame{frame_id}.PNG", image)
                count += 1
    return 0

parser = argparse.ArgumentParser(
    prog='video2ascii',
    description='This program extracts frames from video and turns those frames to ASCII art and stores them in txt files.',
    epilog="Creates txt files on your current folder.",
    usage="%(prog)s video-path)")

parser.add_argument("video_path", help="Path to your video from your current location")
args = parser.parse_args()

# Specify the nested directory structure
file_name = os.path.splitext(f"{args.video_path}")[0]

# Create nested directories
for x in {"/txt", "/frames"}:
    file_path = file_name + x
    try:
        os.makedirs(file_path)
        print(f"Nested directories '{file_path}' created successfully.")
    except FileExistsError:
        print(f"One or more directories in '{file_path}' already exist.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



getframes(args.video_path, f"{file_name}/frames")
image2ascii(f"{file_name}/frames",f"{file_name}/txt")

shutil.rmtree(f"{file_name}/frames")

play_command = f'while read frame; do   clear;   cat "$frame";   sleep 0.1; done < <(ls {file_name}/txt/frame*.txt | sort)'
print(f"To play the ASCII video, in your terminal write the following code.\n {play_command}\n Manipulate the number after 'sleep' to change fps. Enjoy!")



