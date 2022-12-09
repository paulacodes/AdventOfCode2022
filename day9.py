class Node:
	def __init__(self,i,j):
		self.i = i
		self.j = j
	def move_based_on_neighbor_node(self,other):
		if abs(self.i -  other.i) >= 2 or abs(self.j-other.j) >= 2:
			if self.i != other.i:
				self.i += 1 if self.i <= other.i else -1
			if self.j != other.j:
				self.j += 1 if self.j <= other.j else -1

def part1():
	with open('inputs/day9.txt') as f:
		lines = f.readlines()
	f.close()
	motions = [] 
	for line in lines:
		motions.append(line.rstrip().split(" "))
	tail_node = Node(0,0)
	head_node = Node(0,0)
	visited_spots_tail_node = []
	for i in range(len(motions)):
		direction,steps = motions[i]
		steps = int(steps)
		for step in range(0,steps):
			if direction == "R":
				head_node.i += 1
			elif direction == "L":
				head_node.i -= 1
			elif direction == "U":
				head_node.j += 1
			elif direction == "D":
				head_node.j -= 1
			tail_node.move_based_on_neighbor_node(head_node)
			if [tail_node.i, tail_node.j] not in visited_spots_tail_node:
				visited_spots_tail_node.append([tail_node.i, tail_node.j])
	print(len(visited_spots_tail_node))

def part2():
	with open('inputs/day9.txt') as f:
		lines = f.readlines()
	f.close()
	motions = [] 
	for line in lines:
		motions.append(line.rstrip().split(" "))
	tail_nodes = []
	head_node = Node(0,0)
	for i in range(9):
		tail_nodes.append(Node(0,0))
	visited_spots_last_tail_node = []
	for i in range(len(motions)):
		direction,steps = motions[i]
		steps = int(steps)
		for step in range(0,steps):
			if direction == "R":
				head_node.i += 1
			elif direction == "L":
				head_node.i -= 1
			elif direction == "U":
				head_node.j += 1
			elif direction == "D":
				head_node.j -= 1
			tail_nodes[0].move_based_on_neighbor_node(head_node)
			previous_node = tail_nodes[0]
			for node in tail_nodes[1:]:
				node.move_based_on_neighbor_node(previous_node)
				previous_node = node
			if [tail_nodes[-1].i, tail_nodes[-1].j] not in visited_spots_last_tail_node:
				visited_spots_last_tail_node.append([tail_nodes[-1].i, tail_nodes[-1].j])
	print(len(visited_spots_last_tail_node))
		
part1()
part2()