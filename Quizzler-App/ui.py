from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        global THEME_COLOR

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.theme_color = THEME_COLOR
        self.window.config(padx=20, pady=20, bg=self.theme_color)

        self.score_display = Label(text="Score: 0", fg="white", bg=self.theme_color, font=("Calibri", 15, "bold"))
        self.score_display.grid(row=0, column=1)

        self.question_display = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.question_display.create_text(150, 125, text="Question Goes Here", fill="black",
                                                               font=("Calibri", 20, "italic"), width=280,)
        self.question_display.grid(columnspan=2, row=1, column=0, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, activebackground=self.theme_color, borderwidth=0,
                                  highlightthickness=0, pady=10, command=self.input_true)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, activebackground=self.theme_color, borderwidth=0,
                                   highlightthickness=0, command=self.input_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_display.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_display.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_display.itemconfig(self.question_text, text=q_text)
        else:
            self.question_display.itemconfig(self.question_text, text=f"You've reached the end.\n"
                                                                      f"Your final score was: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def input_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def input_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_display.config(bg="green")
        else:
            self.question_display.config(bg="red")
        self.window.after(1000, self.get_next_question)
