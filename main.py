import sys
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
DARK_GREEN = "#557C55"
RED = "#FA7070"
LIGHT_GREEN = "#F2FFE9"
GREEN = "#A6CF98"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def end_clicked():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title = Label(text="TIMER", bg=LIGHT_GREEN, foreground=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
    title.grid(column=1, row=0)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global reps

    reps += 1

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps == 8:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        break_timer = Label(text="BREAK", bg=LIGHT_GREEN, foreground=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
        break_timer.grid(column=1, row=0)
    else:
        count_down(work_sec)
        title_02 = Label(text="START", bg=LIGHT_GREEN, foreground=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
        title_02.grid(column=1, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count) % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_min == 0 and 0 < count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "❤"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=5, pady=3, bg=LIGHT_GREEN)

canvas = Canvas(width=200, height=250, bg=LIGHT_GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

title = Label(text="TIMER", bg=LIGHT_GREEN, foreground=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start_clicked)
start_button.config(width=10, height=2)
start_button.grid(column=0, row=3)

end_button = Button(text="End", command=end_clicked)
end_button.config(width=10, height=2)
end_button.grid(column=2, row=3)

check_marks = Label(text="", bg=LIGHT_GREEN, foreground=DARK_GREEN, font=(FONT_NAME, 50, "bold"))
check_marks.grid(column=1, row=4)

window.mainloop()
