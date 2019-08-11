import numpy as np
import cv2
import datetime
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 800,800)
refreshInterval = 2;
startTime = int(datetime.datetime.now().strftime ("%Y%m%d%H%M%S"))
limit = 2000
flag = True
ret, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
startCount = int(datetime.datetime.now().strftime ("%Y%m%d%H%M%S"))
while(int(datetime.datetime.now().strftime ("%Y%m%d%H%M%S")) - startCount < 10):
    try:
        cv2.imwrite('f1.png',frame)
        print(len(cv2.findNonZero(cv2.inRange(hsv[10:280, 10:370], (45, 100, 50), (75, 255,255)))))
        if(len(cv2.findNonZero(cv2.inRange(hsv[10:280, 10:370], (45, 100, 50), (75, 255,255)))) > limit/2):
            print("not a good background green noise is high")
            flag = False
    except:
        pass
lastValue = -1
while(flag):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = frame
    
    # Display the resulting frame
    cv2.rectangle(image, (10, 10), (100, 100), (255,0,0), 2)
    cv2.rectangle(image, (100, 10), (190, 100), (255,0,0), 2)
    cv2.rectangle(image, (190, 10), (280, 100), (255,0,0), 2)
    cv2.rectangle(image, (10, 100), (100, 190), (255,0,0), 2)
    cv2.rectangle(image, (100, 100), (190, 190), (255,0,0), 2)
    cv2.rectangle(image, (190, 100), (280, 190), (255,0,0), 2)
    cv2.rectangle(image, (10, 190), (100, 280), (255,0,0), 2)
    cv2.rectangle(image, (100, 190), (190, 280), (255,0,0), 2)
    cv2.rectangle(image, (190, 190), (280, 280), (255,0,0), 2)
    cv2.rectangle(image, (100, 280), (190, 370), (255,0,0), 2)
    img = frame
    cv2.putText(frame, "1" ,(50,65), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "2" ,(140,65), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "3" ,(230,65), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "4" ,(50,155), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "5" ,(140,155), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "6" ,(230,155), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "7" ,(50,245), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "8" ,(140,245), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "9" ,(230,245), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame, "0" ,(140,335), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    ## mask of green (36,0,0) ~ (70, 255,255)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,0,0) ~ (70, 255,255)
    mask9 = cv2.inRange(hsv[190:280, 190:280], (45, 100, 50), (75, 255,255)) 
    mask6 = cv2.inRange(hsv[100:190, 190:280], (45, 100, 50), (75, 255,255)) 
    mask3 = cv2.inRange(hsv[10:100, 190:280], (45, 100, 50), (75, 255,255)) 
    mask8 = cv2.inRange(hsv[190:280, 100:190], (45, 100, 50), (75, 255,255)) 
    mask5 = cv2.inRange(hsv[100:190, 100:190], (45, 100, 50), (75, 255,255)) 
    mask2 = cv2.inRange(hsv[10:100, 100:190], (45, 100, 50), (75, 255,255)) 
    mask7 = cv2.inRange(hsv[190:280, 10:100], (45, 100, 50), (75, 255,255)) 
    mask4 = cv2.inRange(hsv[100:190, 10:100], (45, 100, 50), (75, 255,255)) 
    mask1 = cv2.inRange(hsv[10:100, 10:100], (45, 100, 50), (75, 255,255)) 
    mask0 = cv2.inRange(hsv[280:370, 100:190], (45, 100, 50), (75, 255,255))
    mask11 = cv2.inRange(hsv, (45, 100, 50), (75, 255,255))
    #get all non zero values
    target = cv2.bitwise_and(img[100:190, 280:370],img[100:190, 280:370], mask=mask0)
    #target = cv2.bitwise_and(img,img, mask=mask11)
    value = -1
    max = 0

    if(int(datetime.datetime.now().strftime ("%Y%m%d%H%M%S")) - startTime > refreshInterval):
        val0 = 0
        val1 = 0
        val2 = 0
        val3 = 0
        val4 = 0
        val5 = 0
        val6 = 0
        val7 = 0
        val8 = 0
        val9 = 0

        try:
            val0 = len(cv2.findNonZero(mask0))
        except:
            pass
        try:
            val9 = len(cv2.findNonZero(mask9))
        except:
            pass
        try:
            val8 = len(cv2.findNonZero(mask8))
        except:
            pass
        try:
            val7 = len(cv2.findNonZero(mask7))
        except:
            pass
        try:
            val6 = len(cv2.findNonZero(mask6))
        except:
            pass
        try:
            val5 = len(cv2.findNonZero(mask5))
        except:
            pass
        try:
            val4 = len(cv2.findNonZero(mask4))
        except:
            pass
        try:
            val3 = len(cv2.findNonZero(mask3))
        except:
            pass
        try:
            val2 = len(cv2.findNonZero(mask2))
        except:
            pass
        try:
            val1 = len(cv2.findNonZero(mask1))
        except:
            pass
        print(val0, ' ',val1, ' ',val2, ' ',val3, ' ',val4, ' ',val5, ' ',val6, ' ',val7, ' ',val8, ' ',val9, ' ',)

        startTime = int(datetime.datetime.now().strftime ("%Y%m%d%H%M%S"))
        if(val9>limit):
            if(val9>max):
                value = 9
                max = val9
        if(val8>limit):
            if(val8>max):
                value = 8
                max = val8
        if(val7>limit):
            if(val7>max):
                value = 7
                max = val7
        if(val6>limit):
            if(val6>max):
                value = 6
                max = val6
        if(val5>limit):
            if(val5>max):
                value = 5
                max = val5
        if(val4>limit):
            if(val4>max):
                value = 4
                max = val4
        if(val3>limit):
            if(val3>max):
                value = 3
                max = val3
        if(val2>limit):
            if(val2>max):
                value = 2
                max = val2
        if(val1>limit):
            if(val1>max):
                value = 1
                max = val1
        if(val0>limit):
            if(val0>max):
                value = 0
                max = val0

   
    if(value != -1):
        lastValue = value
        print('value is ',value)
    if(lastValue!=-1):
        cv2.putText(frame, str(lastValue) ,(400,335), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame[10:280, 10:370])
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('c1.png',frame)
        cv2.destroyAllWindows()
        break
    #if (cv2.waitKey(1) & 0xFF == ord('q')):# or True:
     #   break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
