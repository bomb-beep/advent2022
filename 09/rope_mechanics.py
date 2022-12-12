import sys

cmd_list = open("input.txt").read()

#head = [0,0]
rope = []
for i in range(10):
    rope.append([0,0])
print(len(rope),len(rope[0]))

tail_locations = {tuple(rope[-1])}
def segment_adjacent(seg):
    return seg == 0 or abs(rope[seg-1][0]-rope[seg][0]) <= 1 and abs(rope[seg-1][1] - rope[seg][1]) <= 1

def move_head(direction):
    if direction == "L":
        rope[0][0] -= 1
    elif direction == "R":
        rope[0][0] += 1
    elif direction == "U":
        rope[0][1] += 1
    elif direction == "D":
        rope[0][1] -= 1


def move_tail():
    for segment in range(len(rope)):
        if not segment_adjacent(segment):
            if rope[segment-1][0] - rope[segment][0] > 0:
                rope[segment][0] += 1
            elif rope[segment-1][0] - rope[segment][0] < 0:
                rope[segment][0] -= 1

            if rope[segment-1][1] - rope[segment][1] > 0:
                rope[segment][1] += 1
            elif rope[segment-1][1] - rope[segment][1] < 0:
                rope[segment][1] -= 1

for line in cmd_list.split("\n"):
    direction,count = line.split(" ")
    count = int(count)
    while count > 0:
        move_head(direction)
        move_tail()
        #print(rope)
        for segment in range(len(rope)):
            if not segment_adjacent(segment):
                print("ERROR! Head and tail out of alignment!")
                print(rope)
                sys.exit()
        tail_locations.add(tuple(rope[-1]))
        count -= 1

print(len(tail_locations))#,tail_locations)