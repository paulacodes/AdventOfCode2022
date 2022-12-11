def part1():
	with open('inputs/day11.txt') as f:
		lines = f.readlines()
	items_per_monkey = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
	monkey_inspections = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
	for round_index in range(20):
		line_index = 0
		while(line_index < len(lines)):
			line = lines[line_index].rstrip()
			if "Monkey" in line:
				monkey_index = int(line.split(" ")[1][:-1])
				starting_items = []
				for monkey_line_index in range(line_index+1,line_index+6):
					line = lines[monkey_line_index].rstrip()
					if "Starting items:" in line and round_index == 0:
						starting_items = [int (i) for i in line.split(": ")[1].split(", ")]
						for item in items_per_monkey[monkey_index]:
							starting_items.append(item)
						items_per_monkey[monkey_index] = starting_items.copy()
					elif "Starting items:" in line and round_index > 0:
						for item in items_per_monkey[monkey_index]:
							starting_items.append(item)
					if "Operation:" in line:
						operation = line.split("= ")[1]
						values = operation.split(" ")
					if "Test:" in line:
						divisible_by = int(line.split("by ")[1])
					if "true:" in line:
						throw_to_if_true = int(line.split("monkey ")[1])
					if "false:" in line:
						throw_to_if_false = int(line.split("monkey ")[1])
				for item in range(len(starting_items)):
					monkey_inspections[monkey_index] += 1
					new_values = values.copy()
					# perform operation on items
					if new_values[0] == "old":
						new_values[0] = starting_items[item]
					else :
						new_values[0] = int(new_values[0])
					if new_values[2] == "old":
						new_values[2] = starting_items[item]
					else:
						new_values[2] = int(new_values[2])
					if new_values[1] == "*":
						starting_items[item] = new_values[0]*new_values[2]
					else:
						starting_items[item] = new_values[0]+new_values[2]
					# divide worry levels of items
					starting_items[item] = int(starting_items[item]/3)
					# check if divisible by test item and throw to monkey
					if starting_items[item]%divisible_by == 0:
						items_per_monkey[throw_to_if_true].append(starting_items[item])
						items_per_monkey[monkey_index].pop()
					else:
						items_per_monkey[throw_to_if_false].append(starting_items[item])
						items_per_monkey[monkey_index].pop()
			line_index += 1
	list_of_inspections = []
	for monkey in monkey_inspections:
		list_of_inspections.append(monkey_inspections[monkey])
	list_of_inspections.sort()
	print(list_of_inspections[-1]*list_of_inspections[-2])

def part2():
	with open('inputs/day11.txt') as f:
		lines = f.readlines()
	items_per_monkey = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
	monkey_inspections = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
	div_product = 1
	line_index = 0
	for line in lines:
		if "Test:" in line:
			divisible_by = int(line.split("by ")[1])
			div_product *= divisible_by
	for round_index in range(10000):
		line_index = 0
		while(line_index < len(lines)):
			line = lines[line_index].rstrip()
			if "Monkey" in line:
				monkey_index = int(line.split(" ")[1][:-1])
				starting_items = []
				for monkey_line_index in range(line_index+1,line_index+6):
					line = lines[monkey_line_index].rstrip()
					if "Starting items:" in line and round_index == 0:
						starting_items = [int (i) for i in line.split(": ")[1].split(", ")]
						for item in items_per_monkey[monkey_index]:
							starting_items.append(item)
						items_per_monkey[monkey_index] = starting_items.copy()
					elif "Starting items:" in line and round_index > 0:
						for item in items_per_monkey[monkey_index]:
							starting_items.append(item)
					if "Operation:" in line:
						operation = line.split("= ")[1]
						values = operation.split(" ")
					if "Test:" in line:
						divisible_by = int(line.split("by ")[1])
					if "true:" in line:
						throw_to_if_true = int(line.split("monkey ")[1])
					if "false:" in line:
						throw_to_if_false = int(line.split("monkey ")[1])
				for item in range(len(starting_items)):
					monkey_inspections[monkey_index] += 1
					new_values = values.copy()
					# perform operation on items
					if new_values[0] == "old":
						new_values[0] = starting_items[item]
					else :
						new_values[0] = int(new_values[0])
					if new_values[2] == "old":
						new_values[2] = starting_items[item]
					else:
						new_values[2] = int(new_values[2])
					if new_values[1] == "*":
						starting_items[item] = new_values[0]*new_values[2]
					else:
						starting_items[item] = new_values[0]+new_values[2]
					# no the smaller numbers that result from using the following congruency rule are perfect, the large ones scare me
					starting_items[item] %= div_product
					# check if divisible by test item and throw to monkey
					if starting_items[item]%divisible_by == 0:
						items_per_monkey[throw_to_if_true].append(starting_items[item])
						items_per_monkey[monkey_index].pop()
					else:
						items_per_monkey[throw_to_if_false].append(starting_items[item])
						items_per_monkey[monkey_index].pop()
			line_index += 1
	list_of_inspections = []
	for monkey in monkey_inspections:
		list_of_inspections.append(monkey_inspections[monkey])
	list_of_inspections.sort()
	print(list_of_inspections[-1]*list_of_inspections[-2])

part1()
part2()