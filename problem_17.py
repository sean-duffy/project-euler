total = 0
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teys = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# 1 - 9
for one in ones:
	print one
	total += len(one)

#10 - 19
for teen in teens:
	print teen
	total += len(teen)

#20 - 99
for tey in teys:
	print tey
	total += len(tey)

	for one in ones:
		print tey, one
		total += len(tey)
		total += len(one)

for one in ones:
	print one, 'hundred'
	total += len(one)
	total += len('hundred')

	for sub_one in ones:
		print one, 'hundred', 'and', sub_one
		total += len(one)
		total += len('hundred')
		total += len('and')
		total += len(sub_one)

	for teen in teens:
		print one, 'hundred', 'and', teen
		total += len(one)
		total += len('hundred')
		total += len('and')
		total += len(teen)

	for tey in teys:
		print one, 'hundred', 'and', tey
		total += len(one)
		total += len('hundred')
		total += len('and')
		total += len(tey)

		for sub_one in ones:
			print one, 'hundred', 'and', tey, sub_one
			total += len(one)
			total += len('hundred')
			total += len('and')
			total += len(tey)
			total += len(sub_one)

print 'one', 'thousand'

total += len('one')
total += len('thousand')

print
print total