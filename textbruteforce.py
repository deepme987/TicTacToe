
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import random

res = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
selected = []


def reset():
    global chance, selected
    chance = 0
    selected = []


def disp(select):
    global chance
    chance += 1
    selected.append(select)
    check()


def check():
    global selected, res, chance

    p1 = [selected[i] for i in range(0, len(selected), 2)]
    p2 = [selected[i+1] for i in range(0, len(selected)-1, 2)]
    avail = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x not in selected]

    for x in res:
        if set(p1) >= set(x):
            print("Player 1 Wins!")
            reset()
            return
        elif set(p2) >= set(x):
            print("Player 2 Wins!")
            reset()
            return

    if len(selected) == 9:
        print("Draw!")
        return

    if chance % 2 == 1:
        my_dict = {}
        for i in avail:
            temp = avail.copy()
            temp.remove(i)
            my_dict[i] = playMove(temp, 1, p1, p2)
        print(my_dict)

        my_list = [x for x in my_dict if my_dict[x] == my_dict[max(my_dict, key=my_dict.get)]]
        x = random.choice(my_list)
        print(x)
        disp(x)


def playMove(avail, minmax, p1, p2):
    global res

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
            if len(avail) % 2 == 1:
                p1.append(i)
            else:
                p2.append(i)
            z = avail.copy()
            z.remove(i)
            val = playMove(z, 0, p1, p2)
            temp = max(temp, val)
        return temp

    else:
        temp = 999
        for i in avail:
            if len(avail) % 2 == 1:
                p1.append(i)
            else:
                p2.append(i)
            z = avail.copy()
            z.remove(i)
            val = playMove(z, 1, p1, p2)
            temp = min(val, temp)
        return temp


if __name__ == '__main__':
    reset()
    while 1:
        n = int(input("Enter your move: "))
        disp(n)
