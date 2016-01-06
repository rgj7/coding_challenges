import math

def distance(x1, y1, x2, y2):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

dist = 1.0
diag_dist = math.sqrt(3)*0.5
	
""" begin """

test_cases = int(input())
for i in range(test_cases):
	moves = input()
	x = 0.0
	y = 0.0
	for m in moves:
		if m == 'A':
			x += dist
		elif m == 'B':
			x += dist/2
			y += diag_dist
		elif m == 'C':
			x -= dist/2
			y += diag_dist
		elif m == 'D':
			x -= dist
		elif m == 'E':
			x -= dist/2
			y -= diag_dist
		elif m == 'F':
			x += dist/2
			y -= diag_dist
	print("{:.8f}".format(distance(0.0, 0.0, x, y)), end=" ")