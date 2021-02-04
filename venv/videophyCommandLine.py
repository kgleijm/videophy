
# import needed libraries
import sys
import os
import shutil
# install open-cv if not yet installed
os.system("pip install opencv-python")
from cv2 import cv2


print('Number of arguments: {}'.format(len(sys.argv)))

# read absolute path from arguments
dirPath = sys.argv[1]
title = sys.argv[2]
fpsInput = int(sys.argv[3])
print(dirPath)
sourcePathString = dirPath + "/source"

# reading in files from that path
path, dirs, files = next(os.walk(dirPath))
print(path, dirs, files)
clip_count = len(files)

# make sourceImagedirectory if not exists
try:
    os.mkdir(sourcePathString)
except:
    pass

# loop over all files in folder and store them as cv2 compatible images
img = []
for file in files:
    img.append(cv2.imread(dirPath + file))
    shutil.move(file, sourcePathString)

# declare open-cv variables
height, width, layers = img[1].shape
fourcc = cv2.VideoWriter_fourcc(*'I420')
video = cv2.VideoWriter(dirPath + 'video.avi', fourcc, fpsInput, (width, height))

# write all images to video
for j in range(clip_count):
    print("Writing img ", j)
    video.write(img[j])

# release video
cv2.destroyAllWindows()
video.release()

print("Released video to: " + dirPath)