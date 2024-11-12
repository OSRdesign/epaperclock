#!/usr/bin/python3
import sys
import os
import time
from datetime import datetime
from waveshare_epaper import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

class EpaperClock:
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.width = self.epd.height  # Note: rotation makes width = height
        self.height = self.epd.width  # and height = width
        
    def initialize(self):
        try:
            self.epd.init(self.epd.FULL_UPDATE)
            self.epd.Clear(0xFF)  # Clear to white
        except Exception as e:
            print(f"Error initializing display: {e}")
            sys.exit(1)

    def create_time_image(self):
        # Create new image with white background
        image = Image.new('1', (self.width, self.height), 255)
        draw = ImageDraw.Draw(image)
        
        # Load a font
        font_time = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
        font_date = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
        
        # Get current time and date
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%Y-%m-%d")
        
        # Calculate positions for centered text
        time_w = draw.textlength(time_str, font=font_time)
        date_w = draw.textlength(date_str, font=font_date)
        
        time_x = (self.width - time_w) // 2
        date_x = (self.width - date_w) // 2
        
        # Draw the time and date
        draw.text((time_x, 20), time_str, font=font_time, fill=0)
        draw.text((date_x, 70), date_str, font=font_date, fill=0)
        
        return image

    def update_display(self):
        while True:
            try:
                # Partial update for smoother refresh
                self.epd.init(self.epd.PART_UPDATE)
                
                # Create and display the time image
                time_image = self.create_time_image()
                self.epd.display_Partial(self.epd.getbuffer(time_image))
                
                # Wait for a second before next update
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("Cleaning up...")
                self.epd.init(self.epd.FULL_UPDATE)
                self.epd.Clear(0xFF)
                self.epd.sleep()
                break
                
            except Exception as e:
                print(f"Error updating display: {e}")
                sys.exit(1)

def main():
    try:
        clock = EpaperClock()
        clock.initialize()
        clock.update_display()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()