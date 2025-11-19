import tkinter as tk
import math
root = tk.Tk()
root.title("Kids Drawing Art")

WIDTH, HEIGHT = 700, 500
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#fffdf7")
canvas.pack()
for i in range(20, HEIGHT, 25):
  canvas.create_line(0, i, WIDTH, i, fill="#f0f0f0")
  canvas.create_line(60, 0, 60, HEIGHT, fill="#ffaaaa", width=2)
canvas.create_oval(50, 50, 120, 120, fill="yellow", outline="orange", width=3)
for i in range(12):
    angle = i * 30
    x1 = 85
    y1 = 85
    x2 = x1 + 40 * math.cos(math.radians(angle))
    y2 = y1 + 40 * math.sin(math.radians(angle))
    canvas.create_line(x1, y1, x2, y2, fill="orange", width=3)
def cloud(x, y):
    canvas.create_oval(x, y, x+60, y+40, fill="white", outline="")
    canvas.create_oval(x+30, y-10, x+90, y+40, fill="white", outline="")
    canvas.create_oval(x+60, y, x+120, y+40, fill="white", outline="")

cloud(150, 40)
cloud(350, 60)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
for i, c in enumerate(colors):
    canvas.create_arc(100, 150, 600, 600, start=180, extent=180,
                      style="arc", outline=c, width=10)
canvas.create_rectangle(250, 250, 390, 380, fill="#ffe8c6", outline="brown", width=3)
canvas.create_polygon(250, 250, 390, 250, 320, 190, fill="red", outline="brown", width=3)
canvas.create_rectangle(300, 300, 340, 380, fill="#c9ffff", outline="blue", width=3)
canvas.create_rectangle(260, 300, 290, 330, fill="white", outline="brown", width=2)
canvas.create_rectangle(430, 280, 450, 380, fill="#8b4513", outline="brown")
canvas.create_oval(390, 210, 490, 310, fill="green", outline="darkgreen", width=3)
def flower(x, y):
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="yellow", outline="orange")
    canvas.create_line(x, y+10, x, y+20, fill="green", width=3)

flower(200, 420)
flower(230, 430)
flower(260, 415)
flower(290, 440)
canvas.create_oval(80, 310, 150, 360, fill="#f2d0a7", outline="brown", width=3)
canvas.create_oval(60, 270, 120, 330, fill="#f2d0a7", outline="brown", width=3)
canvas.create_polygon(65, 275, 85, 250, 100, 275, fill="#f2d0a7", outline="brown", width=3)
canvas.create_polygon(80, 275, 105, 250, 120, 275, fill="#f2d0a7", outline="brown", width=3)
canvas.create_oval(75, 290, 85, 300, fill="white")
canvas.create_oval(95, 290, 105, 300, fill="white")
canvas.create_oval(80, 293, 83, 297, fill="black")
canvas.create_oval(100, 293, 103, 297, fill="black")
canvas.create_oval(88, 305, 93, 310, fill="pink")
canvas.create_line(90, 310, 90, 315, fill="black", width=2)
canvas.create_line(90, 315, 85, 320, fill="black", width=2)
canvas.create_line(90, 315, 95, 320, fill="black", width=2)
canvas.create_line(150, 330, 180, 310, fill="brown", width=5)
root.mainloop()

