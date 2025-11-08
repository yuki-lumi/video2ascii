# video2ascii
video2ascii is a python program that turns each frame in a video to ASCII art and saves them in .txt files. After that you can see them in your terminal as a 'video' by running the code given to you.
# Installation
## Prerequisites
* Python 3.x
* Git
## Installation
1. Clone repository
   ```
   git clone https://github.com/yuki-lumi/video2ascii
   cd video2ascii
   ```
2. Install python dependencies.
    ```
    pip install -r dependencies.txt
    ```
    **OR**
    Install them in a virtual environment.
  
    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r dependencies.txt
    ```
    **NOTE:** If you decide to install in a virtual enviroment you will need to run ```source .venv/bin/activate``` before each use of the program.
  ## Usage
  Simply run ```python video2ascii.py yourvideo```. Program will output a command you can run to see your video in ASCII form :D.
  #
  **Example Usage**
  ```
  python video2ascii.py funnycat.mp4
  while read frame; do   clear;   cat "$frame";   sleep 0.1; done < <(ls funnycat/txt/frame*.txt | sort)
  ```
  
