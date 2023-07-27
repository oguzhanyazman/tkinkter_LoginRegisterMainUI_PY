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
    188.5, 490.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 233, y = 542,
    width = 120,
    height = 60)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    195.5, 410.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#99a3ff",
    highlightthickness = 0)

entry0.place(
    x = 51.0, y = 390,
    width = 289.0,
    height = 38)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    195.5, 486.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#99a3ff",
    highlightthickness = 0)

entry1.place(
    x = 51.0, y = 466,
    width = 289.0,
    height = 38)

window.resizable(False, False)
window.mainloop()
