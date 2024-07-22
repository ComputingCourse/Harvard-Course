from pyfiglet import Figlet
import pyfiglet
import sys, random

if len(sys.argv) == 3:
    ran = False
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    ran = True
else:
    sys.exit("Invalid usage")


if not ran:
    font =sys.argv[2]
else:
    font =random.choice(pyfiglet.FigletFont.getFonts())

f = Figlet(font=font)
text = input("Input: ")
print("Output: ")
print(f.renderText(text))