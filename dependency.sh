#!/bin/bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r dependencies.txt

echo "Setup complete. Activate the environment with: source venv/bin/activate"

