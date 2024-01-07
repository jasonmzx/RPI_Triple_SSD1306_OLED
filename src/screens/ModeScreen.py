from Screen import Screen

from datetime import datetime
from zoneinfo import ZoneInfo
from PIL import ImageFont

class ModeScreen(Screen):

    TIME_ZONE = None
    HEADING_STR : str = ""

    def __init__(self,display,refresh_rate, HEADING_STR, TIME_ZONE_STR):

        super().__init__(display, refresh_rate,)

        self.TIME_ZONE = ZoneInfo(TIME_ZONE_STR) 
        self.HEADING_STR = HEADING_STR

        self._THREAD.start() # Start the Thread running Refresh Loop 

    def drawImage(self):
        
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        
        self.font = ImageFont.load_default(size=18)
        self.draw.text((0, 1), self.HEADING_STR, font=self.font, fill=255)
        
        self.font = ImageFont.load_default(size=16)
        
        # Get current time and format it
        current_time = datetime.now(self.TIME_ZONE)
        time_str = current_time.strftime("%I:%M %p")  # Format: "10:22 AM"
        tz_name = current_time.tzname()  # Get timezone abbreviation

        self.draw.text((0, 30), f"{time_str}       {tz_name}", font=self.font, fill=255)

        self.show()