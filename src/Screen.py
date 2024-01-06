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
        self._THREAD  = threading.Thread(target=self._refresh_loop, daemon=True) 


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

    def _DESTROY_THREAD(self):
        self._DESTROY.set()
        self._THREAD.join()

    def _refresh_loop(self):
        while not self._DESTROY.is_set():
            self.drawImage()
            time.sleep(self.refresh_rate)
    
    def __del__(self):
        print("DESTROYING THREAD...")
        self._DESTROY_THREAD()
        self.clear_screen()