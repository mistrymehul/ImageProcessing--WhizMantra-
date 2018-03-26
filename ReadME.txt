This repository contains 2 python codes.

1)temp.py 
Here we have used template matching algorithm to find tick marks on the paper.
This method is effective but has some issues detecting tick marks on text. The image results.jpg has the demo image with the detected tick marks from paper.img
We can use template matching several times to detect different shapes of tick marks.


2)image_diff.py
This file contains the code for image difference algorithm. The file test1.jpg contains the blank answer sheet and test2.jpg contains the filled answer sheet.
This algorithm finds the difference between these 2 images and writes a new image file diff.jpg. 
We can find the option number by sensing the change in pixel intensity over the image.