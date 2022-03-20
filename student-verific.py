import numpy as np
import cv2
from pyzbar.pyzbar import decode

# variables blah blah

myfile = open('attendence.csv', 'a+')
students = [] # TYPE OUT YOUR OWN NAMES HERE LIKE SO: ['name1', 'name2']
names = [] # dont mind this it will fill up by its own

# vid capture

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# main stuff

while True:
    ret, frame = cap.read()
    
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8') # decode barcode seen in captured video
        print(myData)

        # outputting a quadrilateral around the qrcode (just for show, doesnt do alot)

        pts = np.array([barcode.polygon], np.int32)
        cv2.polylines(frame,[pts],True,(255,0,0),5)
        pts2 = barcode.rect
        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

        string = f'{myData},Present\n'
        if string not in names:
            names.append(string) 
    
    cv2.imshow('cam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        a = 0
        print(names)
        for i in range(len(students)):
            string = f'{students[a]},Present\n'
            if  string not in names:
                myfile.write(f'{students[a]},Absent\n') # if student name not in present name list, then absent
            elif string in names:
                myfile.write(f'{students[a]},Present\n') # if student name in present name list, then present
            a += 1
        break
