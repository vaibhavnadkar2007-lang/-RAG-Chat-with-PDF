import tkinter as tk
import random

WIDTH, HEIGHT = 400, 600
root = tk.Tk()
root.title("Car Racing Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="gray20")
canvas.pack()

# Road
canvas.create_rectangle(WIDTH//4, 0, WIDTH*3//4, HEIGHT, fill="gray30", outline="")

# Road lines
lines = []
for i in range(0, HEIGHT, 50):
    lines.append(canvas.create_rectangle(WIDTH//2-3, i, WIDTH//2+3, i+25, fill="white"))

# Player car
car = canvas.create_rectangle(WIDTH//2-25, HEIGHT-120, WIDTH//2+25, HEIGHT-20, fill="blue", outline="white", width=2)
canvas.create_rectangle(WIDTH//2-15, HEIGHT-100, WIDTH//2+15, HEIGHT-80, fill="lightblue")

# Enemy cars
enemies = []
for i in range(3):
    x = random.randint(WIDTH//4+10, WIDTH*3//4-60)
    y = -i*200
    enemies.append(canvas.create_rectangle(x, y, x+50, y+100, fill="red", outline="white", width=2))
    canvas.create_rectangle(x+10, y+20, x+40, y+40, fill="pink")

score = 0
speed = 6
score_label = canvas.create_text(70, 30, text="Score: 0", fill="white", font=("Arial", 16, "bold"))

def move_left(event):
    coords = canvas.coords(car)
    if coords[0] > WIDTH//4 + 5:
        canvas.move(car, -20, 0)

def move_right(event):
    coords = canvas.coords(car)
    if coords[2] < WIDTH*3//4 - 5:
        canvas.move(car, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

def game_loop():
    global score, speed
    for line in lines:
        canvas.move(line, 0, speed)
        if canvas.coords(line)[1] > HEIGHT:
            canvas.move(line, 0, -HEIGHT-25)

    for enemy in enemies:
        canvas.move(enemy, 0, speed)
        coords = canvas.coords(enemy)
        if coords[1] > HEIGHT:
            new_x = random.randint(WIDTH//4+10, WIDTH*3//4-60)
            canvas.coords(enemy, new_x, -100, new_x+50, 0)
            score += 1
            canvas.itemconfig(score_label, text=f"Score: {score}")
            if score % 5 == 0:
                speed += 1

        car_coords = canvas.coords(car)
        if (car_coords[0] < coords[2] and car_coords[2] > coords[0] and
            car_coords[1] < coords[3] and car_coords[3] > coords[1]):
            canvas.create_text(WIDTH//2, HEIGHT//2, text=f"GAME OVER\nFinal Score: {score}", fill="yellow", font=("Arial", 24, "bold"))
            return

    root.after(30, game_loop)

game_loop()
root.mainloop()
