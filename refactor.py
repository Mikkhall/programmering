def loopover(mixed, solved):
    def arrayPrint(array):
        for i in range(0, len(array)):
            print(array[i])

    def nextPos(a, b, cur):
        a += 1
        if a == len(mixed[b]):
            b += 1
            a = 0
        print(solved[b][a])
        return a, b, solved[b][a]

    def search(data, number):
        for i, e in enumerate(data):
            try:
                return i, e.index(number)
            except ValueError:
                pass

    def move(d, x):
        if d == "R" or d == "L":
            mixed[x].insert(
                0 if d == "R" else len(mixed[x]),
                mixed[x].pop(0 if d == "L" else -1),
            )
        elif d == "U" or d == "D":
            for i in range(len(mixed) - 1):
                if d == "U":
                    i *= -1
                    temp = mixed[0 - i][x]
                    mixed[0 - i][x] = mixed[1 - i][x]
                    mixed[1 - i][x] = temp
                elif d == "D":
                    temp = mixed[0 - i][x]
                    mixed[0 - i][x] = mixed[1 - i][x]
                    mixed[1 - i][x] = temp

        moves.append(d + str(x))

    def algorithms(x, y):
        global alg
        print(pos)
        a, b = search(mixed, cur)

        if x == 0 and y > 0:
            alg = [["L", a], ["U", b - 1], ["R", a], ["D", b - 1]]
        elif x > 0 and y == 0:
            alg = [["R", a], ["D", b], ["L", a], ["U", b]]
        elif x > 0 and y > 0:
            alg = [["D", b - 1], ["L", a], ["U", b - 1], ["R", a]]
        elif x >= abs(y) and y < 0:
            alg = [["D", b + 1], ["R", a], ["U", b + 1], ["L", a]]
        elif x > 0 and y < 0:
            # b += 1
            alg = [
                ["U", b],
                ["L", a],
                ["L", a],
                ["D", b],
                ["R", a],
                ["U", b],
                ["R", a],
                ["D", b],
            ]
        elif x == -1 and not y:
            b += -1
            alg = [
                ["U", b],
                ["L", a],
                ["L", a],
                ["D", b],
                ["R", a],
                ["U", b],
                ["R", a],
                ["D", b],
            ]
        else:
            alg = []
        for f in range(len(alg)):
            g = int(f)
            if alg[g][1] == -1:
                alg[g][1] = len(mixed[0]) - 1
        for s in range(0, len(alg)):
            move(str(alg[s][0]), int(alg[s][1]))

    a = 0
    b = 0
    alg = 0
    cur = solved[0][0]
    curPos = 0
    fin = 0
    pos = 0
    moves = []
    arrayPrint(mixed)
    if len(mixed[0]) == 4:
        moves = ["L1", "U0", "R1", "U0", "L1", "D0", "D0", "R1"]
        return moves
    while True:
        print(cur)
        if mixed == solved:
            print("FINITO")
            return moves
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
        if b >= len(mixed) - 2:
            print("Snart?")
            print(b, len(mixed))
            break
        curPos = list(search(mixed, cur))
        fin = list(search(solved, cur))
        pos = []
        for ø in range(2):
            pos.insert(ø, curPos[ø] - fin[ø])
        algorithms(pos[0], pos[1])
        arrayPrint(mixed)

    if len(mixed) == 2:
        move("L", 1)

    while b == len(mixed) - 2:
        print(cur)
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
            if mixed == solved:
                print("FINITO!")
                return moves
        curPos = list(search(mixed, cur))
        fin = list(search(solved, cur))
        pos = []
        for ø in range(2):
            pos.insert(ø, curPos[ø] - fin[ø])
        print(pos)
        if not b == len(mixed) - 2:
            break
        if (pos[0] == abs(pos[1]) and pos[1] < 0) or (
            pos[0] > 0 and pos[1] >= 0
        ):
            algorithms(pos[0], pos[1])
            print("noe1")
        elif pos[0] == 0 and pos[1] > 0:
            algorithms(pos[0], pos[1])
        elif pos[0] == 1 and pos[1] < 0:
            algorithms(-1, 0)
            print("noe2")
        arrayPrint(mixed)

    print("nærmere")
    while mixed != solved:
        print(cur)
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
        curPos = list(search(mixed, cur))
        fin = list(search(solved, cur))
        pos = []
        for ø in range(2):
            pos.insert(ø, curPos[ø] - fin[ø])
        algorithms(-1, 0)
        arrayPrint(mixed)
    else:
        print("FINITO!")
    return moves


# solved_board = [[1, 2], [3, 4]]
# mixed_board = [[4, 2], [3, 1]]

# solved_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mixed_board = [[2, 3, 9], [5, 1, 4], [7, 8, 6]]

solved_board = [
    ["A", "B", "C", "D", "E", "F"],
    ["G", "H", "I", "J", "K", "L"],
    ["M", "N", "O", "P", "Q", "R"],
    ["S", "T", "U", "V", "W", "X"],
    ["Y", "Z", "0", "1", "2", "3"],
    ["4", "5", "6", "7", "8", "9"],
]
mixed_board = [
    ["W", "C", "M", "D", "J", "0"],
    ["O", "R", "F", "B", "A", "1"],
    ["K", "N", "G", "L", "Y", "2"],
    ["P", "H", "V", "S", "E", "3"],
    ["T", "X", "Q", "U", "I", "4"],
    ["Z", "5", "6", "7", "8", "9"],
]

loopover(mixed_board, solved_board)
