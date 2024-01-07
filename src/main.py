import signal 
import time
from HardwareController import HardwareController
from screens.TransitScreen import TransitScreen


def SHUTDOWN_Handler(displays):
    print("=== Cleaning up Display Threads ===")
    for display in displays:
        display.DESTROY_THREAD()
    print("Shuting down...")

def main():
    
    #TODO: put this .env
    GTFS_Source = "https://drtonline.durhamregiontransit.com/gtfsrealtime/TripUpdates"


    hw_controller = HardwareController(3,2) # SCL pin 3, SDA pin 2

    display0 = hw_controller.spawnScreenAt(0)
    display1 = hw_controller.spawnScreenAt(1)
    display2 = hw_controller.spawnScreenAt(2)

    transit_display = TransitScreen(display1, 60, GTFS_Source, "America/Toronto", "2242:1", "900")
    transit_display2 = TransitScreen(display2, 60, GTFS_Source, "America/Toronto", "2242:1", "900")

    active_displays = [transit_display, transit_display2]

    #* Upon Termination or Interrupt Signals, Initiate Shutdown

    signal.signal(signal.SIGTERM, lambda x, frame: SHUTDOWN_Handler(active_displays))
    signal.signal(signal.SIGINT, lambda x, frame: SHUTDOWN_Handler(active_displays))


    # Keep Lifetime of main function

    try:
        while True:
            time.sleep(1)  
    except Exception:
        pass

if __name__ == "__main__":
    main()