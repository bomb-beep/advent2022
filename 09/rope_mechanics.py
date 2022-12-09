import sys

cmd_list = open("input.txt").read()

head = [0,0]
tail = [0,0]

tail_locations = set(tail)

def head_tail_adjacent():
    return abs(head[0]-tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move_head(direction):
    if direction == "L":
        head[0] -= 1
    elif direction == "R":
        head[0] += 1
    elif direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1


def move_tail():
    if not head_tail_adjacent():
        if head[0] - tail[0] > 0:
            tail[0] += 1
        elif head[0] - tail[0] < 0:
            tail[0] -= 1

        if head[1] - tail[1] > 0:
            tail[1] += 1
        elif head[1] - tail[1] < 0:
            tail[1] -= 1

for line in cmd_list.split("\n"):
    direction,count = line.split(" ")
    count = int(count)
    while count > 0:
        move_head(direction)
        move_tail()
        #print(head,tail)
        if not head_tail_adjacent():
            print("ERROR! Head and tail out of alignment!")
            print(head,tail)
            sys.exit()
        tail_locations.add(tuple(tail))
        count -= 1

print(len(tail_locations))