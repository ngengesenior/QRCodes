import pyqrcode


def generate_qr():
    link_to_post = "https://medium.com/@ngengesenior/qr-codes-generation-with-python-377735be6c5f"
    url = pyqrcode.create(link_to_post)
    url.svg('url.png', scale=8)
    print("Printing QR code")
    print(url.terminal())


if __name__ == '__main__':
    generate_qr()
