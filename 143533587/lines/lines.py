import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("File does not exist")

file_lines = []
try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.replace(" ","")
            if line.rstrip() == "":
                pass
            elif line[0] == "#":
                pass
            else:
                file_lines.append(line)

    print(len(file_lines))

except FileNotFoundError:
    sys.exit("File does not exist")