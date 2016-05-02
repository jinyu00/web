fp = open("1.txt","r")
out = open("x_1.txt","a+")
result = []
lines = fp.xreadlines()
for line in lines:
	line = line.strip()
	try:

		line = line.split('|')[1]
	except:
		print line
	out.write(line + '\n')
fp.close()
out.close()



print "successful"

