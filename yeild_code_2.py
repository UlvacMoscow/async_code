def concat_sequence(s1, s2):
	for elem in s1:
		yield elem
	for elem in s2:
		yield elem

def concat_sequence_v2(s1, s2):
	yield from s1
	yield from s2


seq1 = range(10)
seq2 = range(10, 20)

result = concat_sequence(seq1, seq2)

for el in result:
	print(el, end=' ')

result2 = concat_sequence_v2(seq1, seq2)

for el in result2:
	print(el, end=' ')