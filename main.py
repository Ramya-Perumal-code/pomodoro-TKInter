import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0 or count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(0, math.floor(reps / 2)):
            mark += "✅ "
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=("Times New Romen", 35, "normal"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(fg="green")
tick_label.grid(row=3, column=1)

window.mainloop()
