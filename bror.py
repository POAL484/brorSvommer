import cv2 as cv
import tkinter as tk
import pyperclip as pc

FILE  = "PagMan.png"
frame = cv.imread(FILE)
frame_clr = cv.imread(FILE)

colors = {\
    '&0': (0, 0, 0), '&1': (170, 0, 0), '&2': (0, 170, 0), '&3': (170, 170, 0), '&4': (0, 0, 170), \
    '&5': (170, 0, 170), '&6': (0, 170, 255), \
    '&9': (255, 85, 85), '&a': (85, 255, 85), '&b': (255, 255, 85), '&c': (85, 85, 255), \
    '&d': (255, 85, 255), '&e': (85, 255, 255), '&f': (255, 255, 255)}

frame_colored = {}
for x in range(frame.shape[0]):
    frame_colored[x] = {}
    for y in range(frame.shape[1]):
        frame_colored[x][y] = "&f"

for x in range(frame.shape[0]):
    for y in range(frame.shape[1]):
        colored = {}
        for i in colors.keys():
            delta = 0
            delta += abs(frame[x][y][0] - colors[i][0])
            delta += abs(frame[x][y][1] - colors[i][1])
            delta += abs(frame[x][y][2] - colors[i][2])
            colored[i] = delta
        clrCode = "&f"
        clrDelta = 255+255+255+1
        for i in colors.keys():
            if clrDelta > colored[i]:
                clrCode = i
                clrDelta = colored[i]
        frame_colored[x][y] = clrCode
        frame_clr[x][y] = colors[clrCode]

'''for x in range(frame.shape[0]):
    for y in range(frame.shape[1]):
        print(frame_colored[x][y], end='')
    print()'''

print("\n\n")

for x in range(frame.shape[0]):
    print("/ie lore add ", end="")
    for y in range(frame.shape[1]):
        print(frame_colored[x][y], end="")
        print("@", end="")
    print("\n")


cv.imshow("frame", frame)
cv.imshow("frame_clr", frame_clr)

def nextStep(e):
    global n
    n += 1
    nStr.set(f"{n}/{frame.shape[0]-1}")
    strtocopy = "/ie lore add "
    for l in range(frame.shape[1]):
        strtocopy += frame_colored[n][l]
        strtocopy += "@"
    pc.copy(strtocopy)

global n

root = tk.Tk()
root.geometry("500x500")
tk.Label(root, text="Нажми Enter для следующей строки.").pack()
tk.Label(root, text="Текущая строка:").pack()
nStr = tk.StringVar()
nStr.set(f"ppHop/{frame.shape[0]-1}")
n = -1
tk.Label(root, textvariable=nStr).pack()

root.bind("<Return>", nextStep)

root.mainloop()



    
    
