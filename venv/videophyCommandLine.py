
# import needed libraries
import sys
import os
import shutil
# install open-cv if not yet installed
os.system("pip install opencv-python")
os.system("pip install natsort")
from cv2 import cv2
from natsort import natsorted, ns


print('Number of arguments: {}'.format(len(sys.argv)))

# read absolute path from arguments
dirPath = sys.argv[1]
title = sys.argv[2]
fpsInput = int(sys.argv[3])
print("Directory path = " + dirPath)
sourcePathString = dirPath + "\\source"
print("sourcePathString = " + sourcePathString)

# reading in files from that path
path, dirs, files = next(os.walk(dirPath))
clip_count = len(files)
# print(files, "\n\n\n\n")
# make sourceImagedirectory if not exists
try:
    print("Trying to make: ", sourcePathString)
    os.mkdir(sourcePathString)
except:
    pass

# loop over all files in folder and store them as cv2 compatible images


img = []

for file in natsorted(files):
    print("Trying to append: " + dirPath + "\\" + file)
    img.append(cv2.imread(dirPath + "\\" + file))

# declare open-cv variables
height, width, layers = img[1].shape
fourcc = cv2.VideoWriter_fourcc(*'I420')
video = cv2.VideoWriter(dirPath + "\\" +title + '.avi', fourcc, fpsInput, (width, height))



# write all images to video
for j in range(clip_count):
    print("Writing img ", j)
    video.write(img[j])

# release video
cv2.destroyAllWindows()
video.release()

# move files after processing
for file in files:
    if '.png' in file:
        shutil.move(dirPath + "\\" + file, sourcePathString  + "\\" +  file)

print("Released video to: " + dirPath + "\\" +title + '.avi')