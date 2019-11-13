import hashlib
should_be = "893c539a84e6c96acf5f2ceea2ad9ef7be895580"

def main():
	f = open("tempList.txt","r")

	rl = f.readlines()
	x = 0
	for i in rl:
		hash_object = hashlib.sha1("INSA" + i.replace(" ","") )
		hex_dig = hash_object.hexdigest()
		#print hex_dig
		#print should_be ,str(len(should_be)), hex_dig , str(len(hex_dig)) , rl[x],
		if should_be[:x] == str(hex_dig)[:x]:
			#print "foke"
			print should_be ,str(len(should_be)), hex_dig , str(len(hex_dig)) , rl[x],
		x += 1

if __name__ == '__main__':
	main()