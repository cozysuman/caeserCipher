def getMode():
	print('What do you want?(encrypt or decrypt)')
	mode=input().lower()
	if mode in 'encrypt e decrypt d'.split():
		return mode
	else:
		print('enter either "encrypt" "e" "decrypt" "d"')

def plainText():
	return (input('Enter your message '))

def getKey():
	key=int(input('enter key (1-26)'))
	return key

def cipherText(mode,message,key):
	if mode[0]=='d':
		key= -key
	translated=''
	for symbol in message:
		if symbol.isalpha():
			num= ord(symbol)
			num+=key
			if symbol.isupper():
				if num > ord('Z'):
					num-=26
				elif num<ord('A'):
					num+=26
			elif symbol.islower():
				if num>ord('z'):
					num-=26
				elif num<ord('a'):
					num+=26
			translated+=chr(num)
		else:
			translated +=symbol
	return translated

mode=getMode()
message=plainText()
key=getKey()

print(cipherText(mode, message, key))
