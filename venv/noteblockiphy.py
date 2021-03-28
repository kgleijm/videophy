
import sys
import os

os.system("pip install --upgrade Pillow")
from PIL import Image, ImageDraw

# read absolute path from arguments
# dirPath = sys.argv[1]

#initialize margins
noteWidth = 300
noteHeigth = 500
ruleSpace = 100
sideMarging = 75


# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)


out = Image.new("RGB", (noteWidth, noteHeigth), (255, 255, 255))

d = ImageDraw.Draw(out)
d.line((ruleSpace, 0, ruleSpace, noteHeigth), fill=255)

out.show()

