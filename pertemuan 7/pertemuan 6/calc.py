from tkinter import *

def draw_flag():
    # warna utama bendera
    canvas.create_rectangle(0, 0, 200, 100, fill="red")
    
    # warna pengujian
    canvas.create_polygon(0, 0, 100, 0, 100, 100, fill="green")
    canvas.create_polygon(100, 0, 200, 0, 200, 100, fill="black")

# buat jendela
root = Tk()
root.title("Bendera Palestina")

# buat canvas
canvas = Canvas(root, width=200, height=100)
canvas.pack()

# buat tombol
button = Button(root, text="Tampilkan Bendera", command=draw_flag)
button.pack()

# mulai berjalan
root.mainloop()