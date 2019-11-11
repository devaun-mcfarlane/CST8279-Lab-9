import csv

filename = input("Enter the file name: ")
with open (filename, 'r') as f:
    reader = csv.reader(f)
    pylist = list(reader)

print(pylist)
