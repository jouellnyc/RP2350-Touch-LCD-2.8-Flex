import sys
sys.path.append('./libraries')
import time
from machine import Pin, I2C
from lcd_2inch8 import ST7789, CST328
import lvgl as lv
from lv_port import lv_port

I2C_SCL = 7
I2C_SDA = 6

LCD_WIDTH = 240
LCD_HEIGHT = 320

def load_map_data(module_base_name):
    """
    Dynamically loads map data based on a consistent naming convention.
    
    Args:
        module_base_name (str): The name of the module to import (e.g., 'qq_240_map_data' or 'cg_225x220_map_data').

    Returns:
        tuple: A tuple containing (map_data, map_width, map_height).
    """
    try:
        module = __import__(module_base_name)
        
        # The data variable name is the same as the module name.
        data_var_name = module_base_name
        
        # The width/height variables have the '_data' suffix removed.
        prefix = module_base_name.replace('_data', '')
        width_var_name = f"{prefix}_width"
        height_var_name = f"{prefix}_height"

        map_data = getattr(module, data_var_name)
        map_width = getattr(module, width_var_name)
        map_height = getattr(module, height_var_name)
        
        return map_data, map_width, map_height
    except (ImportError, AttributeError) as e:
        print(f"Error loading map data from module '{module_base_name}': {e}")
        return None, None, None

class lvgl_ui(object):
    def __init__(self, map_data, map_width, map_height):
        self.scr = lv.obj()
        self.tv = lv.tileview(self.scr)
        self.tv.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        self.tile1 = self.tv.add_tile(0, 0, lv.DIR.BOTTOM)
        
        waveshare_lcd_2_8_img = lv.image_dsc_t(
            dict(
                header=dict(cf=lv.COLOR_FORMAT.RGB565, w=map_width, h=map_height),
                data_size=len(map_data),
                data=map_data
            )
        )

        img = lv.image(self.tile1)          # Create image widget
        print(f"Image dimensions: {map_width} x {map_height}")
        print(f"Data length: {len(map_data)}")
        print(f"Expected data length: {map_width * map_height * 2}")
        print(f"First few bytes: {map_data[:20]}")
        img.set_src(waveshare_lcd_2_8_img)    # Set the image source
        img.align(lv.ALIGN.CENTER, 0, 0)      # Center the image
        lv.screen_load(self.scr)              # Load the screen

if __name__ == 'load_png_to_ldc_flex':
    # Set the desired map file base name here
    # For qq_240_map_data.py, use 'qq_240_map_data'
    # For cg_225x220_map_data.py, use 'cg_225x220_map_data'
    #DESIRED_MAP_FILE = 'cg_225x220_map_data'
    DESIRED_MAP_FILE = 'qq_200_map_data'
    
    qq_120_map_data, qq_120_map_width, qq_120_map_height = load_map_data(DESIRED_MAP_FILE)

    if qq_120_map_data:
        i2c = I2C(id=1, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400_000)
        display = ST7789(LCD_WIDTH, LCD_HEIGHT)
        display.set_brightness(50)
        touch = CST328(i2c, LCD_WIDTH, LCD_HEIGHT)
        lv_port(display, touch)
        lvgl_ui(qq_120_map_data, qq_120_map_width, qq_120_map_height)
        while True:
            pass