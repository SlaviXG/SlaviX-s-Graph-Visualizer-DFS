import tkinter as tk
from math import *
import time

root = tk.Tk()
root.title("SlaviX's Graph Visualizer")

BG_COLOR = "white"

cn = tk.Canvas(root, width = 700, height = 700, bg = BG_COLOR)
cn.pack()

g = []
used = []

ver = []
temp = []

idx = 0

def set_vertex (event) :
    global idx
    x = event.x
    y = event.y
    for i in ver :
        if((x-i[0])*(x-i[0])+(y-i[1])*(y-i[1]) < 1600) : return
    ver.append([x,y,idx])
    cn.create_oval(x-19, y+19, x+19, y-19, fill = "grey75", outline = "black", width = 1)
    cn.create_text(x,y,text = str(idx+1),justify = tk.CENTER,font="Impact 12", fill="black")
    g.append([])
    used.append(0)
    idx+=1
    print("Set :",x ,y)
    

def try_to_merge (event) :
    x = event.x
    y = event.y
    for i in ver :
        if((x-i[0])*(x-i[0])+(y-i[1])*(y-i[1]) <= 400) :
            if(len(temp) == 0) :
                temp.append([i[0],i[1],i[2]])
                cn.create_oval(i[0]-19, i[1]+19, i[0]+19, i[1]-19, fill = "grey85", outline = "black", width = 1)
                cn.create_text(i[0],i[1],text = str(i[2]+1),justify = tk.CENTER,font="Impact 12", fill="black")
            else :
                temp.append([i[0],i[1],i[2]])
                g[temp[0][2]].append(temp[1][2])
                g[temp[1][2]].append(temp[0][2])
                cn.create_polygon(temp[0][0], temp[0][1], temp[1][0], temp[1][1], fill = "black", outline = "black", width = 0)
                if(used[temp[0][2]] == 0) :
                    cn.create_oval(temp[0][0]-19, temp[0][1]+19, temp[0][0]+19, temp[0][1]-19, fill = "grey75", outline = "black", width = 1)
                    cn.create_text(temp[0][0],temp[0][1],text = str(temp[0][2]+1),justify = tk.CENTER,font="Impact 12", fill="black")
                else :
                    cn.create_oval(temp[0][0]-19, temp[0][1]+19, temp[0][0]+19, temp[0][1]-19, fill = "grey52", outline = "black", width = 1)
                    cn.create_text(temp[0][0],temp[0][1],text = str(temp[0][2]+1),justify = tk.CENTER,font="Impact 12", fill="black")
                if(used[temp[1][2]] == 0) :
                    cn.create_oval(temp[1][0]-19, temp[1][1]+19, temp[1][0]+19, temp[1][1]-19, fill = "grey75", outline = "black", width = 1)
                    cn.create_text(temp[1][0],temp[1][1],text = str(temp[1][2]+1),justify = tk.CENTER,font="Impact 12", fill="black")
                else :
                    cn.create_oval(temp[1][0]-19, temp[1][1]+19, temp[1][0]+19, temp[1][1]-19, fill = "grey52", outline = "black", width = 1)
                    cn.create_text(temp[1][0],temp[1][1],text = str(temp[1][2]+1),justify = tk.CENTER,font="Impact 12", fill="black")
                print("Merged :", temp[0][0], temp[0][1], " and ", temp[1][0], temp[1][1])
                temp.clear()
                break

def dfs (event) :
    x = event.x
    y = event.y
    s = -1
    for i in ver :
        if((x-i[0])*(x-i[0])+(y-i[1])*(y-i[1]) <= 400) :
            s = i[2]
            break
    path = []
    
    def df_s (v) :
        path.append(v)
        used[v] = 1;
        for to in g[v] :
            if(used[to]==0) :
                df_s(to)

    if(used[s]==0) :
        df_s(s);

    for v in path :
        cn.create_oval(ver[v][0]-19, ver[v][1]+19, ver[v][0]+19, ver[v][1]-19, fill = "grey52", outline = "black", width = 1)
        cn.create_text(ver[v][0],ver[v][1],text = str(v+1),justify = tk.CENTER,font="Impact 12", fill="black")
        cn.update()
        time.sleep(0.5)
    

root.bind("<Button-1>",set_vertex)
root.bind("<Button-2>",dfs)
root.bind("<Button-3>",try_to_merge)

root.mainloop()
