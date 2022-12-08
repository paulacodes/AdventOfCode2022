import numpy as np
from collections import Counter

def part1():
	with open('inputs/day8.txt') as f:
		lines = f.readlines()
	f.close()
	tree_matrix = []
	for l in lines:
		tree_matrix.append(list(int(x) for x in list(l.rstrip())))
	tree_matrix = np.array(tree_matrix)
	transposed_matrix =	tree_matrix.transpose()
	visible_trees = set()
	for i,row in enumerate(tree_matrix):
		for j,col in enumerate(row):
			if i in [0,len(tree_matrix)-1] or j in[0,len(row)-1] or (max(row[:j]) < col or max(row[j+1:])<col):
				visible_trees.add((i,j))
	for i,row in enumerate(transposed_matrix):
		for j,col in enumerate(row):
			if i in [0,len(transposed_matrix)-1] or j in[0,len(row)-1] or (max(row[:j]) < col or max(row[j+1:])<col):
				visible_trees.add((j,i))
	print(len(visible_trees))

def part2():
	with open('inputs/day8.txt') as f:
		lines = f.readlines()
	f.close()
	tree_matrix = []
	for l in lines:
		tree_matrix.append(list(int(x) for x in list(l.rstrip())))
	tree_matrix = np.array(tree_matrix)
	transposed_matrix =	tree_matrix.transpose()
	visible_trees_down = Counter()
	visible_trees_up = Counter()
	visible_trees_left = Counter()
	visible_trees_right = Counter()
	for i,row in enumerate(tree_matrix):
		for j,col in enumerate(row):
			visible_trees_left[(i,j)] = 0
			visible_trees_right[(i,j)] = 0
			if i in [0,len(tree_matrix)-1] or j in[0,len(row)-1]:
				continue
			
			trees_to_left = list(reversed(row[:j]))
			found_tree = False
			for index,tree in enumerate(trees_to_left):
				if tree >= col:
					visible_trees_left[(i,j)] = index + 1
					found_tree = True
					break
			if not found_tree:
				visible_trees_left[(i,j)] = len(trees_to_left)

			trees_to_right = row[j+1:]
			found_tree = False
			for index,tree in enumerate(trees_to_right):
				if tree >= col:
					visible_trees_right[(i,j)] = index + 1
					found_tree = True
					break
			if not found_tree:
				visible_trees_right[(i,j)] = len(trees_to_right)
	
	for i,row in enumerate(transposed_matrix):
		for j,col in enumerate(row):
			visible_trees_up[(j,i)] = 0
			visible_trees_down[(j,i)] = 0
			if i in [0,len(tree_matrix)-1] or j in[0,len(row)-1]:
				continue
			
			trees_to_up = list(reversed(row[:j]))
			found_tree = False
			for index,tree in enumerate(trees_to_up):
				if tree >= col:
					visible_trees_up[(j,i)] = index + 1
					found_tree = True
					break
			if not found_tree:
				visible_trees_up[(j,i)] = len(trees_to_up)

			trees_to_down = row[j+1:]
			found_tree = False
			for index,tree in enumerate(trees_to_down):
				if tree >= col:
					visible_trees_down[(j,i)] = index + 1
					found_tree = True
					break
			if not found_tree:
				visible_trees_down[(j,i)] = len(trees_to_down)
	
	max_score = 0
	for i in range(len(tree_matrix)):
		row = ""
		for j in range(len(tree_matrix)):
			scenic_score = visible_trees_up[(i,j)]*visible_trees_down[(i,j)]*visible_trees_left[(i,j)]*visible_trees_right[(i,j)]
			row += str(scenic_score) + " "
			max_score = max(max_score,scenic_score)
	print(max_score)

part1()
part2()
