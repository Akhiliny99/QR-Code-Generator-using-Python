import qrcode


data = "https://example.com"


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=20, 
    border=4  
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill="darkblue", back_color="lightblue")
img.save("QR_COLOR.png")

print("QR Code generated successfully!")
