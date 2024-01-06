from google.transit import gtfs_realtime_pb2
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

class Formatted_Arrival_Entry:
    ARRIVAL_UNIX: int = None
    FORMATTED_ARRIVAL: str = None
    ROUTE_ID: str = None
    VEHICLE_ID: str = None
    # Didn't include stop ID, as it's redundant for this app.

    def __init__(self, arrival_time_unix, route, vehicle):
        self.ARRIVAL_UNIX = arrival_time_unix
        # * Format :: %I is the hour (01 to 12) , %M is the minute, %p is either AM or PM.
        self.FORMATTED_ARRIVAL = datetime.fromtimestamp(arrival_time_unix).strftime("%I:%M %p")

        self.ROUTE_ID = route
        self.VEHICLE_ID = vehicle

    def __repr__(self):  # for DEBUG purposes
        return (
            f"Formatted_Arrival_Entry( ARRIVAL_UNIX={self.ARRIVAL_UNIX}, "
            f"FORMATTED_ARRIVAL= '{self.FORMATTED_ARRIVAL}', "
            f"ROUTE_ID= '{self.ROUTE_ID}', "
            f"VEHICLE_ID= '{self.VEHICLE_ID}' )"
        )


class GTFS_Bus_Tracker:
    Arrivals = []

    # --- Class Configuration Variables ---
    STOP_ID: str = None
    ROUTE_ID: str = None
    GTFS_URL: str = None
    T_ZONE: str = None

    def __init__(self, gtfs_url, time_zone, stop_id, route_id):
        self.GTFS_URL = gtfs_url
        self.T_ZONE = time_zone
        self.STOP_ID = stop_id
        self.ROUTE_ID = route_id


    #TODO: Potentially make this async
    def refreshArrivals(self):
        
        time_zone = ZoneInfo(self.T_ZONE)

        # * 1. ==== Request & Get Raw GTFS Realtime Data, and Decode to Object
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(self.GTFS_URL)
        feed.ParseFromString(response.content)

        # * 2. ==== Build List of Formatted Arrival Objects
        for entity in feed.entity:
            if entity.HasField("trip_update"):
                for stop_time_update in entity.trip_update.stop_time_update:

                    route_id = ( #Initially Pull-in Route ID as we'll be comparing on this field aswell
                        entity.trip_update.trip.route_id
                        if entity.trip_update.trip
                        else "N/A"
                    )

                    if stop_time_update.stop_id == self.STOP_ID and route_id == self.ROUTE_ID:
                        
                        arrival_time_unix = stop_time_update.arrival.time
                        
                        vehicle_id = (
                            entity.trip_update.vehicle.id
                            if entity.trip_update.vehicle
                            else "N/A"
                        )

                        self.Arrivals.append(
                            Formatted_Arrival_Entry(
                                arrival_time_unix, route_id, vehicle_id
                            )
                        )

        # * 3. ==== Sort Arrivals based on Unix Timestamp:
        self.Arrivals.sort(key=lambda entry: entry.ARRIVAL_UNIX)

        # * 4. ==== Manully Remove any entries that have passed by | Compare to Eastern Standard Time | Toronto, ON (GMT-5)
        current_time = datetime.now(time_zone)

        self.Arrivals = [
            arrival
            for arrival in self.Arrivals
            if datetime.fromtimestamp(arrival.ARRIVAL_UNIX, time_zone) > current_time
        ]

        print("____DEBUG PRINTING____")
        for x in self.Arrivals:
            print(x)