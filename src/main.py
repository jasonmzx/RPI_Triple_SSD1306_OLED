
import HardwareController
from screens import TransitScreen

def main():
    
    hw_controller = HardwareController(3,2) # SCL pin 3, SDA pin 2

    display0 = hw_controller.add_screen(0)
    display1 = hw_controller.add_screen(1)
    display2 = hw_controller.add_screen(2)

    transit_display = TransitScreen(display1)
    transit_display.drawImage()
    transit_display.show()

if __name__ == "__main__":
    main()