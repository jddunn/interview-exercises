def gcd(m, n):
	while m % n != 0:
		# print("Old" m, n)
		old_m = m
		old_n = n
		m = old_n
		n = old_m % old_n
		print(m, n)
	return n

print(gcd(50, 20))