import regex as re

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
index = 1

for pair in open("test_input.txt").read().split("\n\n"):
	#print(">",pair)
	left,right = pair.split("\n")
	#print(parse_packet(left)[0],parse_packet(right)[0])
	packets[index] = (parse_packet(left)[0],parse_packet(right)[0])
	index += 1

print(packets)