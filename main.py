import turtle
import pandas as pd

writer = turtle.Turtle(visible=False)
writer.penup()
screen = turtle.Screen()
screen.setup(720,505)
screen.bgpic("blank_states_img.gif")
score=0


data = pd.read_csv("all_states.csv")

states = data.state.tolist()
guessed_states=[]
missed_states=[]

screen.textinput(f"Directions","1. Guess states to score\n2. Enter exit to end game and get file of un-guessed states\n3. Click Ok to continue")

for _ in range(len(states)):
    ans = screen.textinput(f"States Quiz {score}/50 ","Enter state name : ").title()
    data_row =data[data.state==ans]
    if ans == "Exit":
        for state in states:
            if state not in guessed_states:
                missed_states.append(state)
        data = pd.DataFrame(missed_states)
        data.tocsv("States_to_learn.csv")
        break
    if ans in states:
        score+=1
        guessed_states+=ans
        writer.goto(int(data_row.x),int(data_row.y))
        writer.write(data_row.state.item(),False,"center",("monospace",8,"bold"))
        
writer.goto(0,0)
writer.write(f"Score : {score}",False,"center",("monospace",20,"bold"))


screen.mainloop()
