from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    752.0, -653.0,
    text = "Air Nest",
    fill = "#ffffff",
    font = ("Inter-Bold", int(36.0)))

window.resizable(False, False)
window.mainloop()
