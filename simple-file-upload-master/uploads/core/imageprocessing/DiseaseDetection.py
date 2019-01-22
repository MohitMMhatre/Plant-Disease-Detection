import cv2
import numpy as np

def detector(uploadedImage):
    
    leaf_cascade=cv2.CascadeClassifier('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master/uploads/core/imageprocessing/leaf-cascade.xml')
    funaglcascade=cv2.CascadeClassifier('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master/uploads/core/imageprocessing/fungalcascade.xml')
    ##img=cv2.imread('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master/uploads/core/imageprocessing/positive.jpg',1)
    img=cv2.imread('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master'+uploadedImage,1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
    leaf=leaf_cascade.detectMultiScale(gray,2,2)

    fungalleaf=funaglcascade.detectMultiScale(gray,2,2)

    i=0
    for(x,y,w,h) in fungalleaf:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),5)
        cv2.imshow('img',img)
        cv2.imwrite('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master'+uploadedImage,img)
        return 'plant has fungal disease';
        i=1
  
    for(x,y,w,h) in leaf:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),5)
        cv2.imshow('img',img)
        cv2.imwrite('C:/Users/mohit/Desktop/PlantDisease project/simple-file-upload-master'+uploadedImage,img)
        return 'plant has bacterial disease';
        i=1
     
    if i!=0:
        return 'plant has no disease';
            
    ##    k=cv2.waitKey(30) &0xFF
    ##    if k==27:
    ##        cv2.destroyAllWindows()
    ##        cap.release()
    ##        break
        
    ##for(x,y,w,h) in faces:
    ##    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)    
    ##    roi_gray=gray[y:y+h,x:x+w]
    ##    roi_color=img[y:y+h,x:x+w]
    ##    eyes=eye_cascade.detectMultiScale(roi_gray)
    ##    for(ex,ey,ew,eh) in eyes:
    ##        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)




            
