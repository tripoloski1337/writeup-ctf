a = [  132,137,142,142,182,143,249,248,252,174,146,191,254,187,168,191,158,164,131,244,146,252,253,252,176,]
for x in range(255):
	plain = ''
	for i in range(len(a)):
		plain += chr(a[i] ^ x)
	if "IDC" in plain:
		print plain
		break

