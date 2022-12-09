# goblin mode part 1 without objects, did not bother refactoring to the more elegant part 2 approach
def part1():
	with open('inputs/day9.txt') as f:
		lines = f.readlines()
	f.close()
	motions = [] 
	for line in lines:
		motions.append(line.rstrip().split(" "))
	current_position_of_head = [0,0]
	current_position_of_tail = [0,0]
	visited_spots_tail = []
	for i in range(len(motions)):
		direction,steps = motions[i]
		if i<=len(motions)-2:
			next_direction = motions[i+1][0]
		else:
			next_direction = "I"
		steps = int(steps)
		if direction == "R":
			for step in range(0,steps):
				current_position_of_head[1] += 1
				if not(abs(current_position_of_head[0]-current_position_of_tail[0]) <= 1 and abs(current_position_of_head[1]-current_position_of_tail[1]) <= 1):
					current_position_of_tail = [current_position_of_head[0], current_position_of_head[1]-1]
					if current_position_of_tail not in visited_spots_tail:
						visited_spots_tail.append(current_position_of_tail.copy())
		elif direction == "L":
			for step in range(0,steps):
				current_position_of_head[1] -= 1
				if not(abs(current_position_of_head[0]-current_position_of_tail[0]) <= 1 and abs(current_position_of_head[1]-current_position_of_tail[1]) <= 1):
					current_position_of_tail = [current_position_of_head[0], current_position_of_head[1]+1]
					if current_position_of_tail not in visited_spots_tail:
						visited_spots_tail.append(current_position_of_tail.copy())
		elif direction == "U":
			for step in range(0,steps):
				current_position_of_head[0] += 1
				if not(abs(current_position_of_head[0]-current_position_of_tail[0]) <= 1 and abs(current_position_of_head[1]-current_position_of_tail[1]) <= 1):
					current_position_of_tail = [current_position_of_head[0]-1, current_position_of_head[1]]
					if current_position_of_tail not in visited_spots_tail:
						visited_spots_tail.append(current_position_of_tail.copy())
		elif direction == "D":
			for step in range(0,steps):
				current_position_of_head[0] -= 1
				if not(abs(current_position_of_head[0]-current_position_of_tail[0]) <= 1 and abs(current_position_of_head[1]-current_position_of_tail[1]) <= 1):
					current_position_of_tail = [current_position_of_head[0]+1, current_position_of_head[1]]
					if current_position_of_tail not in visited_spots_tail:
						visited_spots_tail.append(current_position_of_tail.copy())
	print(len(visited_spots_tail))


class Node:
	def __init__(self,i,j):
		self.i = i
		self.j = j
		self.prev_i = i
		self.prev_j = j
	def move_based_on_neighbor_node(self,other):
		self.prev_i = self.i
		self.prev_j = self.j
		if abs(self.i -  other.i) >= 2 or abs(self.j-other.j) >= 2:
			if self.i != other.i:
				self.i += 1 if self.i <= other.i else -1
			if self.j != other.j:
				self.j += 1 if self.j <= other.j else -1
		if self.i - other.i == -2:
			self.i += 1
		if self.i -  other.i == 2:
			self.i -= 1
		if self.j - other.j == -2:
			self.j += 1
		if self.j - other.j == 2:
			self.j -= 1

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
			head_node.prev_i = head_node.i
			head_node.prev_j= head_node.j
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