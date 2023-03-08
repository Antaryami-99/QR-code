import qrcode

qr=qrcode.QRCode(version=1,border=4,box_size=10)



data="https://github.com/Antaryami-99"


qr.make(fit=True)
qr.add_data(data)

img=qr.make_image()
img.save("image.png")