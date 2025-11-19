from tkinter import Tk, Canvas
import random
WIDTH, HEIGHT = 500, 600
root = Tk()
root.title("Cartoon Singer Animation")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
def draw_singer():canvas.create_oval(WIDTH//2-30, HEIGHT-250, WIDTH//2+30, HEIGHT-190, fill="white")
canvas.create_text(WIDTH//2-10, HEIGHT-230, text="👀", font=("Arial", 20))
canvas.create_text(WIDTH//2, HEIGHT-210, text="👄", font=("Arial", 20))
canvas.create_rectangle(WIDTH//2-25, HEIGHT-190, WIDTH//2+25, HEIGHT-100, fill="blue")
canvas.create_line(WIDTH//2-15, HEIGHT-100, WIDTH//2-15, HEIGHT-60, width=4, fill="blue")
canvas.create_line(WIDTH//2-15, HEIGHT-100, WIDTH//2-15, HEIGHT-60, width=4, fill="blue")
canvas.create_line(WIDTH//2+15, HEIGHT-100, WIDTH//2+15, HEIGHT-60, width=4, fill="blue")
canvas.create_line(WIDTH//2-25, HEIGHT-170, WIDTH//2-50, HEIGHT-150, width=4, fill="blue")
canvas.create_line(WIDTH//2+25, HEIGHT-170, WIDTH//2+50, HEIGHT-150, width=4, fill="blue")
canvas.create_text(WIDTH//2+10, HEIGHT-160, text="🎤", font=("Arial", 24))

draw_singer()
notes = []

def add_note():
    x = random.randint(50, WIDTH-50)
    y = HEIGHT
    speed = random.randint(3, 6)
    note_id = canvas.create_text(x, y, text="🎵", font=("Arial", 24), fill=random.choice(["yellow","cyan","magenta","white","red"]))
    notes.append({"id": note_id, "y": y, "speed": speed})
    root.after(400, add_note)
   
    def move_notes():
        for note in notes[:]:
            canvas.move(note["id"],0 -note["speed"])
            note["y"] -= note["speed"]
            for note in notes [:]:
             if note["y"] < -50:
                canvas.delete(note["id"])
                notes.remove(note)
    root.after(50, move_notes) 
    add_note()
    move_notes()

root.mainloop()

