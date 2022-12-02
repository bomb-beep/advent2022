rps_guide = open("input.txt").read().lower()

rps_points = {
    "x":1,
    "y":2,
    "z":3,
    "a":1,
    "b":2,
    "c":3
}
rps_score = {
    ("x","a"):4,
    ("x","b"):1,
    ("x","c"):7,
    ("y","a"):8,
    ("y","b"):5,
    ("y","c"):2,
    ("z","a"):3,
    ("z","b"):9,
    ("z","c"):6,
}

correct_rps_score = {
    ("x","a"):3,
    ("x","b"):1,
    ("x","c"):2,
    ("y","a"):4,
    ("y","b"):5,
    ("y","c"):6,
    ("z","a"):8,
    ("z","b"):9,
    ("z","c"):7,
}

def rps(own,elf):
    points = rps_points[own]
    if own == "x":
        if elf == "a":
            points += 3

points = 0

for line in rps_guide.split("\n"):
    if line != "":
        elf,own = line.split(" ")
        points += rps_score[(own,elf)]
print(points)

points = 0

for line in rps_guide.split("\n"):
    if line != "":
        elf,own = line.split(" ")
        points += correct_rps_score[(own,elf)]
print(points)