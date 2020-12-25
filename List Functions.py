list2 = [0, 54, 35, 75, 78, 34, 47]
list1 = ["Aanda", "Ravi", "Karan", "Shamsher", "Ved", "Kevin", "Mayank"]
print(list1[0:4])
list1[3] = "Ram"
print(list1)
list1.extend(list2)
print(list1)
guns = ["AKM", "UMP", "AWM", "P90", "Bizon", "M416", "M762"]
guns.append("Pistol")
print(guns)
guns.insert(3, "SCAR-L")
print(guns)
guns.remove("Pistol")
print(guns)
list2.clear()
print(list2)
# pop() pops out the last element in the list
guns.pop()
print(guns)
print(guns.index("UMP"))
guns.append("P90")
print(guns.count("P90"))
guns.sort()
print(guns)
list3 = [45, 26, 35, 74, 35, 78, 37, 83, 26]
list3.sort()
print(list3)
guns.reverse()
print(guns)
guns2 = guns.copy()
print(guns2)







