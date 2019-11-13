# v7 = strlen(argv[2]);
# dest = (char *)malloc(v7 + 1);
# strcpy(dest, argv[2]);
# for ( i = 0LL; i < strlen(dest) >> 1; ++i )
# {
# 	v13 = dest[i];
# 	dest[i] = dest[strlen(dest) - i - 1];
# 	dest[strlen(dest) - i - 1] = v13;
# }

#data = raw_input(">> ")
#data = data.list()
# data = ["z","L","l","1","k","s","_","d","4","m","_","T","0","g","_","I"]
# v7 = len(data)
# print "sebelum : " + str(data)
# for x in range(v7):
# 	for i in range(len(data)):
# 		v13 = data[i]
# 		data[i] = data[len(data) - i - 1]
# 		data[len(data) - i - 1 ] = v13
# 		print "proses = " + str(data)
# 		print data[i]
# print "sesudah : " + str(data)
#I_g0T_md4_sk1lLz
#I_g0T_m4d_sk1lLz
a = [c for c in "zLl1ks_d4m_T0g_I"]
gl = len(a)

for i  in range(0,len(a),2):
	tmp = a[i]
	a[i] = a[gl-i-1]
	a[gl-i-1] = tmp
	pass

print "".join(a)

