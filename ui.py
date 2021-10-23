THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizzInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text \
                (
                150, 125,
                width=280,
                text="text",
                font=("Arial", 20, "italic"),
                fill=THEME_COLOR
            )
        # Buttons
        # correct button
        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz :)")
            self.correct_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
