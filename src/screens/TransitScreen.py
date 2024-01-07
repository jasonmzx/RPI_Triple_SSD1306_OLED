from Screen import Screen
from utility.gtfs import GTFS_Bus_Tracker, Formatted_Arrival_Entry
from PIL import Image, ImageDraw, ImageFont

from datetime import datetime
from zoneinfo import ZoneInfo

class TransitScreen(Screen):

    TIME_ZONE = None
    BUS_TRACKER = None
    
    #`display` & `refresh_rate` is for Screen Class, everything else is for GTFS configuration
    
    def __init__(self, display, refresh_rate, GTFS_URL, TIME_ZONE_STR, STOP_ID, ROUTE_ID):
        
        super().__init__(display, refresh_rate)
        
        #* === Instanciate Time Zone & Bus Tracker Objects ===
        self.TIME_ZONE = ZoneInfo(TIME_ZONE_STR) 
        self.BUS_TRACKER = GTFS_Bus_Tracker(GTFS_URL, self.TIME_ZONE, STOP_ID, ROUTE_ID)

        self._THREAD.start() # Start the Thread running Refresh Loop 


    #* Helper Draw FN:
    def _drawArrivalEntry(self, idx):

        Elm = self.BUS_TRACKER.Arrivals[idx]

        if Elm is None: #! Basic Assertion for Elm
            return 1

        # Convert arrival time and current time to aware datetime objects
        arrival_time = datetime.fromtimestamp(Elm.ARRIVAL_UNIX, self.TIME_ZONE)
        current_time = datetime.now(self.TIME_ZONE)

        # Calculate time difference in minutes and seconds
        time_diff = arrival_time - current_time
        minutes_until_arrival = int(time_diff.total_seconds() / 60)
        seconds_until_arrival = int(time_diff.total_seconds() % 60)

        # Draw formatted arrival and time until arrival
        self.draw.text((0, 14*(idx+1)), f"{Elm.FORMATTED_ARRIVAL} - {minutes_until_arrival}m {seconds_until_arrival}s", font=self.font, fill=255)
        return 0

    def drawImage(self):
        
        self.BUS_TRACKER.refreshArrivals()

        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), f"{self.BUS_TRACKER.ROUTE_ID} Arrivals:      IN:", font=self.font, fill=255)
        
        if self.BUS_TRACKER.Arrivals:
            self._drawArrivalEntry(0)
            self._drawArrivalEntry(1)
            self._drawArrivalEntry(2)
        else:
            self.draw.text((0, 13), f"No active routes...", font=self.font, fill=255)

        self.show()