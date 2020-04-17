message = "hackhackglhfglhf"

def msg():
	return message

def encrypt(m):
	n = ""
	if len(m)%2 == 0:
		pass
	else:
		m += "0"
	for i in range(0,len(m),2):
		if ord(m[i]) >= 97 and ord(m[i]) <= 122 and ord(m[i+1]) >= 97 and ord(m[i+1]) <= 122:
			n += chr((ord(m[i])+ord(m[i+1])-194)%26+97)
		else:
			if ord(m[i]) >= 97 and ord(m[i]) <= 122:
				n += m[i]
			else:
				n += m[i+1]
	return n

#print(encrypt(msg()))