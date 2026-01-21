from guizero import App, Text, Box, PushButton, info, error

app = App(title="Bảng tuần hoàn hóa học")

chu = Text(app, "Bảng tuần hoàn hóa học")


box = Box(app, align="left", layout="grid", height=500, width=100)

lines = ""

result = ""

def read_line():
    global lines, result
    try:
        with open("nguyentu.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                result = line.strip()
    except FileNotFoundError:
        error("Lỗi", "File không tồn tại")

y = 0
for y in range(0, 7):
    read_line()

    buttons = PushButton(box, width=4, height=2, grid=[0,y], text=result)

app.display()