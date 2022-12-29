import math,sys
import regex as re
from itertools import permutations

print_moves = False
valves = []

class Valve:
	def __init__(self,name,flow,connections):
		self.name = name
		self.flow = int(flow)
		self.connections = connections.strip().split(",")
		self.connections = list(map(lambda x:x.strip(),self.connections))
		#print(self.connections)
		self.edges = []
		self.roadsigns = {}
		self.distance = {}
		self.open = False

	def establish_connections(self,nodes):
		for edge in self.connections:
			#print(edge)
			for node in nodes:
				if node.name == edge:
					self.edges.append(node)
					#self.roadsigns[edge] = node
					#self.distance[edge] = 1
					break
		
	def find_quickest_route(self,node):
		path = Traveler(self).findBFS(node)
		if type(node) == str:
			at_node = valve_by_name(node)
		else:
			at_node = node
			node = node.name
		prev_node = None
		self.distance[node] = 0
		while at_node.name != self.name:
			self.distance[node] += 1
			for edge in path:
				if edge[1] == at_node:
					#print(edge[0].name,edge[1].name)
					at_node = edge[0]
					prev_node = edge[1]
					break
		self.roadsigns[node] = prev_node

	def find(self,node,path = []):
		path.append(self)
		for edge in self.edges:
			if edge not in path:
				pass

class Traveler:
	def __init__(self,start) -> None:
		self.queue = []
		self.node = None
		self.set_start(start)
		self.path = []
		self.time = 30
		self.total_pressure = 0
		self.valves = []
		self.dest = None

	def set_valves(self,valves):
		self.valves = valves

	def set_start(self,start):
		self.node = start
		if type(self.node) == str:
			self.node = valve_by_name(self.node)

	def open_valves_by_weight(self,valves):
		pass

	def weight_valves(self,valves):
		weights = {}
		for valve in valves:
			if valve != self.node:
				weights[valve] = valve.flow/self.node.distance[valve.name]
		return weights

	def open_valves_in_order(self,order = []):
		if order:
			self.valves = order
		if type(self.valves) != list:
			self.valves = list(self.valves)
		#print(get_names(self.valves))
		#print(self.node.name,self.dest,self.node.roadsigns.keys())
		while self.time > 0:
			self.total_pressure += release_pressure()
			open_valve = False
			move = False

			if not self.dest:
				if self.valves:
					self.dest = self.valves.pop(0)
					move = True
				elif not self.node.open:
					open_valve = True
			else:
				if self.node == self.dest:
					if self.node.open and self.valves:
						self.dest = self.valves.pop(0)
						move = True
					elif not self.node.open:
						open_valve = True

				else:
					move = True

			if open_valve and move:
				print("Error!")
				return
			elif open_valve:
				if print_moves:
					print(f"{self.time} minutes left. Open valve {self.node.name}. Release {release_pressure()}. Total pressure is {self.total_pressure}")
				self.node.open = True
			elif move:
				self.node = self.node.roadsigns[self.dest.name]
				if print_moves:
					print(f"{self.time} minutes left. Move to valve {self.node.name}. Destination {self.dest.name}. Release {release_pressure()}. Total pressure is {self.total_pressure}")

			else:
				if print_moves:
					print(f"{self.time} minutes left. Stay at valve {self.node.name}. Release {release_pressure()}. Total pressure is {self.total_pressure}")

			self.time -= 1
		close_valves()
		return self.total_pressure
			# if valves:
			# 	if not self.dest:
			# 		self.dest = self.valves.pop(0)
			# 		move = True
			# 	elif self.dest != self.node:
			# 		move = True
			# 	elif not self.node.open:
			# 		open_valve = True
			# elif self.dest and self.dest != self.node:
			# 	move = True
			# elif self.dest and self.node == self.dest and not self.node.open:
			# 	open_valve = True


	def queue_names(self):
		s = ""
		for node in self.queue:
			s += node.name + ", "
		return s

	def findBFS(self,node = None):
		self.queue.append(self.node)
		self.path.append(self.node)
		edges = set()
		while self.queue != []:
			#print(self.node.name,self)
			self.node = self.queue.pop(0)
			# if node and self.node.name == node:
			# 	return edges
			for edge in self.node.edges:
				if edge.name == node:
					edges.add((self.node,edge))
					return edges
				if edge not in self.path:
					self.queue.append(edge)
					self.path.append(edge)
					edges.add((self.node,edge))

		return edges

def get_names(nodes):
	s = ""
	for node in nodes:
		s += node.name+", "
	return s

def close_valves():
	for valve in valves:
		valve.open = False

def release_pressure():
	pressure = 0
	for valve in valves:
		if valve.open:
			pressure += valve.flow
	return pressure
		
def valve_by_name(name):
	for valve in valves:
		if valve.name == name:
			return valve

def sort_valves():
	ret = valves.copy()
	for valve in valves:
		#print(valve.name,valve.flow,type(valve.flow))
		if valve.flow == 0:
			#print("remove",valve.name)
			ret.remove(valve)
		
	return sorted(ret,key = lambda x:x.flow,reverse = True)

for line in open("test_input.txt").read().strip().split("\n"):
	m = re.search("Valve (?P<name>\w+) has flow rate=(?P<flow>\d+); tunnels? leads? to valves? (?P<connections>.+)",line)
	if m:
		valves.append(Valve(m.group("name"),m.group("flow"),m.group("connections")))

# for valve in valves:
# 	print("-",valve.name,valve.flow)
# t = Traveler("AA")
# t.set_valves(sort_valves())

# # for valve in valves:
# # 	print("+",valve.name,valve.flow)
# for valve in t.valves:
# 	print(valve.name,valve.flow)

for valve in valves:
	#print(valve.name,valve.flow,valve.connections)
	valve.establish_connections(valves)
	#print(valve.name,valve.flow,valve.edges)
	
# for edge in t.findBFS("CC"):
# 	print(edge[0].name,edge[1].name)
for node1 in valves:
	for node2 in valves:
		#print(node1.name,node2.name)
		if node1 != node2 and node2.name not in node1.roadsigns.keys():
			node1.find_quickest_route(node2)

# print(valve_by_name("AA").distance)
# for node in valves:
# 	if node.name == "DD":
# 		for name,path in node.roadsigns.items():
# 			print(name,path.name,node.distance[name])
for valve,weight in Traveler("AA").weight_valves(sort_valves()).items():
	print(valve.name,weight)


#sys.exit()
print(len(sort_valves()),math.factorial(len(sort_valves())))
all_permutations = permutations(sort_valves())

#print(len(list(all_permutations)))
greatest_total = 0
greatest_order = []
index = 0
for perm in all_permutations:
	total = Traveler("AA").open_valves_in_order(perm)
	if total > greatest_total:
		greatest_total = total
		greatest_order = perm
		print(total)

print_moves = True
Traveler("AA").open_valves_in_order(greatest_order)