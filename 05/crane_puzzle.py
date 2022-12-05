import regex as re

text = open("input.txt").read()

starting_pos,move_list = re.split("\n\n",text)

print(starting_pos)
print("blank space here separator!")
#print(move_list)
cargo = {

}
indexes = {

}
#print(list(re.finditer("\s*\[([A-Z])\]\s*",starting_pos)))
starting_pos = starting_pos.split("\n")
#print(list(re.finditer("\s*(\d+)\s*",starting_pos))[0].group(1))
#print(list(range(len(starting_pos)-1,0)))
for line in reversed(starting_pos):
	print(list(re.finditer("\s*(\d+)\s*",line)))
	print(list(re.finditer("\s*\[(\[A-Z])\]\s*",line)))
	for match in re.finditer("\s*(\d+)\s*",line):
		if match:
			#print(match.group(1)+"|")
			cargo[int(match.group(1))] = []#[match.start(1)]
			indexes[match.start(1)] = int(match.group(1))
	for match in re.finditer("\s*\[([A-Z])\]\s*",line):
		if match:
			cargo[indexes[match.start(1)]].append(match.group(1))

print(cargo)
print(indexes)