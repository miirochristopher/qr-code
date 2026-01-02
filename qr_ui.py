import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

qr_image = None  

def generate_qr():
    global qr_image

    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    preview = qr_image.resize((220, 220))
    photo = ImageTk.PhotoImage(preview)

    qr_label.config(image=photo)
    qr_label.image = photo  

def save_qr():
    if qr_image is None:
        messagebox.showerror("Error", "Generate a QR code first")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")]
    )

    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")

root = tk.Tk()
root.title("Google Docs QR Generator")
root.geometry("420x420")
root.resizable(False, False)

tk.Label(root, text="Google Docs URL", font=("Arial", 12)).pack(pady=10)

url_entry = tk.Entry(root, width=55)
url_entry.pack(pady=5)
url_entry.insert(0, "")

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

tk.Button(root, text="Save QR Code", command=save_qr).pack(pady=10)

root.mainloop()
