import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the data from the entry widget
    data = entry.get()
    
    if not data:
        messagebox.showwarning("Input Error", "Please enter the URL!")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("GUIqr.png")

    # Display the QR code
    img = Image.open("GUIqr.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

# Set up the main application window
root = tk.Tk()
root.title("QR Code Generator")

# Create a frame for the input
frame = tk.Frame(root)
frame.pack(pady=20)

# Input label and entry
label = tk.Label(frame, text="Enter URL =>")
label.grid(row=0, column=0, padx=10)
entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1, padx=10)

# Generate button
button = tk.Button(root, text="Generate QR Code",fg="black",bg="pink", command=generate_qr, )
button.pack(pady=20)

# Label to display the QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
