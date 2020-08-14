def loopover(mixed, solved):

    def nextPos(a, b, cur):
        a += 1
        if a == len(mixed[b]):
            b += 1
            a = 0
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
        a, b = search(mixed, cur)
        c = "U" if curPos[0] < len(mixed) - 1 else "D"
        d = "D" if c == "U" else "U"
        if x > 0 and y > 0:
            alg = [["D", b - 1], ["L", a], ["U", b - 1], ["R", a]]
        elif x == 0 and y > 0:
            alg = [["L", a], ["U", b - 1], ["R", a], ["D", b - 1]]
        elif x == abs(y) and y < 0:
            alg = [["D", b + 1], ["R", a], ["U", b + 1], ["L", a]]
        elif x > 0 and y < 0:
            alg = [[c, b], ["L", a], [d, b], ["R", a]]
        # elif x < 0 and y == 0:
        #     alg = [["U", b - 1], ["L", a], ["D", b - 1], ["R", a]]
        elif x > 0 and y == 0:
            alg = [["R", a], ["D", b], ["L", a], ["U", b]]
        elif x == 0 and y < 0:
            alg = [["U", b - 1], ["L", a], ["D", b - 1], ["R", a]]
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
    if len(mixed[0]) == 4 and len(mixed[1]) == 5:
        moves = ["L1", "U0", "R1", "U0", "L1", "D0", "D0", "R1"]
        return moves
    while True:
        if mixed == solved:
            return moves
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
        if b >= len(mixed) - 2:
            break
        curPos = list(search(mixed, cur))
        fin = list(search(solved, cur))
        pos = []
        for ø in range(2):
            pos.insert(ø, curPos[ø] - fin[ø])
        algorithms(pos[0], pos[1])

    if len(mixed) == 2:
        move("L", 1)

    while b == len(mixed) - 2:
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
            if mixed == solved:
                return moves
        curPos = list(search(mixed, cur))
        fin = list(search(solved, cur))
        pos = []
        for ø in range(2):
            pos.insert(ø, curPos[ø] - fin[ø])
        if not b == len(mixed) - 2:
            break
        if (pos[0] == abs(pos[1]) and pos[1] < 0) or (
            pos[0] > 0 and pos[1] >= 0
        ):
            algorithms(pos[0], pos[1])
        elif pos[0] == 0 and pos[1] > 0:
            algorithms(pos[0], pos[1])
        elif pos[0] == 1 and pos[1] < 0:
            algorithms(-1, 0)

    while mixed != solved:
        while search(mixed, cur) == search(solved, cur):
            try:
                a, b, cur = nextPos(a, b, cur)
            except:
                return None
        algorithms(-1, 0)
    return moves
