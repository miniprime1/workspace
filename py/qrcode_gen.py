import qrcode
print("QR Code Generator v1.0")
print("Copyright (c) 2020 miniprime1")
input_data = input("\nEnter Text: ")
print("\n", end='')
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
print("Result: 'qrcode.png'")