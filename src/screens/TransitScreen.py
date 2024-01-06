from ..Screen import Screen
from ..utility.gtfs import GTFS_Bus_Tracker
from PIL import Image, ImageDraw, ImageFont

class TransitScreen(Screen):

    def __init__(self, display):
        super().__init__(display)

        # TODO: Put these in .env
        GTFS_Source = "https://drtonline.durhamregiontransit.com/gtfsrealtime/TripUpdates"

        bustrack = GTFS_Bus_Tracker(GTFS_Source,"America/Toronto", "2242:1", "920")
        bustrack.refreshArrivals()

    def drawImage(self):

        self.show()