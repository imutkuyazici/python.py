import numpy as np
import cv2
i=[]
vid = cv2.VideoCapture(0)


while True :
    ret , frame = vid.read() #ret bir boolen degerdir boolen deger 
    

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    


    cv2.imshow('title',frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break 

vid.release()
cv2.destroyAllWindows()

"""if i in range:
    breakpoint 
"""
