# Micropython LVGL Display Script 

This project demonstrates how to dynamically load and display different image assets on a Waveshare LCD (ST7789) using MicroPython and the LVGL UI library. It provides a flexible and maintainable way to switch between various image maps without modifying the core code.

## Features

- **Dynamic Image Loading:** Loads different image files at runtime by changing a single variable.
- **Parameterized Configuration:** Avoids static imports, making it easy to add or remove new image files.
- **Hardware Abstraction:** Utilizes `lv_port` for seamless integration with the ST7789 LCD and CST328 touch controller.
- **Modular Design:** Separates the UI logic from the image data, promoting a clean code structure.

## Requirements

### Hardware
- An ESP32-based development board.
- Waveshare 2.8-inch LCD with ST7789 driver.
- CST328 touch controller.

### Software
- MicroPython firmware installed on your ESP32 board.
- The `lvgl` library for MicroPython.
- The `lcd_2inch8` library from your project (and its dependencies).

## Steps to Get Started

### Step 1: File Structure

Ensure your project has the following file structure. The custom map data files (`.py` files containing the image data) should be in the main project directory.

├── main.py
├── libraries/
│   ├── lcd_2inch8.py
│   ├── lv_port.py
│   └── ...
├── qq_240_map_data.py


### Step 2: Prepare Your Image Data

Your image data files must follow a consistent naming convention for the dynamic loader to work.

- **File Name:** `[name]_data.py` (e.g., `my_custom_map_data.py`)
- **Variables Inside the File:**
    - `[name]_data` (e.g., `my_custom_map_data`)
    - `[name]_width` (e.g., `my_custom_map_width`)
    - `[name]_height` (e.g., `my_custom_map_height`)

If your files do not follow this pattern, the dynamic loader will fail with an `AttributeError`.

### Step 3: Configure `main.py`

In your `main.py` file, you only need to change one line to select which image map to load.

Locate the following line:

```python
DESIRED_MAP_FILE = 'cg_225x220_map_data'
```



Change the value to the base name of the file you want to load (without the .py extension).

Examples:

To load qq_240_map_data.py, set DESIRED_MAP_FILE = 'qq_240_map_data'

To load cg_225x220_map_data.py, set DESIRED_MAP_FILE = 'cg_225x220_map_data'

### Step 4: Run the Code

Upload all your files to your ESP32 board. You can use a tool like ampy or thonny for this.

After uploading, reset the device. The script will automatically load the specified image and display it on the LCD.

Troubleshooting
ImportError: no module named ...:
This means the script cannot find your image data file. Check that the file is uploaded to the board and that the name in DESIRED_MAP_FILE matches the filename exactly.

AttributeError: 'module' object has no attribute '...':
This error occurs when the script finds the file but cannot find the variables inside it. Double-check that the variable names inside your image data file (.py) match the required naming convention as described in Step 2.



