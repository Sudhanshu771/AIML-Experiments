from tkinter import *
from time import *
import random 


# '0' means clean & '1' means dirty
def initmap(row,col):
    global dirty_pieces
    global maps
    global visited
    for j in range(row):
        tmp = []
        tmpv = []
        for i in range(col):
            rand = random.randint(0,1)
            if rand == 1 :
                dirty_pieces = dirty_pieces + 1
            tmp.append(rand)               #initializing pieces with random cleanliness
            tmpv.append(0)
        visited.append(tmpv)
        maps.append(tmp)
    
    for i in range(row):
        tmp = []
        for j in range(col):
                if maps[i][j] == 0 :
                    tmp.append(Label(image = tile_clean ))
                else:
                    tmp.append(Label(image = tile_dirty ))
        lab1.append(tmp)    

    for i in range(row):
            for j in range(col):        
                lab1[i][j].grid(row=i,column=j)


def cleanmaster(row,col,vacpos):
    cleaned_pieces=0
    for i in range(row):
        for j in range(col):
            vacpos[0]=i
            vacpos[1]=j
            lab1[vacpos[0]][vacpos[1]].config(image = Vacuum)
            mygui.update()
            sleep(1)
            lab1[vacpos[0]][vacpos[1]].config(image = tile_clean)
            mygui.update()
            sleep(0)
            if maps[vacpos[0]][vacpos[1]]==1:
                maps[vacpos[0]][vacpos[1]] = 0
                lab1[vacpos[0]][vacpos[1]].config(image = done_icon)
                mygui.update()
                sleep(1)
                cleaned_pieces = cleaned_pieces + 1
    print('-------------------------------------')
    print('Environment Total Pieces :' , rows*cols)
    print('dirty_pieces : ', dirty_pieces)
    print('cleaned_pieces : ', cleaned_pieces)

    print("Current location of vacuum cleaner: ",vacpos)
    print('-------------------------------------')
    print('env. after cleaning:')
    for i in range (rows):
        print (maps[i])

#main

#initializing       

maps = []
tmp_maps = []
visited = []
visited_pieces = 0
dirty_pieces = 0
cleaned_pieces = 0


rows =  4               #Row number
cols = 4                #Column number
vac_pos = [0,0]           #Current Cursor
vac_str = str(vac_pos[0]) + str(vac_pos[1])
mygui = Tk()
mygui.title("AI Vacuum Cleaner Bot")
mygui.geometry("400x400")
lab1 = []
tile_clean = PhotoImage(file="Src\\tile2.gif")
tile_dirty = PhotoImage(file="Src\\tile1.gif")
done_icon = PhotoImage(file="Src\done_icon.png")
Vacuum = PhotoImage(file="Src\Vacuum.gif")
initmap(rows,cols)
mygui.update()
tmp_maps = maps[:]

print('-------------------------------------')
print('Current Cursor Location :' , vac_pos)
print('-------------------------------------')
print('env. before cleaning:')
#showing the whole env.
for i in range (rows):
    print (maps[i])
cleanmaster(rows,cols,vac_pos)
print("Done Cleaning!!")
mygui.mainloop()
