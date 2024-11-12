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

2. Install required packages:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-pil python3-numpy
   pip3 install -r requirements.txt
   ```

3. Run the clock:
   ```bash
   python3 epaper_clock.py
   ```

## Features

- Displays current time in 24-hour format
- Shows current date
- Updates every second
- Clean shutdown with Ctrl+C
- Centered text layout
- Power-efficient partial updates

## Notes

- The display will update every second using partial refresh for better performance
- Press Ctrl+C to exit cleanly and clear the display
- The script requires root privileges to access GPIO pins