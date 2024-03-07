import tkinter as tk
from PIL import Image, ImageTk

def button_clicked(button_name):
    print(f"{button_name} by clicking the button")

root = tk.Tk()
root.title("unique buttons")

image1 = Image.open("test.webp")
image2 = Image.open("test.webp")

image1 = image1.resize((100, 50), Image.LANCZOS)
image2 = image2.resize((100, 50), Image.LANCZOS)

photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)

button1 = tk.Button(root, image=photo1, command=lambda: button_clicked("Button 1"))
button1.pack()

button2 = tk.Button(root, image=photo2, command=lambda: button_clicked("Button 2"))
button2.pack()

root.mainloop()
