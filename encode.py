#!/usr/bin/env python3

f = open("a.out", "rb")

count = 0
res = ""
pipe = "> b.out"
while True:
	byte = f.read(1)
	if not byte:
		break
	res += "\\x" + byte.hex()
	count+=1
	
	if count % 16 == 0:
		print("echo -n -e '" + res + "' " + pipe)
		print("")
		res = ""
	
	if count == 16:
		pipe = ">> b.out"

if len(res) > 0:
	print("echo -n -e '" + res + "' " + pipe)
	print("")
		
