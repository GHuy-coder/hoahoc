from guizero import App, Text, Box, PushButton, info

app = App(title="Bảng tuần hoàn hóa học")

chu = Text(app, "Bảng tuần hoàn hóa học")


box = Box(app, align="left", layout="grid")

h  = PushButton(box, text="H",  grid=[0,0], width=4, height=2)
li = PushButton(box, text="Li", grid=[0,1], width=4, height=2)
be = PushButton(box, text="Be", grid=[1,1], width=4, height=2)
na = PushButton(box, text="Na", grid=[0,2], width=4, height=2)
mg = PushButton(box, text="Mg", grid=[1,2], width=4, height=2)

khoang_giua = Box(app, width=200)

box1 = Box(app, align="right", layout="grid")

he  = PushButton(box1, text="He",  grid=[5,0], width=4, height=2)
ne = PushButton(box1, text="Ne", grid=[5,2], width=4, height=2)
f = PushButton(box1, text="F", grid=[4,2], width=4, height=2)
na = PushButton(box1, text="Na", grid=[3,2], width=4, height=2)
n = PushButton(box1, text="N", grid=[2,2], width=4, height=2)
c = PushButton(box1, text="C", grid=[1,2], width=4, height=2)
b = PushButton(box1, text="B", grid=[0,2], width=4, height=2)
ar = PushButton(box1, text="Ar", grid=[5,3], width=4, height=2)
cl = PushButton(box1, text="Cl", grid=[4,3], width=4, height=2)
s = PushButton(box1, text="S", grid=[3,3], width=4, height=2)
p = PushButton(box1, text="P", grid=[2,3], width=4, height=2)
si = PushButton(box1, text="Si", grid=[1,3], width=4, height=2)
al = PushButton(box1, text="Al", grid=[0,3], width=4, height=2)

app.display()