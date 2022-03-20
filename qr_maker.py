import qrcode
name=input("NAME OF STUDENT: ")
img = qrcode.make(name)
img.save(f'{name}.png')