import cv2
import string
import random
 
# Randomly choose a letter from all the ascii_letters so i can name a file
randomLetter=''
for i in range(0,5):
    randomLetter += random.choice(string.ascii_letters)
    
#opening our system camera

cam=cv2.VideoCapture(0)

while True:
   
    success, frame = cam.read()
    # if statement to check if camera worked
    if not success:
        print('failed to grab frame')
        break
    
    frame=cv2.rotate(frame, cv2.ROTATE_180)
    frame=cv2.flip(frame,1)#uncomment this and the line above if output is upside down
    
    #to get continuous live video feed from my laptops webcam
    cv2.imshow('CHEESE!!', frame)
    
    
    k  = cv2.waitKey(1)
    # if the escape key is been pressed, the program terminates
    if k%256 == 27:
        print('closing the program')
        break
    
    # if ' l ' key is pressed
    # pictures will be taken
    elif k%256  == 108:
        # the name for storing the images taken
        img_name = f'{randomLetter}'
        cv2.imwrite(img_name+'.jpg', frame)
        print('picture taken')
        break 
    
cam.release()
cv2.destroyAllWindows()


img = cv2.imread(f'D:/coincent/ai/{img_name}.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Loading the haar-cascade xml classifier file for facial detection
haar_cascade = cv2.CascadeClassifier('D:/coincent/ai/haarcascade_frontalface_default.xml')
  
# Applying the face detection method on the grayscale image
faces = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
no=1
# Iterating through rectangles of detected faces

#Drawing rectangles of detected faces    
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img,str(no),(x,y+10),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA,False)
    no+=1

no-=1

print("The total no of faces detected : {0}".format(no))

cv2.imshow('Detected faces', img)
cv2.imwrite(img_name+'_detected.jpg', img)
cv2.waitKey(0)
if k%256 == 27:
    print('closing the program')
    
cam.release()
cv2.destroyAllWindows()


