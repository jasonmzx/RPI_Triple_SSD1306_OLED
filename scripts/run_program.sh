#!bin/bash
# chmod +x run_program.sh

cd ..

# Activate the virtual environment
source TRIPLE_SSD1306_OLED_VENV/bin/activate

python3 src/TRIPLE_SSD1306_PROG.py #Entry point to program

deactivate