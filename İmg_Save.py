import cv2
import time
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

i=0
son = 40
kisi_id=input('ID numarası giriniz')
while True:
    i = i+1
    _, img =cam.read()
    #gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("img_Obj/obj-" + kisi_id + '.' + str(i) + ".jpg",img)
    cv2.imshow('resim', img)
    cv2.waitKey(20)
    time.sleep(1)
    if i>=(son-1):
        cam.release()
        cv2.destroyAllWindows()
        break

