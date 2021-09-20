try:
    import cv2 #for image processing
    import sys
    import os
except Exception as e:
    print(e)
    
def cartoonify(ImagePath):
    #ImagePath=r"C:/Users/Dell/Desktop/Nitish Jain/Pic.jpeg"
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    if originalmage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    ReSized1 = cv2.resize(originalmage, (960, 540))
    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (960, 540))
    colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = cv2.resize(cartoonImage, (1000, 1500))
    print('1')
    cv2.imwrite('public/Cartoon.jpeg', ReSized6)
    print('2')
    # print('Resized6')
    # fig=plt.imshow(ReSized6)
    # print('1')
    # fig.set_cmap('hot')
    # print('2')
    # fig.axes.get_xaxis().set_visible(False)
    # print('3')
    # fig.axes.get_yaxis().set_visible(False)
    # print('4')
    # plt.savefig('public/Cartoon.jpeg')
    # print('5')

oldname = sys.argv[1]
newname = oldname+'.jpg'
os.rename(oldname,newname)
cartoonify(newname) 