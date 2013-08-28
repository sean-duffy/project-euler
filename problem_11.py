with open('problem_11_resource.txt', 'rb') as raw_data:

	data = []
	for row in raw_data:
		data.append(row.split())

greatest_product = 0

def product_find():
	global greatest_product
	if product > greatest_product:
		greatest_product = product

# Horizontal
for row in data:
	for i in range(17):

		product = 1
		for n in range(4):
			product *= int(row[n + i])

		product_find()

# Vertical
for x in range(20):
	for y in range(16):

		product = 1
		for n in range(4):
			product *= int(data[x][y + n])

		product_find()

#Diagonal Right
for x in range(17):
	for y in range(17):

		product = 1
		for n in range(4):
			product *= int(data[x + n][y + n])

		product_find()

#Diagonal Left
for x in range(3, 20):
	for y in range(17):

		product = 1
		for n in range(4):
			product *= int(data[x - n][y + n])

		product_find()

print greatest_product