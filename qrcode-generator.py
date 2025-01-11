import qrcode
data = input("Enter url to generate qrcode : ")
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=15,border=3)
qr.make(fit= True)
qr.add_data(data)
img = qr.make_image(fill_color= "black", back_color = "white")
img.save(input("Enter image name and type : "))
print(type(img))
