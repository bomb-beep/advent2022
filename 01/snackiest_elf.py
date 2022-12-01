import sys

inventory = open(sys.argv[1],"r").read() if len(sys.argv) > 1 else open("input.txt","r").read()
elves = [0]

for line in inventory.split("\n"):
	if line == "":
		elves.append(0)
	else:
		elves[-1] += int(line)

print("The elf at position {} has the most calories with {}cal".format(elves.index(max(elves)) +1,max(elves)))

elves.sort()
print("The three elves with the most calories have {} in total".format(sum(elves[-3:])))