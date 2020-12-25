# This is inheritence in which we can import functions of other class to our class
from PC_Class import PC
class PC2(PC):

    def monitor_4k(self):
        print("This has a 4k monitor")

    def webcam(self):
        print("This PC has a webcam in hd quality")



