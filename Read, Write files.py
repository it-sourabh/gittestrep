file = open("Security products.txt", "r")
for product in file.readlines():
    print(product)
file.close()

file1 = open("Security products1.txt", "a")
file1.write("Network:")
file1.write("\n1. Firewall")
file1.write("\n2. Network Intrusion-Detection System")
file1.close()
