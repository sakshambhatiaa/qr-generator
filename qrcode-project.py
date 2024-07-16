import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 8,
    border = 5
)

data = "https://www.google.com/"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_colour="red")
img.save("myQRred.png")

