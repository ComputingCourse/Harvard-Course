import sys

#testing
if len(sys.argv) <3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

new_file = []
for line in file:
    line = line.replace('"', "")
    line = line.replace(' ', "")
    row = line.rstrip().split(",")
    new_file.append(row)
file.close()
new_file[0] = ["last", "first", "house"]

with open(sys.argv[2],"w") as file:
    file.write("")

with open(sys.argv[2],"a") as file:
    for row in new_file:
        file.write(f"{row[1]},{row[0]},{row[2]}")
        file.write("\n")
