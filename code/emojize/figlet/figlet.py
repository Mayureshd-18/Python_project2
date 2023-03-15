from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv)==3:
        if (sys.argv[1]== "-f" or sys.argv[1] == "--font"):
                if sys.argv[2] in fonts:
                        f = sys.argv[2]
                elif sys.argv[2] not in fonts:
                        sys.exit("Invalid usage")
        else:
                sys.exit("Invalid usage")
elif len(sys.argv)==2:
        sys.exit("Invalid usage")
else:
        f = random.choice(fonts)
s = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(s))