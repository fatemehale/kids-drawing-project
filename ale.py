import tkinter as tk
import math

root = tk.Tk()
root.title("Animated Kids Drawing")

WIDTH, HEIGHT = 800, 600
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#fffdf7")
canvas.pack()
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
for i, c in enumerate(colors):
    pass  # TODO: Add loop body

def draw_house():
    canvas.create_rectangle(300, 350, 450, 470, fill="#ffe8c6", outline="brown", width=3)
    canvas.create_polygon(300, 350, 450, 350, 375, 280, fill="red", outline="brown", width=3)
    canvas.create_rectangle(360, 410, 390, 470, fill="#c9ffff", outline="blue", width=2)
    canvas.create_rectangle(310, 380, 340, 410, fill="white", outline="brown", width=2)
    canvas.create_rectangle(410, 380, 440, 410, fill="white", outline="brown", width=2)

def draw_tree():
    canvas.create_rectangle(500, 400, 520, 500, fill="#8b4513", outline="brown")
    canvas.create_oval(470, 350, 550, 430, fill="green", outline="darkgreen", width=3)

flowers = [(200, 500), (240, 520), (280, 505), (320, 525)]
def draw_flowers():
    for x, y in flowers:
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="yellow", outline="orange")
        canvas.create_line(x, y+10, x, y+25, fill="green", width=3)

sun_angle = 0
def draw_sun():
    global sun_angle
    sun_x, sun_y = 100, 100
    sun_r = 50
    canvas.create_oval(sun_x-sun_r, sun_y-sun_r, sun_x+sun_r, sun_y+sun_r, fill="yellow", outline="orange", width=3)
    for i in range(12):
        angle = i * 30 + sun_angle
        x2 = sun_x + sun_r * 1.5 * math.cos(math.radians(angle))
        y2 = sun_y + sun_r * 1.5 * math.sin(math.radians(angle))
        canvas.create_line(sun_x, sun_y, x2, y2, fill="orange", width=3)
    sun_angle += 4

clouds = [{"x": 200, "y": 80, "dx": 2}, {"x": 500, "y": 50, "dx": 1.5}]
def draw_clouds():
    for c in clouds:
        c["x"] += c["dx"]
        if c["x"] > WIDTH:
            c["x"] = -120
        x, y = c["x"], c["y"]
        canvas.create_oval(x, y, x+60, y+40, fill="white", outline="")
        canvas.create_oval(x+30, y-10, x+90, y+40, fill="white", outline="")
        canvas.create_oval(x+60, y, x+120, y+40, fill="white", outline="")
cat_dx = 0
cat_dy = 0
cat_tail_angle = 0
def draw_cat():
    global cat_tail_angle
    canvas.create_oval(100, 450, 180, 500, fill="#f2d0a7", outline="brown", width=3)
    canvas.create_oval(120, 410, 160, 450, fill="#f2d0a7", outline="brown", width=3)
    canvas.create_polygon(125, 410, 135, 390, 145, 410, fill="#f2d0a7", outline="brown", width=2)
    canvas.create_polygon(135, 410, 150, 390, 155, 410, fill="#f2d0a7", outline="brown", width=2)
    canvas.create_oval(130, 420, 135, 425, fill="white")
    canvas.create_oval(145, 420, 150, 425, fill="white")
    canvas.create_oval(132, 422, 133, 423, fill="black")
    canvas.create_oval(147, 422, 148, 423, fill="black")
    canvas.create_oval(138, 430, 142, 434, fill="pink")
    canvas.create_line(140, 434, 140, 438, fill="black", width=1)
    canvas.create_line(140, 438, 136, 442, fill="black", width=1)
    canvas.create_line(140, 438, 144, 442, fill="black", width=1)
    tail_x = 180 + 20 * math.sin(math.radians(cat_tail_angle))
    tail_y = 460 - 10 * math.cos(math.radians(cat_tail_angle))
    canvas.create_line(180, 460, tail_x, tail_y, fill="brown", width=5)
    cat_tail_angle += 15

def animate():
    canvas.delete("all")
    draw_sun()
    draw_clouds()
    draw_house()
    draw_tree()
    draw_flowers()
    draw_cat()
    root.after(80, animate)

animate()
root.mainloop()
