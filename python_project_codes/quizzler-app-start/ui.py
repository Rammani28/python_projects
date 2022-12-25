from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_img, highlightthickness=0, command=self.right_click)
        self.right_button.grid(column=1, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_img, highlightthickness=0, command=self.wrong_click)
        self.wrong_button.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.right_button.config(command=self.right_click)
        self.wrong_button.config(command=self.wrong_click)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled", )

    def right_click(self):
        self.right_button.config(command=self.do_nothing)
        self.wrong_button.config(command=self.do_nothing)
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_click(self):
        self.right_button.config(command=self.do_nothing)
        self.wrong_button.config(command=self.do_nothing)
        self.give_feedback(self.quiz.check_answer("False")
)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def do_nothing(self):
        pass
