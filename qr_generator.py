import qrcode


data = "https://www.linkedin.com/in/akhiliny-vijeyagumar1208/"


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4  
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated successfully! Check the 'qrcode.png' file.")
