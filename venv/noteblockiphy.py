
import sys
import os

os.system("pip install --upgrade Pillow")
from PIL import Image, ImageDraw

# read absolute path from arguments
# dirPath = sys.argv[1]

#initialize margins
noteWidth = 500
noteHeigth = 700
ruleSpace = 20
sideMarging = 50


# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)

# initialize image
out = Image.new("RGBA", (noteWidth, noteHeigth), (255, 255, 255, 255))
d = ImageDraw.Draw(out)

# draw lines
for i in range(1, (noteHeigth//ruleSpace)):
    d.line((0, i*ruleSpace, noteWidth, i*ruleSpace), fill=255)


# draw margin line
d.line((sideMarging, 0, sideMarging, noteHeigth), fill=(255, 0, 0, 255))

out.show()

