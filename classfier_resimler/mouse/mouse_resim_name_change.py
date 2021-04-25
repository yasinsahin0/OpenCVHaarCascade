import glob
import cv2
list1 = []
jpeg = glob.glob("*.jpeg")
png = glob.glob("*.png")
jpg = glob.glob("*.jpg")
for i in jpeg:
    list1.append(i)
for i in png:
    list1.append(i)
for i in jpg:
    list1.append(i)
say = 0
for yeni in list1:
    say = say+1
    resim = cv2.imread(yeni)
    scale_p = 60
    width = int(resim.shape[1]*scale_p/100)
    height = int(resim.shape[0]*scale_p/100)
    dim = (width,height)
    resized = cv2.resize(resim,dim,scale_p,interpolation=cv2.INTER_AREA)
    resized = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gri-resized/mouse_"+str(say)+".jpg",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()