#!/bin/bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r dependencies.txt

echo "Dependencies installed. You can run the program now."

