#Assume a png is called qq.png

Step 1: On a Linux PC

```
convert qq.png -resize 125x125! qq_125.png
```

Step 2: On a Linux PC
```
python3 png_converter.py  qq_125.png  qq_125_map
```

Converting qq_125.png...
Image size: 125x125
Generated 31250 bytes (15625 pixels)
Saved to qq_125_map_data.py
Dimensions: 125x125
Data size: 31250 bytes

Conversion successful!

Use: from qq_125_map_data import qq_125_map_data, qq_125_map_width, qq_125_map_height

Step 3: On rp2350
Upload qq_125_map_data to / and edit load_png_to_ldc_flex.py to point to qq_125_map_data

Step 4: On rp2350
```
import load_png_to_ldc_flex.py
```




NOTE: An issue is that ImageMagick's -resize 125x125 preserves aspect ratio by default.
To force an exact square size with ImageMagick, use an !.
If you don't mind some distortion, or the crop version if you want to keep the image looking natural but perfectly square!

