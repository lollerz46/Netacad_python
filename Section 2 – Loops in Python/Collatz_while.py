"""
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

1 take any non-negative and non-zero integer number and name it c0;
2 if it's even, evaluate a new c0 as c0 ÷ 2;
3 otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4 if c0 ≠ 1, go back to point 2.
"""

c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")