#!bin/bash
# chmod +x setup.sh

cd ..

# Create a Python virtual environment
python3 -m venv TRIPLE_SSD1306_OLED_VENV

# Activate the virtual environment
source TRIPLE_SSD1306_OLED_VENV/bin/activate

# Install requirements using pip
pip install -r requirements.txt

deactivate