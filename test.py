import subprocess

def possible_list(c):
	l = []
	target = ord(c)-97
	for i in range(26):
		if i <= target:
			j = target-i
		else:
			j = target+26-i
		l.append(chr(i+97)+chr(j+97))
	return l

psw = []
for i1 in possible_list("h"):
	for i2 in possible_list("m"):
		for i3 in possible_list("r"):
			for i4 in possible_list("m"):
				msg = i1+i2+i1+i2+i3+i4+i3+i4+"\n" 	
				psw.append(msg)

n = 0
while True:
	p = subprocess.Popen("password.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	for i in range(962*n,962*(n+1)):
		p.stdin.write(psw[i].encode())
		print(i)
	result = p.communicate()[0].decode()
	print(result)
	c = result.count("Wrong")
	print(c)
	if c < 962:
		print(962*n+c,psw[962*n+c])
		break
	else:
		n += 1