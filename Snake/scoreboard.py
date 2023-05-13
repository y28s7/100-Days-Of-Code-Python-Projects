from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 15, "normal")
GAME_OVER_FONT = ("Consolas", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
