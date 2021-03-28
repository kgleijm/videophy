
import sys
import os

os.system("pip install --upgrade Pillow")
from PIL import Image, ImageDraw, ImageFont

# read absolute path from arguments
# dirPath = sys.argv[1]

# count lines
lines = 0
maxWidth = 0
with open("C:\\Users\\kevin\\PycharmProjects\\videophy\\venv\\textContainer.txt", "r") as a_file:
    for line in a_file:
        lines += 1
        maxWidth = max(maxWidth, len(line))


#initialize margins
noteWidth = 60 + maxWidth*11
ruleSpace = 20
noteHeigth = (lines + 2)*ruleSpace
sideMarging = 50




# initialize image
out = Image.new("RGBA", (noteWidth, noteHeigth), (255, 255, 255, 255))
d = ImageDraw.Draw(out)
fnt = ImageFont.truetype(r"C:\Users\kevin\PycharmProjects\videophy\venv\testImages\fonts\PinkChicken-Regular.otf", 25)



# draw lines
for i in range(1, (noteHeigth//ruleSpace)):
    d.line((0, i*ruleSpace, noteWidth, i*ruleSpace), fill=255)

# read and draw text from textcontainer
index = 1
with open("C:\\Users\\kevin\\PycharmProjects\\videophy\\venv\\textContainer.txt", "r") as a_file:
  for line in a_file:
    #line = line.strip()
    print(line)
    d.text((sideMarging +10, (index*ruleSpace)-4), line, font=fnt, fill=(0, 0, 0, 255))

    index += 1


# draw margin line
d.line((sideMarging, 0, sideMarging, noteHeigth), fill=(255, 0, 0, 255))

out.show()

