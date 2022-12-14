import tkinter as tk
import tkinter.messagebox as tkm
import math
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        pass
        siki = entry.get() # 数式の文字列
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    elif num == "x^2": #入力された数のべき乗の計算
        siki = entry.get()
        res = eval(siki) 
        entry.delete(0, tk.END) 
        ans = str(int(siki) * int(siki))
        entry.insert(tk.END, ans) 
    elif num == "2^x": #２の入力された数乗の計算
        siki = entry.get() 
        res = eval(siki) 
        entry.delete(0, tk.END) 
        ans = 2 ** int(siki)
        entry.insert(tk.END, ans)
    elif num == "%": #%の計算を行いたかったが実装できなかった。
        siki = entry.get() 
        res = eval(siki) 
        entry.delete(0, tk.END)
        ans = int(siki)/100
        entry.insert(tk.END, ans)
    elif num == "√":#平方根の計算
        siki = entry.get() 
        res = eval(siki)
        entry.delete(0, tk.END) 
        rooot = math.sqrt(int(siki))
        entry.insert(tk.END, rooot)
    elif num == "AC":#オールキャンセル
        entry.delete(0, tk.END)
    elif num == "1/x": #逆数の計算
        siki = entry.get() 
        res = eval(siki)
        entry.delete(0, tk.END) 
        ans = 1/int(siki)
        entry.insert(tk.END, ans)
    else: 
        entry.insert(tk.END, num)
    

root = tk.Tk()
root.geometry("380x480")

entry = tk.Entry(root, justify="right", width=10, font=("",40),bg = "lightyellow")#入力された数のプログラム
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for num in range(9,-1,-1):#１～９までの数字のボタンのプログラム
    button = tk.Button(root,text=f"{num}", width=4, height=1, font=("", 30),bg = "slategrey")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        r += 1
        c = 0

operators = ["+","-","*","/","x^2","2^x","%",".","AC","1/x","√","="]
for ope in operators: #計算するボタンのプログラム
    button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("", 30),bg = "honeydew")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        r += 1
        c = 0
root.mainloop()