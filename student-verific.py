import numpy as np
import qrcode
import cv2
from pyzbar.pyzbar import decode
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

myfile = open('attendence.csv', 'a+')
students = [] # TYPE OUT YOUR OWN NAMES HERE LIKE SO: ['name1', 'name2']
names = []
print(len(students))
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, frame = cap.read()
    
    for barcode in decode(frame):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        
        print(myData)
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
                myfile.write(f'{students[a]},Absent\n')
            elif string in names:
                myfile.write(f'{students[a]},Present\n')
            a += 1
        break