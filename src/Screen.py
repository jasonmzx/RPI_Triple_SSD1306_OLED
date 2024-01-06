import threading
import time
from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont

class Screen(ABC):

    def __init__(self, display):
        
        self.display = display #* Actual Reference to I2C Screen Element 

        self.width = display.width
        self.height = display.height
        self.image = Image.new('1', (self.width, self.height))
        
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default(size=14)

    def show(self): 
        
        self.display.image(self.image)        
        self.display.show()

    @abstractmethod
    def drawImage(self):
        #This class method is defined by Classes implementing Screen
        pass