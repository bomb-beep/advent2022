import regex as re
import sys

class Directory:
	def __init__(self,name,superdirectory):
		self.name = name
		self.superdirectory = superdirectory
		self.dept = 0 if not superdirectory else superdirectory.dept +1

		self.subdirectories = []
		self.files = []

	def mkdir(self,name):
		if self.finddir(name):
			print("Duplicate directory!!!")
			sys.exit()
		self.subdirectories.append(Directory(name,self))
		return self.finddir(name)

	def finddir(self,name):
		for dir in self.subdirectories:
			if dir.name == name:
				return dir
		return None

	def mkfile(self,size,name):
		if name in [file[1] for file in self.files]:
			print("Duplicate file!!!")
			sys.exit()
		self.files.append((size,name))

	def directory_size(self):
		total_size = 0
		for size,name in self.files:
			total_size += size
			spacing = " "
			print(spacing * (self.dept+1)+f"{name} (file, size={size})")
		for directory in self.subdirectories:
			total_size += directory.directory_size()
		spacing = " " * self.dept
		print(spacing+f"{self.name} (dir, size={total_size})")
		directories.append((self.name,total_size))
		return total_size

main_directory = Directory("/",None)
directories = []
current_directory = None

def parse_command(command:str):
	global current_directory
	command = command.strip().split(" ")
	if command[0] == "cd":
		if command[1] == "/":
			current_directory = main_directory
		elif command[1] == "..":
			current_directory = current_directory.superdirectory
		else:
			current_directory = current_directory.finddir(command[1])
		print(current_directory)

def parse_directory(dir:str):
	global current_directory,dicretory
	dir = dir.strip()
	newdir = current_directory.mkdir(dir)

def parse_file(size,name):
	global current_directory
	current_directory.mkfile(int(size),name.strip())

promt = open("input.txt").read().split("\n")

for line in promt:
	m = re.search("^(?P<cmd>\$)(?P<args>.*)|(?P<dir>dir)(?P<args>.*)|(?P<file>\d+)(?P<args>.*)",line)
	if m and m.group("cmd"):
		print("cmd",m.group("cmd"),m.group("args"))
		parse_command(m.group("args"))
	elif m and m.group("dir"):
		print("dir",m.group("dir"),m.group("args"))
		parse_directory(m.group("args"))
	elif m and m.group("file"):
		print("file",m.group("file"),m.group("args"))
		parse_file(m.group("file"),m.group("args"))


free_space = 70000000 - main_directory.directory_size()
total = 0
for name,size in directories:
	if size <= 100000:
		total += size
		print(name,size)

print("Total:",total)

large_enough_dirs = []
for name,size in directories:
	if free_space + size > 30000000:
		large_enough_dirs.append((name,size))

large_enough_dirs = sorted(large_enough_dirs,key=lambda x:x[1])
print(large_enough_dirs[0],large_enough_dirs[-1])