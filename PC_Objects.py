from PC import PC2
from PC_Class import PC
PC1 = PC2(12, 1000, 256, None, "Intel i3 7th Gen", "Windows", "Lenovo")
PC2 = PC(8, 1000, None, 2, "Intel i5 8th Gen", "Windows", "DELL")


print(PC1.Processor)

print(PC2.Vendor)

print(PC1.SSD)
try:
    PC.webcam(PC2)
except TypeError as Error:
    print(Error)

PC2.webcam()