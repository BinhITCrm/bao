# print('bao dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')
# print('binh dep trai khoai to')

import cv2

cap = cv2.VideoCapture(0)
# cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    cv2.imshow('Camera',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
