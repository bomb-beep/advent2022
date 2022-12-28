import regex as re

valves = []

class Valve:
	def __init__(self,name,flow,connections):
		self.name = name
		self.flow = flow
		self.connections = connections.strip().split(",")
		self.connections = list(map(lambda x:x.strip(),self.connections))
		#print(self.connections)
		self.edges = []
		self.roadsigns = {}

	def establish_connections(self,nodes):
		for edge in self.connections:
			#print(edge)
			for node in nodes:
				if node.name == edge:
					self.edges.append(node)
					self.roadsigns[edge] = node
					break
		
	def find_quickest_route(self,node):
		path = Traveler(self).findBFS(node)
		at_node = node
		prev_node = None
		while at_node != self.name:
			for edge in path:
				if edge[1].name == at_node:
					print(edge[0].name,edge[1].name)
					at_node = edge[0].name
					prev_node = edge[1]
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

	def set_start(self,start):
		self.node = start
		if type(self.node) == str:
			for node in valves:
				if self.node == node.name:
					self.node = node
					break

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


for line in open("test_input.txt").read().strip().split("\n"):
	m = re.search("Valve (?P<name>\w+) has flow rate=(?P<flow>\d+); tunnels? leads? to valves? (?P<connections>.+)",line)
	if m:
		valves.append(Valve(m.group("name"),m.group("flow"),m.group("connections")))

t = Traveler("AA")
for valve in valves:
	#print(valve.name,valve.flow,valve.connections)
	valve.establish_connections(valves)
	print(valve.name,valve.flow,valve.edges)
	
# for edge in t.findBFS("CC"):
# 	print(edge[0].name,edge[1].name)
for node1 in valves:
	for node2 in valves:
		print(node1.name,node2.name)
		if node1 != node2 and node2.name not in node1.roadsigns.keys():
			node1.find_quickest_route(node2)

for node in valves:
	if node.name == "AA":
		for name,path in node.roadsigns.items():
			print(name,path.name)