import sys
from tabulate import tabulate

#testing validity
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")
try:
    file = open(sys.argv[1], "r")
    print("P")
except FileNotFoundError:
    sys.exit("File does not exist")

table = []
print("I")
with open(sys.argv[1]) as file:
    for line in file:
        row = line.rstrip().split(",")
        table.append(row)
        print(line)




print(tabulate(table[1:], headers = table[0],tablefmt="grid"))
file.close()