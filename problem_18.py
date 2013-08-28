with open('problem_18_resource.txt', 'rb') as raw_data:
	data = []
	for row in raw_data:
		data.append(row.split())

greatest_total = 0
start = int(data.pop(0)[0])

for c in range(8193, 16384):
	
	this_total = start
	position = 0

	for i, row in enumerate(data):
		this_c = str(bin(c))[i+2]
		position += int(this_c)
		this_total += int(row[position])

	if this_total > greatest_total:
		greatest_total = this_total

print greatest_total