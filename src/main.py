import time
from HardwareController import HardwareController
from screens.TransitScreen import TransitScreen

def main():
    
    #TODO: put this .env
    GTFS_Source = "https://drtonline.durhamregiontransit.com/gtfsrealtime/TripUpdates"


    hw_controller = HardwareController(3,2) # SCL pin 3, SDA pin 2

    display0 = hw_controller.spawnScreenAt(0)
    display1 = hw_controller.spawnScreenAt(1)
    display2 = hw_controller.spawnScreenAt(2)

    transit_display = TransitScreen(display1, 60, GTFS_Source, "America/Toronto", "2242:1", "900")

    # Keep Lifetime of main function

    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        print("Program terminated by user")

    #* === Cleanup Screens ===
        transit_display.DESTROY_THREAD()

if __name__ == "__main__":
    main()