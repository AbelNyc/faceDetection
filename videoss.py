<<<<<<< HEAD
import cv2 ,time , pandas as pd
from datetime import datetime

first_pic= None #save inital frame of the video
#a=0
video = cv2.VideoCapture(0)
movement_list = [None,None] #track movement changes,,if object is showing in the webcam
time = [] #tracked time when object appears

df = pd.DataFrame(columns=["Start","End"])
while True:
    #a+=1
    
    check, frame = video.read()
    movement = 0 #when no object is showing
    grayy = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grayy = cv2.GaussianBlur(grayy,(21,21),0) #parameters for bluriness
    if first_pic is None:
        first_pic = grayy #after capturing the first frame go to the second loop
        continue
    
    
    
    cur_frame = cv2.absdiff(first_pic,grayy)
    threshold_binary = cv2.threshold(cur_frame,30,255,cv2.THRESH_BINARY)[1] #only need to access the second item of the tuple
    threshold_binary =cv2.dilate(threshold_binary,None,iterations=2)
    #find the countors 
    (cnts,_) = cv2.findContours(threshold_binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        if cv2.contourArea(cnt) < 5000:
            continue
        movement=1 #when an area > 5000 appears on screen set movement to 1 and track the time
        #rectangle
        (x,y,w,h) =cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    #time.sleep(3)
    movement_list.append(movement)
    if movement_list[-1]==0 and movement_list[-2]==1:
        time.append(datetime.now())
    if movement_list[-1]==1 and movement_list[-2]==0:
        time.append(datetime.now())
    cv2.imshow("Stoking",grayy)
    cv2.imshow("Current Frame",cur_frame)
    cv2.imshow("threshold Frame",threshold_binary)
    cv2.imshow("Reactangle",frame)
    
    if cv2.waitKey(1)==ord('s'): #s to quit
        if movement==1:
            times(append(datetime.now())) #trakc exit time 
        break
print(movement_list)
print(time)

for i in range(0,len(time),2):
    df = df.append({"Start":time[i],"End":time[i+1]},ignore_index=True)

df.to_csv("RecordedTime.csv")
video.release()
cv2.destroyAllWindows()
=======
import cv2 ,time

first_frame = None #save inital frame of the video
#a=0
video = cv2.VideoCapture(0)
while True:
    #a+=1
    check, frame = video.read()
    
    grayy = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grayy = cv2.GaussianBlur(grayy,(21,21),0) #parameters for bluriness
    if first_frame is None:
        first_frame = grayy #after capturing the first frame go to the second loop
        continue
    
    
    cur_frame = cv2.absdiff(first_frame,grayy)
    threshold_binary = cv2.threshold(cur_frame,30,255,cv2.THRESH_BINARY)[1] #only need to access the second item of the tuple
    threshold_binary =cv2.dilate(threshold_binary,None,iterations=2)
    #find the countors 
    (cnts,_) = cv2.findContours(threshold_binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        if cv2.contourArea(cnt) < 1000:
            continue
        #rectangle
        (x,y,w,h) =cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    #time.sleep(3)
    cv2.imshow("Stoking",grayy)
    cv2.imshow("Current Frame",cur_frame)
    cv2.imshow("threshold Frame",threshold_binary)
    cv2.imshow("Reactangle",frame)
    if cv2.waitKey(1)==ord('s'): #s to quit
        break
video.release()
cv2.destroyAllWindows()
>>>>>>> af3af7a0cfb8d5b602f1b3e403dd184937768006
