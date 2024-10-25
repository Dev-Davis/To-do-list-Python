# # print the 3rd serial number from the list
#
# serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
# print(serials[2])

# for loop
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    newName = filename.replace(".", "-", 1)

    print(newName)
