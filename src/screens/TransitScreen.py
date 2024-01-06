from Screen import Screen
from utility.gtfs import GTFS_Bus_Tracker, Formatted_Arrival_Entry
from PIL import Image, ImageDraw, ImageFont

class TransitScreen(Screen):

    BUS_TRACKER = None
    
    #`display` is for Screen Class, everything else is for GTFS configuration
    
    def __init__(self, display, GTFS_URL, TIME_ZONE, STOP_ID, ROUTE_ID):
        super().__init__(display)

        self.BUS_TRACKER = GTFS_Bus_Tracker(GTFS_URL, TIME_ZONE, STOP_ID, ROUTE_ID)

    def drawImage(self):

        self.BUS_TRACKER.refreshArrivals()

        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), f"NEXT: {self.BUS_TRACKER.ROUTE_ID}", font=self.font, fill=255)
        
        Elm0 = self.BUS_TRACKER.Arrivals[0]
        #Elm1 = self.BUS_TRACKER.Arrivals[1]
        
        self.draw.text((0, 13), f"{Elm0.FORMATTED_ARRIVAL} R: {Elm0.ROUTE_ID}", font=self.font, fill=255)
        #self.draw.text((0, 13), f"{Elm1.FORMATTED_ARRIVAL} R: {Elm0.ROUTE_ID}", font=self.font, fill=255)


        self.show()