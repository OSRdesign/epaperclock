#!/usr/bin/python3
import sys
import os
import time
from datetime import datetime
from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont

class EpaperClock:
    def __init__(self):
        self.epd = epd2in13_V3.EPD()
        self.width = self.epd.height  # Note: rotation makes width = height
        self.height = self.epd.width  # and height = width
        self.font_path = self._get_font_path()
        
    def _get_font_path(self):
        """Get the appropriate font path based on system"""
        common_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Debian/Ubuntu
            '/usr/share/fonts/TTF/DejaVuSans.ttf',              # Arch Linux
            '/usr/share/fonts/dejavu/DejaVuSans.ttf'            # Fedora
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
                
        raise FileNotFoundError("Could not find DejaVuSans font. Please install dejavu-fonts package.")
        
    def initialize(self):
        """Initialize the e-Paper display"""
        try:
            self.epd.init(self.epd.FULL_UPDATE)
            self.epd.Clear(0xFF)  # Clear to white
        except Exception as e:
            print(f"Error initializing display: {e}")
            sys.exit(1)

    def create_time_image(self):
        """Create an image with the current time and date"""
        # Create new image with white background
        image = Image.new('1', (self.width, self.height), 255)
        draw = ImageDraw.Draw(image)
        
        # Load fonts
        font_time = ImageFont.truetype(self.font_path, 36)
        font_date = ImageFont.truetype(self.font_path, 16)
        
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
        """Main loop to update the display"""
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
    """Main entry point of the application"""
    try:
        clock = EpaperClock()
        clock.initialize()
        clock.update_display()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()