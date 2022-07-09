'''Build a program take an input (which is an arbitrary color image), 
then, plot the histogram of the image. 
(To do so, you should investigate what is histogram of the image). 
Put the code and the result (figures) in the github.'''
from matplotlib import pyplot as plt
import cv2 as cv
import numpy 
import os 
def histmaker():
    print("Welcome to Histogram Maker!!")
    imagepath= input("Enter Image path: ")
    imagepath1=str(imagepath)   
    img= cv.imread(imagepath1, -1)
    color = ('b','g','r')
    for i,col in enumerate(color):     
        histogram1 = cv.calcHist([img],[i],None, [256],[0,256])
        plt.plot(histogram1,color = col)
        plt.xlim([0,256])
    plt.show()









histmaker()



