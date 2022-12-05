def read_stacks_and_instructions():
	with open('inputs/day5.txt') as f:
		stacks = {}
		instruction_list = []
		for line in f:
			if "[" in line:
				crates_on_row = line.rstrip()	
				row_index = 0
				stack_index = 1
				while row_index < len(crates_on_row):
					if crates_on_row[row_index] == "[":
						if stack_index not in stacks:
							stacks[stack_index] = []
						stacks[stack_index].append(crates_on_row[row_index+1])
					stack_index += 1
					row_index += 4
			if "move" in line:
				instructions = line.rstrip()
				stacks_to_move = int(instructions.split(" from")[0].split(" ")[1])
				from_stack, to_stack = instructions.split("from ")[1].split(" to ")
				from_stack = int(from_stack)
				to_stack = int(to_stack)
				instruction_list.append([stacks_to_move, [from_stack, to_stack]])
		for stack in stacks:
			list_to_reverse = stacks[stack]
			list_to_reverse.reverse()
			stacks[stack] = list_to_reverse
	f.close()
	return stacks, instruction_list

def part1():
	stacks, instruction_list = read_stacks_and_instructions()
	for instruction in instruction_list:
		from_stack = instruction[1][0]
		to_stack = instruction[1][1]
		for i in range(instruction[0]):
			last_stack = stacks[from_stack][-1]
			stacks[from_stack].pop()
			stacks[to_stack].append(last_stack)
	message = ""
	for stack in stacks:
		message += stacks[stack][-1]
	print(message)

def part2():
	stacks, instruction_list = read_stacks_and_instructions()
	for instruction in instruction_list:
		from_stack = instruction[1][0]
		to_stack = instruction[1][1]
		for i in range(instruction[0]):
			last_stack = stacks[from_stack][-instruction[0]+i]
			stacks[from_stack].pop(-instruction[0]+i)
			stacks[to_stack].append(last_stack)
	message = ""
	for stack in stacks:
		message += stacks[stack][-1]
	print(message)

part1()
part2()