import cipher

i = input("Enter Password:")
while True:
	if i == cipher.msg():
		print("\n###################\n")
		print("     Bingo!!!!!!   \n")
		print("###################\n")
		break
	else:
		print("Wrong!!!!!!")
		i = input("Please Enter Again:\n")

print("Congratulations!!!!\nYou got the key having access to the next flag.\nGood luck!!!\n")
input("")
