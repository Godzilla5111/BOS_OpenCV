import cv2

cap = cv2.VideoCapture('../gross_BOS/videos/stripe_dslr.MOV')

ret, img = cap.read()

background = img

count = 1
meanframe = cv2.absdiff(img, background)
while(ret):

    frame = cv2.absdiff(img, background)

    ret, frame = cv2.threshold(frame,20,255,cv2.THRESH_TOZERO)
    ret, frame = cv2.threshold(frame,60,255,cv2.THRESH_TOZERO_INV)
    frame = frame*4

    meanframe = cv2.addWeighted(meanframe, 1-1/count, frame, 1/count, 0)
    count = count+1
    frame = cv2.absdiff(frame,meanframe)

    # frame = cv2.blur(frame,(5,5))
    frame = cv2.GaussianBlur(frame, (5,5), 0)
    # frame = cv2.medianBlur(frame, 5)

    cv2.imshow('frame', frame)
    ret, img = cap.read()
    k = cv2.waitKey(33)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
