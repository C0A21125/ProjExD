import tkinter as tk
import maze_maker as mm
import random
def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():                    #移動に関する関数
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1:  # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1        
    cx, cy = mx*100+50, my*100+50
    canvas.coords("mikata", cx, cy)
    root.after(100, main_proc)



if __name__ == "__main__":          #キャラクターに関する関数
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)


    mx, my = 1, 1
    #tx, ty = random.randint(), random.randint()
    cx, cy = mx*100+50, my*100+50
    #cx2,cy2 = tx*100+50, ty*100+50
    tori = tk.PhotoImage(file="fig/mikata.png")
    #teki = tk.PhotoImage(file="fig/teki.png")
    canvas.create_image(cx, cy, image=tori, tag="mikata")
    #canvas.create_image(tx, ty, image2=teki, ta="tekikyara")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()