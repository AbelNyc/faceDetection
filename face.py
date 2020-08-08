import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

images = cv2.imread("news.jpg")

gray_pic = cv2.cvtColor(images,cv2.COLOR_BGR2GRAY) # turn into grayscale 

resizeddd = cv2.resize(gray_pic,(int(gray_pic.shape[1]),int(gray_pic.shape[0])))

facess = face_cascade.detectMultiScale(resizeddd,scaleFactor=1.05,minNeighbors=5)
#the letters stands for the values in the numpy array [[267 174 408 408]]
for a,b,c,d in facess:
    resizeddd  = cv2.rectangle(resizeddd,(a,b),(a+c,b+d),(0,255,0),3)
print(facess)
cv2.imshow("Gray",resizeddd)
cv2.waitKey(25000)
cv2.destroyAllWindows()