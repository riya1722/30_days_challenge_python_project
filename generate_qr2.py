import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=2,border=4,)
qr.add_data("https://www.linkedin.com/in/riya-dwivedi-70a3712bb/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("riya_qr.png")