
# import needed libraries
import sys.argv
import os
from cv2 import cv2

# generate absolute path
dirPath = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "/testImages/"
print(dirPath)
pathString = "./testImages/"

# reading in files from that path
path, dirs, files = next(os.walk(pathString))
print(path, dirs, files)
clip_count = len(files)

# make directory if not exists
try:
    os.mkdir(dirPath + 'output')
except:
    pass


# loop over all files in folder and store them as cv2 compatible images
img = []
for file in files:
    # print(dirPath + file)
    img.append(cv2.imread(dirPath + file))

# declare open-cv variables
height, width, layers = img[1].shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(dirPath + 'output/video.mp4', fourcc, 1, (width, height))

# write all images to video
for j in range(clip_count):
    print("Writing img ", j)
    video.write(img[j])

# release video
cv2.destroyAllWindows()
video.release()

print("Released video to: " + dirPath + 'output/video.mp4')