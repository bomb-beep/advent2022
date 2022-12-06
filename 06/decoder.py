text = open("input.txt").read()

index = 0

print(len(text))
print(text[index:index+4])
found = False

while not found and index+4 < len(text):
	found = True
	window = text[index:index+4]
	for char in window:
		if window.count(char) != 1:
			index += 1
			found = False
			break

print(index +4)
#print(text[:index+4])
#print(text[index+4:])
found = False
while not found and index+14 < len(text):
	found = True
	window = text[index:index+14]
	for char in window:
		if window.count(char) != 1:
			index += 1
			found = False
			break

print(index +14)	