from Screen import Screen
from utility.gtfs import GTFS_Bus_Tracker, Formatted_Arrival_Entry
from PIL import Image, ImageDraw, ImageFont

class TransitScreen(Screen):

    BUS_TRACKER = None

    def __init__(self, display):
        super().__init__(display)

        # TODO: Put these in .env
        GTFS_Source = "https://drtonline.durhamregiontransit.com/gtfsrealtime/TripUpdates"

        BUS_TRACKER = GTFS_Bus_Tracker(GTFS_Source,"America/Toronto", "2242:1", "920")
        BUS_TRACKER.refreshArrivals()

    def drawImage(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), "NXT:  920 | 900 ", font=self.font, fill=255)
        
        Elm0 = self.BUS_TRACKER.Arrivals[0]
        
        self.draw.text((0, 13), f"{Elm0.FORMATTED_ARRIVAL} R: {Elm0.ROUTE_ID}", font=self.font, fill=255)

        self.show()