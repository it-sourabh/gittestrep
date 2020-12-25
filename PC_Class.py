class PC:


    def __init__(self, RAM, HDD, SSD, Graphic_Card, Processor, OS, Vendor):
        self.RAM = str(RAM) + " GB"
        self.HDD = str(HDD) + " GB"
        self.SSD = str(SSD) + " GB"
        self.Graphic_Card = str(Graphic_Card) + " GB"
        self.Processor = Processor
        self.OS = OS
        self.Vendor = Vendor


    def webcam(self):
        print("This PC has a webcam")