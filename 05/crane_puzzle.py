import regex as re


text = open("input.txt").read()

starting_pos,move_list = re.split("\n\n",text)

print(starting_pos)
print("blank space here separator!")
cargo = {

}
indexes = {

}

def move_crates(source,dest,num):
	while num > 0:
		cargo[dest].append(cargo[source].pop())
		num -= 1

def move_crates_bulk(source,dest,num):
	index = len(cargo[source])-num
	crane = cargo[source][index:]
	cargo[source] = cargo[source][:index]
	cargo[dest].extend(crane)

starting_pos = starting_pos.split("\n")
for line in reversed(starting_pos):
	for match in re.finditer("\s*(\d+)\s*",line):
		if match:
			cargo[int(match.group(1))] = []
			indexes[match.start(1)] = int(match.group(1))
	for match in re.finditer("\s*\[([A-Z])\]\s*",line):
		if match:
			cargo[indexes[match.start(1)]].append(match.group(1))

print(cargo)
print(indexes)
total_crates = 0
for stack in cargo.values():
	total_crates += len(stack)
print(total_crates)


for line in move_list.split("\n"):
	match = re.search("move (?P<number>\d+) from (?P<source>\d) to (?P<dest>\d)",line)
	if match:
		try:
			move_crates_bulk(int(match.group("source")),int(match.group("dest")),int(match.group("number")))
		except IndexError:
			print(match.string)
			print(cargo)


print(cargo)
total_crates = 0
for stack in cargo.values():
	total_crates += len(stack)
print(total_crates)

final_arrangement = ""
for stack in range(1,10):
	if cargo[stack]:
		final_arrangement += cargo[stack][-1]
	else:
		final_arrangement += " "
print(final_arrangement)