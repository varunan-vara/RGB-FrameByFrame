# Ran script: pip3 install opencv-python

import cv2
import math
import csv

# Some code taken from: https://answers.opencv.org/question/62029/extract-a-frame-every-second-in-python/
# Change following as needed
vidSource = "Trial1.mp4"
imageFolder = "./Trial1Images"
coords = [617, 923] # Doesn't do anything, see Line 40
print("Established Variables")

vid = cv2.VideoCapture(vidSource)
filenameList = []
counter = 0
framerate = vid.get(5)
while(vid.isOpened()):
	print("Working....")
	frameID = vid.get(5)
	ret, frame = vid.read()
	if (ret != True):
		print("Ending Process")
		break
	if (frameID % math.floor(framerate) == 0):
		print("Saving....")
		fileName = "{}/image {}s.jpg".format(imageFolder, counter)
		filenameList.append(fileName)
		counter += 1
		cv2.imwrite(fileName, frame)
		print("Saved!")
vid.release()
print("Done Saving Images!")

with open("results.csv", "w", newline="") as results:
	export = csv.writer(results).writerow
	export(["Time (s)","R", "G", "B"])
	scounter = 0
	for image in filenameList:
		s = cv2.imread(image)
		colour = s[643, 920] # Change coordinates as needed
		export([scounter,colour[2],colour[1],colour[0]])
		scounter += 5
		print("Working....")
	print("Done writing results to results.csv")