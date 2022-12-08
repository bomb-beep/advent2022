forest = open("input.txt").read()
forest_map = []

def scenic_score(origin_tree):
	count = 0
	score = 1
	for tree in reversed(range(origin_tree[0])):
		count +=1
		if forest_map[tree][origin_tree[1]] >= forest_map[origin_tree[0]][origin_tree[1]]:
			#print(tree,"tree at {},{} with height {} blocks origin at {} with {}".format(tree,origin_tree[1],forest_map[tree][origin_tree[1]],origin_tree,forest_map[origin_tree[0]][origin_tree[1]]))
			break
	score *= count
	#print("score,count",score,count)
	count = 0

	for tree in range(origin_tree[0]+1,len(forest_map)):
		count +=1
		if forest_map[tree][origin_tree[1]] >= forest_map[origin_tree[0]][origin_tree[1]]:
			#print(tree,"tree at {},{} with height {} blocks origin at {} with {}".format(tree,origin_tree[1],forest_map[tree][origin_tree[1]],origin_tree,forest_map[origin_tree[0]][origin_tree[1]]))
			break
	score *= count
	#print("score,count",score,count)
	count = 0

	for tree in reversed(range(origin_tree[1])):
		count +=1
		if forest_map[origin_tree[0]][tree] >= forest_map[origin_tree[0]][origin_tree[1]]:
			#print(tree,"tree at {},{} with height {} blocks origin at {} with {}".format(origin_tree[0],tree,forest_map[origin_tree[0]][tree],origin_tree,forest_map[origin_tree[0]][origin_tree[1]]))
			break
	score *= count
	#print("score,count",score,count)
	count = 0

	for tree in range(origin_tree[1]+1,len(forest_map[0])):
		count +=1
		if forest_map[origin_tree[0]][tree] >= forest_map[origin_tree[0]][origin_tree[1]]:
			#print(tree,"tree at {},{} with height {} blocks origin at {} with {}".format(origin_tree[0],tree,forest_map[origin_tree[0]][tree],origin_tree,forest_map[origin_tree[0]][origin_tree[1]]))
			break
	score *= count
	#print("score,count",score,count)
	count = 0

	return score

for line in forest.split("\n"):
	row = []
	for char in line:
		row.append(int(char))
	forest_map.append(row)

#print(forest_map)
visible_trees = set()

for row in range(len(forest_map)):
	highest_tree = -1
	for col in range(len(forest_map[row])):
		if forest_map[row][col] > highest_tree:
			visible_trees.add((row,col))
			highest_tree = forest_map[row][col]
			if highest_tree == 9:
				break
	highest_tree = -1
	for col in reversed(range(len(forest_map[row]))):
		if forest_map[row][col] > highest_tree:
			visible_trees.add((row,col))
			highest_tree = forest_map[row][col]
			if highest_tree == 9:
				break

for col in range(len(forest_map[0])):
	highest_tree = -1
	for row in range(len(forest_map)):
		if forest_map[row][col] > highest_tree:
			visible_trees.add((row,col))
			highest_tree = forest_map[row][col]
			if highest_tree == 9:
				break
	highest_tree = -1
	for row in reversed(range(len(forest_map[0]))):
		if forest_map[row][col] > highest_tree:
			visible_trees.add((row,col))
			highest_tree = forest_map[row][col]
			if highest_tree == 9:
				break

print(len(forest_map),len(forest_map[0]))
print(len(visible_trees))

scores = []
for row in range(len(forest_map)):
	for col in range(len(forest_map[row])):
		#print("scenic score",(row,col),scenic_score((row,col)))
		scores.append(scenic_score((row,col)))

print(max(scores))