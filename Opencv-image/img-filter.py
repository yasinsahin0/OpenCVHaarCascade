import cv2
import numpy as np
img = cv2.imread("img/elma.jpg")

def img_blur():
    kernel = np.ones((3,3),np.float32)/9
    blur = cv2.filter2D(img,-1,kernel)      # -1 orjinal resimle aynı derinlik
    #cv2.imshow("blur", blur)
    blurr = cv2.blur(img,(7,7))             # fonksiyon
    #cv2.imshow("blurr", blurr)
    gaus = cv2.GaussianBlur(img,(5,5),0)    # Gaus filtresi
    #cv2.imshow("gaus", gaus)
    bilateral = cv2.bilateralFilter(img,9,75,75)
    #cv2.imshow("bilateral",bilateral)
    median = cv2.medianBlur(img,11)
    #cv2.imshow("median",median)


def img_sharpen():
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
    sharped = cv2.filter2D(img,-1,kernel)
    return sharped

def img_edge_detect():
    canny = cv2.Canny(img,10,100)
    cv2.imshow("canny",canny)


cv2.imshow("orjinal",img_sharpen())
cv2.waitKey(0)
cv2.destroyAllWindows()