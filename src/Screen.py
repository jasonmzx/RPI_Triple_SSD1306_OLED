import threading
import time
from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont

class Screen(ABC):

    def __init__(self, display, refresh_rate):
        
        self.display = display #* Actual Reference to I2C Screen Element 

        self.width = display.width
        self.height = display.height
        self.image = Image.new('1', (self.width, self.height))
        
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default(size=14)

        self.refresh_rate = refresh_rate

        #* === Threading Class Attributes (prefixed with `_` denoting "private" attribs) ====

        self._DESTROY = threading.Event() #This event tells the thread if it's destroyed or not
        self._THREAD  = threading.Thread(target=self._refresh_loop) 

    def show(self): 
        
        self.display.image(self.image)        
        self.display.show()

    def clear_screen(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.show()

    @abstractmethod
    def drawImage(self):
        #This class method is defined by Classes implementing Screen
        pass

    #* Threading Functionality (Pertaining to Refresh of Screen) 

    def DESTROY_THREAD(self):
        self._DESTROY.set()
        self._THREAD.join()
        self.clear_screen()


    def _refresh_loop(self):

        #! The reason i'm not doing `time.sleep(self.refresh_rate)`
        #! Is because it takes forever for them to .join() upon Destruction of threads
        #! Now the OLED Screens have to "wait" maximum 1 second to turn off, upon termination of program

        TICK_DURATION = 0.5

        second_counter = self.refresh_rate

        while not self._DESTROY.is_set():
    
            if second_counter == self.refresh_rate:
                self.drawImage()
                second_counter =  TICK_DURATION
            else:
                second_counter += TICK_DURATION

            time.sleep(TICK_DURATION)
        
        print(">> Refresh Loop has terminated...")