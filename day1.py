def part1():
	max_sum = 0
	with open('inputs/day1.txt') as f:
		calorie_sum = 0
		for line in f:
			if line.strip():
				calorie_sum += int(line.rstrip())
			else:
				if calorie_sum > max_sum:
					max_sum = calorie_sum
				calorie_sum = 0
	print(max_sum)

def part2():
	sums = []
	with open('inputs/day1.txt') as f:
		calorie_sum = 0
		for line in f:
			if line.strip():
				calorie_sum += int(line.rstrip())
			else:
				sums.append(calorie_sum)
				calorie_sum = 0
	sums.sort()
	print(sums[-1] + sums [-2] + sums [-3])

part1()
part2()