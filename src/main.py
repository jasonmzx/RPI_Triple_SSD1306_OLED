
from HardwareController import HardwareController
from screens.TransitScreen import TransitScreen

def main():
    
    hw_controller = HardwareController(3,2) # SCL pin 3, SDA pin 2

    display0 = hw_controller.spawnScreenAt(0)
    display1 = hw_controller.spawnScreenAt(1)
    display2 = hw_controller.spawnScreenAt(2)

    transit_display = TransitScreen(display1)
    transit_display.drawImage()
    transit_display.show()

if __name__ == "__main__":
    main()