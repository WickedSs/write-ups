

Calculation = []

def calc(var_24):
	if (var_24 <= 0x4):
		var_14 = (var_24 * var_24)  + 0x2345
		return var_14
	else:
		var_14 = (Calculation[var_24 - 0x5] * 0x1234) + Calculation[var_24 - 0x1] - Calculation[var_24 - 0x2] + Calculation[var_24 - 0x3] - Calculation[var_24 - 0x4]
		return var_14




for i in range(101930):
	print i
	Calculation.append(calc(i))

result = (Calculation[0x18e29])
print(result & (2**64 -1))


