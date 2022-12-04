def part1():
	with open('inputs/day4.txt') as f:
		valid_pairs = 0
		for line in f:
			pairs = line.rstrip()
			first_elf = pairs.split(",")[0]
			second_elf = pairs.split(",")[1]
			first_elf_first_num = int(first_elf.split("-")[0])
			first_elf_second_num = int(first_elf.split("-")[1])
			second_elf_first_num = int(second_elf.split("-")[0])
			second_elf_second_num = int(second_elf.split("-")[1])
			if (first_elf_first_num >= second_elf_first_num and first_elf_second_num <= second_elf_second_num) or (second_elf_first_num >= first_elf_first_num and second_elf_second_num <= first_elf_second_num):
				valid_pairs += 1
		print(valid_pairs)
	f.close()

def part2():
	with open('inputs/day4.txt') as f:
		valid_pairs = 0
		for line in f:
			pairs = line.rstrip()
			first_elf = pairs.split(",")[0]
			second_elf = pairs.split(",")[1]
			first_elf_first_num = int(first_elf.split("-")[0])
			first_elf_second_num = int(first_elf.split("-")[1])
			second_elf_first_num = int(second_elf.split("-")[0])
			second_elf_second_num = int(second_elf.split("-")[1])
			first_elf_range = range(first_elf_first_num, first_elf_second_num+1)
			for i in range(second_elf_first_num, second_elf_second_num+1):
				if i in first_elf_range:
					valid_pairs += 1
					break
		print(valid_pairs)
	f.close()

part1()
part2()
