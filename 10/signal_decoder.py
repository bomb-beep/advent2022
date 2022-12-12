import sys
import regex as re

instr_list = open("input.txt").read().split("\n")
index = 0
x = 1
cycle = 0
cycles_remaining = 0
instr = None
args = None

signal_start = 20
signal_step = 40
total_strength = 0

display = ""
def get_command():
	global index,instr,args,cycles_remaining
	try:
		new_instr = instr_list[index]
	except IndexError:
		return -1
	index += 1 
	match = re.search("^(?P<instr>\w+)\s*(?P<args>-?\w*)",new_instr)
	if match and match.group("instr") == "noop":
		instr = noop
		cycles_remaining = 1
	elif match and match.group("instr") == "addx":
		instr = addx
		args = match.group("args")
		cycles_remaining = 2

def addx(v):
	global x
	x += int(v)

def noop(any=None):
	pass

def signal_strength():
	return cycle * x

def render_screen():
	global display
	#print(cycle,cycle%signal_step,x)
	s = f"{cycle}, {cycle%signal_step}, {x}, "
	if cycle % signal_step in range(x-1,x+2):
		display += "#"
		s += "#"
	else:
		display += "."
		s += "."
	print(s)

#print(instr_list)
while True:
	if cycle % signal_step == signal_start:
		print(f"signal strength {signal_strength()} at cycle {cycle} with reg {x}")
		total_strength += signal_strength()
	if cycles_remaining > 0:
		pass
	else:
		if instr:
			instr(args)
		instr = None
		args = None

		if get_command() == -1:
			break

	#print(cycle,instr,args,cycles_remaining,x)
	render_screen()
	cycles_remaining -= 1
	cycle += 1
	if cycle % signal_step == 0:
		display += "\n"

print(total_strength)
print(display)