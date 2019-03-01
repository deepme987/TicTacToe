
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import random
import csv

res = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


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

    ui.label_1.setText("")


def disable():
    ui.pushButton_1.setEnabled(False)
    ui.pushButton_2.setEnabled(False)
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
    self.setIconSize(QtCore.QSize(175,180))

    chance += 1
    selected.append(select)
    check()


def check():
    global selected, res, chance

    p1 = [selected[i] for i in range(0, len(selected), 2)]
    p2 = [selected[i+1] for i in range(0, len(selected)-1, 2)]

    for x in res:
        if set(p1) >= set(x):
            ui.label_1.setText("Player 1 Wins!")
            storeData("L")
            disable()
            return
        elif set(p2) >= set(x):
            ui.label_1.setText("Player 2 Wins!")
            storeData("W")
            disable()
            return

    if len(selected) == 9:
        ui.label_1.setText("Draw!")
        storeData("D")
        return

    if chance % 2 == 1:
        k = testLose(p2,p1)               #Win Move
        if k == 99:
            k = testLose(p1,p2)           #Force Move
            if k == 99:
                avail = [x for x in [1,2,3,4,5,6,7,8,9] if x not in selected]
                dict = {x: 0 for x in avail}

                with open('dataset.csv', mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0:
                            line_count += 1
                            continue

                        temp = [x for x in row[:-1] if int(x) not in selected]
                        while '0' in temp:
                            del temp[-1]
                        if len(temp) > 0:
                            if row[chance] == temp[0]:
                                if row[-1] == 'W':
                                    dict[int(temp[0])] += 1
                                elif row[-1] == 'D':
                                    dict[int(temp[0])] += 0.5
                                elif row[-1] == 'L':
                                    dict[int(temp[0])] -= 1
                            else:
                                dict[int(random.choice(temp))] += 0.5
                        else:
                            dict[random.choice(avail)] -= 0.5
                x = max(dict, key=dict.get)
            else:
                x = k
        else:
            x = k
        exec("disp(ui.pushButton_%d, %d)" % (x,x))


def testLose(p1,p2):
    global selected

    for x in res:
        if len(set(x)-set(p1)) < 2 and list(set(x) - set(p1))[0] not in p2:
            return list(set(x) - set(p1))[0]

    return 99


def storeData(outcome):
    global selected
    with open('dataset.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(9 - len(selected)):
            selected.append(0)
        csv_writer.writerow(
            [str(selected[0]), str(selected[1]), str(selected[2]), str(selected[3]), str(selected[4]), str(selected[5]),
             str(selected[6]), str(selected[7]), str(selected[8]), outcome])


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