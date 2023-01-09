import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_IMAGE = "images/true.png"
WRONG_IMAGE = "images/false.png"
RIGHT_COLOR = "#82CD47".lower()
WRONG_COLOR = "#DD5353".lower()
FONT = ("Arial", 20, "italic")

class QuizInterface():
    

    def __init__(self, quiz_brain: QuizBrain):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = tk.Canvas()
        self.canvas.config(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file=RIGHT_IMAGE)
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file=WRONG_IMAGE)
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.quiz = quiz_brain
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Final score: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    
    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=WRONG_COLOR)

        self.window.after(1000, self.get_next_question)
    