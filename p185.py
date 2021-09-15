import cv2
try:
    img=cv2.imread('girl01.jpg')
    if img is None:
        raise ValueError('ファイルが見つかりません。')
    img_height=int(img.shape[1]/2)#画像の縦1/2
    img_weidth=int(img.shape[1]/2)#画像の横1/2
    cv2.circle(img,(img_weidth,img_height),200,(0,200,255),3)
    cv2.rectangle(img,(img_weidth-50,img_height-50),(img_weidth+50,img_height+50),(0,0,200),3,4)
    cv2.imshow('Photo+Circle+Rectangle Center',img)
    cv2.waitKey(0)
    cv2.estroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()