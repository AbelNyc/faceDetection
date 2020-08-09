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