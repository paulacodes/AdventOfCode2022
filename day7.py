folder_items = {}
folder_sums = {}

def part1():
	get_folder_items()
	total_sum = 0
	for folder in folder_items:
		folder_sum = 0
		for item in folder_items[folder]:
			if isinstance(item, list):
				folder_sum += int(item[0])
			else:
				if item in folder_sums:
					folder_sum += folder_sums[item]
				else:
					current_item_sum = get_sum_of_folder(item)
					folder_sums[item] = current_item_sum
					folder_sum += current_item_sum
		if folder_sum <= 100000:
			total_sum += folder_sum

	print(total_sum)

def part2():
	global folder_items
	folder_items = {}
	global folder_sums
	folder_sums = {}
	get_folder_items()
	for folder in folder_items:
		folder_sum = 0
		for item in folder_items[folder]:
			if isinstance(item, list):
				folder_sum += int(item[0])
			else:
				if item in folder_sums:
					folder_sum += folder_sums[item]
				else:
					current_item_sum = get_sum_of_folder(item)
					folder_sums[item] = current_item_sum
					folder_sum += current_item_sum
	sum_to_delete = 30000000 - (70000000 - get_sum_of_folder("/"))
	folder_differences = []
	for folder in folder_sums:
		if folder != "/":
			if sum_to_delete <= folder_sums[folder]:
				difference = folder_sums[folder] - sum_to_delete
				folder_differences.append(difference)
	folder_differences.sort()

	print(folder_differences[0]+sum_to_delete)

def get_folder_items():
	with open('inputs/day7.txt') as f:
		lines = f.readlines()
		line_index = 0
		while line_index < len(lines):
			output_line = lines[line_index].rstrip()
			if output_line[0:4] == "$ cd":
				if output_line == "$ cd /":
					current_folder_name = "/"
				elif output_line == "$ cd ..":
					for item in folder_items:
						for subitem in folder_items[item]:
							if subitem == current_folder_name:
								current_folder_name = item
				else:
					current_folder_name = current_folder_name+"."+output_line[5:len(output_line)]
				line_index += 1
			elif output_line == "$ ls":
				line_index = line_index + 1
				while lines[line_index][0] != "$":
					output_line = lines[line_index].rstrip()
					if output_line[0:3] == "dir":
						folder_name = current_folder_name+"."+output_line[4:len(output_line)]
						if current_folder_name in folder_items:
							folder_items[current_folder_name].append(folder_name)
						else:
							folder_items[current_folder_name] = [folder_name]
					else:
						value,file_name = output_line.split(" ")
						if current_folder_name in folder_items:
							folder_items[current_folder_name].append([value, file_name])
						else:
							folder_items[current_folder_name] = [[value,file_name]]
					line_index = line_index + 1
					if line_index >= len(lines):
						break
	f.close()

def get_sum_of_folder(folder):
	folder_sum = 0
	for item in folder_items[folder]:
		if isinstance(item, list):
			folder_sum += int(item[0])
		else:
			if item in folder_sums:
				folder_sum += folder_sums[item]
			else:
				current_item_sum = get_sum_of_folder(item)
				folder_sums[item] = current_item_sum
				folder_sum += current_item_sum
	return folder_sum

part1()
part2()