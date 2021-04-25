import cv2
import numpy as np

mario = cv2.imread("img/mario.png")
mario_gray = cv2.cvtColor(mario,cv2.COLOR_BGR2GRAY)

coin = cv2.imread("img/coin1.png")
coin_gray = cv2.cvtColor(coin,cv2.COLOR_BGR2GRAY)
print(cv2.imshow("gray",mario_gray))
cv2.waitKey(0)
cv2.destroyAllWindows()