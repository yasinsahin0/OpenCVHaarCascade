import cv2
import numpy as np
from matplotlib import  pyplot as plt
img_path = 'img/mario.png'

def img_resize(scale):
    img_r = cv2.imread(img_path)
    scale_p = int(scale)
    width = int(img_r.shape[1] * scale_p / 100)
    height = int(img_r.shape[0]*scale_p/100)
    dim = (width,height)
    resized = cv2.resize(img_r,dim,scale_p,interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized",resized)

def img_color(color_code):
    img_c = cv2.imread(img_path)
    if(color_code=='gray'):  #gri
        img_c = cv2.cvtColor(img_c,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gri Tonlama",img_c)
    elif(color_code=='rgb'):
        img_c = cv2.cvtColor(img_c,cv2.COLOR_BGR2RGB)
        cv2.imshow("RGB Tonlama",img_c)
    else:
        print("Renk tonu hatası")

def img_corner():
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,40,0.05,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),5,255,-1)
    cv2.imshow("Köse Noktalar",img)

def img_threshold():
    img = cv2.imread(img_path, 0)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()




def CFMGetFM(self, R, G, B):
    # max(R,G,B)
    tmp1 = cv2.max(R, G)
    RGBMax = cv2.max(B, tmp1)
    RGBMax[RGBMax <= 0] = 0.0001  # prevent dividing by 0
    # min(R,G)
    RGMin = cv2.min(R, G)
    # RG = (R-G)/max(R,G,B)
    RG = (R - G) / RGBMax
    # BY = (B-min(R,G)/max(R,G,B)
    BY = (B - RGMin) / RGBMax
    # clamp nagative values to 0
    RG[RG < 0] = 0
    BY[BY < 0] = 0
    # obtain feature maps in the same way as intensity
    RGFM = self.FMGaussianPyrCSD(RG)
    BYFM = self.FMGaussianPyrCSD(BY)
    # return
    return RGFM, BYFM


# orientation feature maps

#ROI = resim[200:300,150:300]                    # Resmin belirli bölgesini alır

#img_threshold()
#img_corner()
#img_resize(img_path,80)
#img_color(img_path,'rgb')

cv2.waitKey(0)
cv2.destroyAllWindows()

