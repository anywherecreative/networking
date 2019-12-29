# Convert decimal ip address to binary
# author: Hexentales <hexentales.com>

# takes a decimal ip and converts to binary.
def convert(ip):
	new = [] # the new ip address
	# break ip address into 4 parts based on decimals
	x = 0
	parts = ip.split(".")

	if(len(parts) < 4):
		return "Invalid IP - Ip must be 4 octets seperated by decimals."

	for p in parts:
		try:
			p = int(p)
			if(p >= 0 and p <= 255):
				new.append(bin(int(p)).replace("0b", "").zfill(8))

			else:
				return "Invalid IP - octets must be in range of 0-255."
		except ValueError:
			return "Invalid IP - octets must be valid numbers."

	return ".".join(new)

def mainLoop():
	ip = raw_input("Enter an ip address, or Q to quit: ")
	if(ip != "q" and ip != "Q"):
		print(convert(ip))
	else:
		exit()

while(1):
	mainLoop()
