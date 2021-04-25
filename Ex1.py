import cv2
import numpy as np
kamera= cv2.VideoCapture(0)

#kamera.set(cv2.CAP_PROP_FRAME_WIDTH,1024)    # genişlik değişme
#kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,500)    # yükseklik değişme
#kamera.set(cv2.CAP_PROP_FPS,200)             # FPS Değiştirme veya bilgi alma
#kamera.set(cv2.CAP_PROP_BRIGHTNESS,1)        # Parlaklık değiştirme veya alma

def Blur_f(img,fonk,matris):
    matris = int(matris)
    if fonk=="conv":
        kernel = np.ones((matris, matris), np.float32) / 25
        out_img = cv2.filter2D(img, -1, kernel)
    elif fonk =="blur":
        out_img = cv2.blur(img,(matris,matris))
    elif fonk == "gaus":
        out_img = cv2.GaussianBlur(img,(matris,matris),0)
    elif fonk =="median":
        out_img = cv2.medianBlur(img,matris)
    return out_img

kernel1 = np.array(([[1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1]]),np.float32) / 25

kernel2 = np.array(([[0,0,0,0,0,0],
                     [0,0,1,1,1,0],
                     [0,1,0,1,1,0],
                     [1,0,1,1,1,0],
                     [0,0,1,0,1,0],
                     [1,1,1,1,1,1]]),np.float32) / 25
kernel3 = np.eye(5,5)
while(1):
    ret, frame=kamera.read()
    #Blur_f(resim,fonksiyon türü,bulanıklaştırma gücü(matris büyüklüğü))
    #img = Blur_f(frame,"conv",3)
    img1 = cv2.filter2D(frame, -1, kernel1)
    img2 = cv2.filter2D(frame, -1, kernel3)
    cv2.imshow('kernel 1', img1)
    cv2.imshow('kernel 2', img2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



kamera.release()
cv2.destroyAllWindows()
