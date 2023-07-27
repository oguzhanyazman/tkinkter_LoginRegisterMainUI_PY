from tkinter import *


def btn_clicked():
    print("Button Clicked")

#ekranın tam ortasında başlatmak için
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

window = Tk()

window.geometry("411x731")
window.configure(bg = "#ffffff")
window_width = 411
window_height = 731
center_window(window, window_width, window_height)
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 731,
    width = 411,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    110.0, 368.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 88, y = 652,
    width = 140,
    height = 60)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 244, y = 652,
    width = 140,
    height = 60)

window.resizable(False, False)
window.mainloop()
