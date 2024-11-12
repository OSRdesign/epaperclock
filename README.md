# E-Paper Clock Display

This project displays a digital clock on a Waveshare 2.13" e-Paper HAT display connected to a Raspberry Pi.

## Hardware Requirements

- Raspberry Pi (any model)
- Waveshare 2.13" e-Paper HAT
- Proper connection of the HAT to the Raspberry Pi's GPIO pins

## Installation

1. Enable SPI interface on your Raspberry Pi:
   ```bash
   sudo raspi-config
   # Navigate to Interface Options > SPI > Enable
   ```

2. Install required packages:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-pil python3-numpy fonts-dejavu
   pip3 install -r requirements.txt
   ```

3. Run the clock:
   ```bash
   sudo python3 epaper_clock.py
   ```

## Features

- Displays current time in 24-hour format
- Shows current date
- Updates every second using partial refresh for better performance
- Clean shutdown with Ctrl+C
- Centered text layout
- Power-efficient partial updates
- Automatic font detection across different Linux distributions

## Notes

- The display will update every second using partial refresh for better performance
- Press Ctrl+C to exit cleanly and clear the display
- The script requires root privileges to access GPIO pins
- The program will automatically find the DejaVu Sans font on most Linux distributions

## Troubleshooting

If you encounter a "No module named 'waveshare_epd'" error:
1. Ensure you've installed all requirements: `pip3 install -r requirements.txt`
2. Try installing the package directly: `pip3 install waveshare-epd`

If you see font-related errors:
1. Install the DejaVu fonts package: `sudo apt-get install fonts-dejavu`