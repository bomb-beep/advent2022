import regex as re

debug = False

class BinaryTree:
	def __init__(self,value) -> None:
		self.value = value
		self.left = None
		self.right = None

	def insert(self,value):
		r = compare(value,self.value)
		if r == -1:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BinaryTree(value)

		elif r == 1:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BinaryTree(value)

	def list(self):
		r = []
		if self.left:
			r += self.left.list()
		r.append(self.value)
		if self.right:
			r += self.right.list()
		return r

def parse_packet(raw_packet):
	# if not raw_packet:
	# 	return None
	packet = []
	bracket_index = raw_packet.find("[")
	#print(raw_packet,bracket_index)
	if bracket_index == -1:
		for num in raw_packet.split(","):
			#print(num)
			if num:
				packet.append(int(num))
		#print(raw_packet.find("["))
		
	elif bracket_index == 0:
		open_brackets = 0
		for index in range(len(raw_packet)):
			if raw_packet[index] == "[":
				if open_brackets == 0:
					bracket_index = index
				open_brackets += 1
			elif raw_packet[index] == "]":
				open_brackets -= 1
				if open_brackets == 0:
					#print(raw_packet, index,len(raw_packet))
					#tail = parse_packet(raw_packet[index+1:])
					#print(bracket_index,index,raw_packet[bracket_index+1:index])
					packet.append(parse_packet(raw_packet[bracket_index+1:index]))
			if "]" not in raw_packet[index:] and index < len(raw_packet) -1:
				packet += parse_packet(raw_packet[index:])
				break

	else:
		packet += parse_packet(raw_packet[:bracket_index]) + parse_packet(raw_packet[bracket_index:])
		#print(packet)
		#print(raw_packet)
		
	
	return packet

def compare(left,right):
	if debug:
		print("enter compare",left,right)
	result = 0
	for i in range(len(left)):
		#print("i",i)
		try:
			right[i]
		except IndexError:
			result = 1
			break

		if type(left[i]) == int and type(right[i])== int:
			if debug:
				print("compare int",left[i],right[i])
			if left[i] < right[i]:
				result = -1
			elif left[i] > right[i]:
				result = 1

		elif type(left[i]) == list and type(right[i]) == list:
			if debug:
				print("compare list",left[i],right[i])
			result = compare(left[i],right[i])

		elif type(left[i]) == int:
			if debug:
				print("compare int list",left[i],right[i])
			result = compare([left[i]],right[i])
		
		elif type(right[i]) == int:
			if debug:
				print("compare list int",left[i],right[i])
			result = compare(left[i],[right[i]])
		if result:
			break
	if not result and len(left) < len(right):
		result = -1

	return result
	# m = re.search("(?P<head>[\d,]*)\[(?P<body>[\d,\[\]]*)\](?P<tail>[\d,\[\]]*)",raw_packet)
	# if m:
	# 	print("head {} body {} tail {}".format(m.group("head"),m.group("body"),m.group("tail")))
	# 	if m.group("head"):
	# 		packet += parse_packet(m.group("head"))
	# 	if m.group("body"):
	# 		packet += parse_packet(m.group("body"))
	# 	if m.group("tail"):
	# 		packet += parse_packet(m.group("tail"))
	# else:
	# 	for num in raw_packet.split(","):
	# 		print("num",num,raw_packet)
	# 		packet.append(int(num))

	# return packet
		#return raw_packet[m.start():m.end()]
	# while raw_packet[0] != "[":
	# 	print(raw_packet)#[:raw_packet.find(",")])
	# 	m = re.search(",|[",raw_packet)
	# 	if m:
	# 		packet.append(int(raw_packet[:m.start()]))
	# 		raw_packet = raw_packet[m.end():]
	# 	else:
	# 		packet.append(int(raw_packet))
	# while raw_packet[0] == "[":
	# 	closeing_index = list(re.finditer("]",raw_packet))#len(raw_packet) - list(reversed(raw_packet)).index("]")
	# 	tail = raw_packet[closeing_index:]
	# 	raw_packet = raw_packet[1:closeing_index-1]
	# 	packet += [parse_packet(raw_packet)] + parse_packet(tail)
	# return packet	


packets = {}
#packets = "[[1],[2,3,4]]\n[[1],4]"
packet_list = []#[[[2]],[[6]]]
test_packet = ["[9]\n[[8,7,6]]"]#["[[1],[2,3,4]]\n[[1],4]"]
index = 1

for pair in open("input.txt").read().split("\n\n"):
	#print(">",pair)
	left,right = pair.split("\n")
	#print(parse_packet(left)[0],parse_packet(right)[0])
	packets[index] = (parse_packet(left)[0],parse_packet(right)[0])
	packet_list += list(packets[index])
	index += 1

tree = BinaryTree([[2]])
tree.insert([[6]])
for packet in packet_list:
	tree.insert(packet)

sorted_packets = tree.list()
decoder_key = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
#print(tree.list())
# for leaf in tree.list():
# 	print(leaf)

total = 0
for index,(left,right) in packets.items():
	if compare(left,right) == -1:
		total += index
print(total)

print(decoder_key)