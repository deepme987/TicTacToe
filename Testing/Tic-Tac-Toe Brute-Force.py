
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import random

res = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
selected = []


def reset():
    global chance, selected
    chance = 0
    selected = []

    ui.pushButton_1.setEnabled(True)
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    ui.pushButton_5.setEnabled(True)
    ui.pushButton_6.setEnabled(True)
    ui.pushButton_7.setEnabled(True)
    ui.pushButton_8.setEnabled(True)
    ui.pushButton_9.setEnabled(True)

    ui.pushButton_1.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_2.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_3.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_4.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_5.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_6.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_7.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_8.setIcon(QtGui.QIcon('def.jpg'))
    ui.pushButton_9.setIcon(QtGui.QIcon('def.jpg'))

    ui.pushButton_1.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_2.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_3.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_4.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_5.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_6.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_7.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_8.setIconSize(QtCore.QSize(175, 175))
    ui.pushButton_9.setIconSize(QtCore.QSize(175, 175))

    ui.label_1.setText("Your Turn")


def disable():
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_1.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    ui.pushButton_5.setEnabled(False)
    ui.pushButton_6.setEnabled(False)
    ui.pushButton_7.setEnabled(False)
    ui.pushButton_8.setEnabled(False)
    ui.pushButton_9.setEnabled(False)


def disp(self, select):
    global chance

    if chance % 2 == 0:
        self.setIcon(QtGui.QIcon('cross.jpg'))
    else:
        self.setIcon(QtGui.QIcon('circle.jpg'))
    self.setIconSize(QtCore.QSize(175, 180))
    chance += 1
    selected.append(select)
    check()


def check():
    global selected, res, chance, recur

    p1 = [selected[i] for i in range(0, len(selected), 2)]
    p2 = [selected[i+1] for i in range(0, len(selected)-1, 2)]
    avail = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x not in selected]

    for x in res:
        if set(p1) >= set(x):
            ui.label_1.setText("Player 1 Wins!")
            disable()
            return
        elif set(p2) >= set(x):
            ui.label_1.setText("Player 2 Wins!")
            disable()
            return

    if len(selected) == 9:
        ui.label_1.setText("Draw!")
        return

    if chance % 2 == 1:
        my_dict = {}
        for i in avail:
            print("Available: ", avail, i)
            temp = avail.copy()
            temp.remove(i)
            p2temp = p2.copy()
            p2temp.append(i)
            print(temp, p1, p2, p2temp)
            recur = ""
            my_dict[i] = playMove(temp, 1, p1, p2temp)
            print(my_dict)

        my_list = [x for x in my_dict if my_dict[x] == my_dict[max(my_dict, key=my_dict.get)]]
        x = random.choice(my_list)
        print(x)
        exec("disp(ui.pushButton_%d, %d)" % (x, x))


def playMove(avail, minmax, p1, p2):
    global res, chance

    p1 = p1.copy()
    p2 = p2.copy()
    avail = avail.copy()

    for temp in res:
        if set(p1) >= set(temp):
            return +10
        elif set(p2) >= set(temp):
            return -10
        elif len(avail) == 0:
            return 0

    if minmax == 1:
        temp = -999
        for i in avail:
            p1temp = p1.copy()
            p2temp = p2.copy()

            if len(avail) % 2 == 1:
                p1temp.append(i)
            else:
                p2temp.append(i)
            z = avail.copy()
            z.remove(i)
            val = playMove(z, 0, p1temp, p2temp)
            temp = max(temp, val)
        return temp

    else:
        temp = 999

        for i in avail:
            p1temp = p1.copy()
            p2temp = p2.copy()

            if len(avail) % 2 == 1:
                p1temp.append(i)
            else:
                p2temp.append(i)

            z = avail.copy()
            z.remove(i)
            val = playMove(z, 1, p1temp, p2temp)
            recur = y

            temp = min(val, temp)
        return temp


def initButtons():
    reset()

    ui.pushButton_1.clicked.connect(lambda x: disp(ui.pushButton_1, 1) if 1 not in selected else 0)
    ui.pushButton_2.clicked.connect(lambda x: disp(ui.pushButton_2, 2) if 2 not in selected else 0)
    ui.pushButton_3.clicked.connect(lambda x: disp(ui.pushButton_3, 3) if 3 not in selected else 0)
    ui.pushButton_4.clicked.connect(lambda x: disp(ui.pushButton_4, 4) if 4 not in selected else 0)
    ui.pushButton_5.clicked.connect(lambda x: disp(ui.pushButton_5, 5) if 5 not in selected else 0)
    ui.pushButton_6.clicked.connect(lambda x: disp(ui.pushButton_6, 6) if 6 not in selected else 0)
    ui.pushButton_7.clicked.connect(lambda x: disp(ui.pushButton_7, 7) if 7 not in selected else 0)
    ui.pushButton_8.clicked.connect(lambda x: disp(ui.pushButton_8, 8) if 8 not in selected else 0)
    ui.pushButton_9.clicked.connect(lambda x: disp(ui.pushButton_9, 9) if 9 not in selected else 0)

    ui.pushButton_new.clicked.connect(reset)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QtGui.QIcon('icon.jpg'))
    ui = uic.loadUi("Main.ui")

    initButtons()

    ui.show()
    app.exec()
