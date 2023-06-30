from tkinter import *

CALC_WIDTH = 500
CALC_HEIGHT = 100
BUTTON_WIDTH = 7
BUTTON_HEIGHT = 2
BACKGROUND_COLOR = "#505C68"

exp = ""


def btn_click(item):
    global exp
    exp = exp + str(item)
    equation.set(exp)


def equal():
    global exp
    result = str(eval(exp))
    equation.set(result)
    exp = ""


def clear_all():
    global exp
    exp = ""
    equation.set("")


def clear():
    global exp
    exp = ""
    equation.set("")


if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")
    window.resizable(False, False)

    equation = StringVar()

    input_field = Entry(window, textvariable=equation, width=23, font=("consoles", 30), bg=BACKGROUND_COLOR)
    input_field.grid(row=0, column=0, columnspan=4)

    clr_all_button = Button(window, text=" CE ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                            font=("consoles", 20),
                            relief='flat', command=clear_all)
    clr_all_button.grid(row=1, column=0)

    clr_button = Button(window, text=" C ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=clear)
    clr_button.grid(row=1, column=1)

    del_button = Button(window, text=" DEL ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,  # edit
                        font=("consoles", 20),
                        relief='flat', command=())
    del_button.grid(row=1, column=2)

    div_button = Button(window, text=" ÷ ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("/"))
    div_button.grid(row=1, column=3)

    add_button = Button(window, text=" + ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("+"))
    add_button.grid(row=4, column=3)

    sub_button = Button(window, text=" - ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("-"))
    sub_button.grid(row=3, column=3)

    mul_button = Button(window, text=" x ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("*"))
    mul_button.grid(row=2, column=3)

    eql_button = Button(window, text=" = ", height=BUTTON_HEIGHT, width=14, bg=BACKGROUND_COLOR, font=("consoles", 20),
                        # edit
                        relief='flat', command=equal)
    eql_button.grid(row=5, column=2, columnspan=2)

    one_button = Button(window, text=" 1 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("1"))
    one_button.grid(row=4, column=0)

    two_button = Button(window, text=" 2 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("2"))
    two_button.grid(row=4, column=1)

    three_button = Button(window, text=" 3 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                          font=("consoles", 20),
                          relief='flat', command=lambda: btn_click("3"))
    three_button.grid(row=4, column=2)

    four_button = Button(window, text=" 4 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                         font=("consoles", 20),
                         relief='flat', command=lambda: btn_click("4"))
    four_button.grid(row=3, column=0)

    five_button = Button(window, text=" 5 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                         font=("consoles", 20),
                         relief='flat', command=lambda: btn_click("5"))
    five_button.grid(row=3, column=1)

    six_button = Button(window, text=" 6 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("6"))
    six_button.grid(row=3, column=2)

    seven_button = Button(window, text=" 7 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                          font=("consoles", 20),
                          relief='flat', command=lambda: btn_click("7"))
    seven_button.grid(row=2, column=0)

    eight_button = Button(window, text=" 8 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                          font=("consoles", 20),
                          relief='flat', command=lambda: btn_click("8"))
    eight_button.grid(row=2, column=1)

    nine_button = Button(window, text=" 9 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                         font=("consoles", 20),
                         relief='flat', command=lambda: btn_click("9"))
    nine_button.grid(row=2, column=2)

    zero_button = Button(window, text=" 0 ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                         font=("consoles", 20),
                         relief='flat', command=lambda: btn_click("0"))
    zero_button.grid(row=5, column=1)

    dot_button = Button(window, text=" . ", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg=BACKGROUND_COLOR,
                        font=("consoles", 20),
                        relief='flat', command=lambda: btn_click("."))
    dot_button.grid(row=5, column=0)

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.mainloop()
