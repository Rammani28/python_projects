from tkinter import *

# import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # 25
SHORT_BREAK_MIN = 5  # 5
LONG_BREAK_MIN = 20  # 20
CHECK = "✓"

marks = ""
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, check_label, marks
    marks = CHECK
    length = len(marks) + 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text=marks * length, fg=YELLOW, bg=YELLOW, font=(FONT_NAME, 24, 'normal'))
    marks = ""
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        minutes = SHORT_BREAK_MIN
        timer_label.config(text="Break", fg=PINK)
    else:
        minutes = WORK_MIN
        timer_label.config(text="Work", fg=GREEN)

    count_down(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, check_label, marks
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        if reps % 2 == 0:
            work_sessions = reps // 2
            for _ in range(work_sessions):
                marks += CHECK
            check_label = Label(text=marks, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
            check_label.grid(column=1, row=3)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# check_label = Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)

start_button = Button(text="Start", font=(FONT_NAME, 16, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 16, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
