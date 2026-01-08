import qrcode

def generate_qrcode(data, filename="qrcode.png"):
    """
    Generate a QR code from the given data and save it as an image.
    
    Args:
        data (str): The data to encode in the QR code
        filename (str): The output filename (default: qrcode.png)
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    # Example usage
    user_data = input("Enter data to encode: ")
    generate_qrcode(user_data)