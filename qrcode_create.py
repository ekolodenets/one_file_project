# pip install qrcode Image
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black', back_color='white')
    img.save('qrimage.png')

url = 'Checking the Message!'
generate_qrcode(url)