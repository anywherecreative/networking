# calculate subnet mask, network address, broadcast, and range from ip and mask
# author: Hexentales <hexentales.com>

# takes a decimal ip and converts to binary.

from pprint import pprint

def getSubnetMask(slash):
	# show subnet mask from
	try:
		full = int(slash)/8 #how many full octets
		partial = int(slash)%8 #calculate shift on partial octet
		octet = "1"*partial #expand shift into left part of binary number
		octet = octet.ljust(8,"0") #pad the rest with 0 to make octet
		octet = int(octet,2) #convert to decimal
		return "255."*full+str(octet) +".0"*(3-full) #return 4 octets
	except ValueError:
		return 0

def getGateWay(ip):
	try:
		parts = ip.split("/")
		full = int(parts[1])/8 # how many full octets
		partial = int(parts[1])%8 # the partial octet
		ipParts = parts[0].split(".") # break the ip address into octets
		final = "" # placeholder for final gateway address
		# grab the full octets from the original ip as these are part of the mask
		for x in range(full):
			final += ipParts[x] + "."

		# take the octet that needs to be calculated, and convert to binary.
		pcalc = bin(int(ipParts[full])).replace("0b", "")+""

		# we are only interested in the places dictated by the mask, so we take these and trim the rest
		# we append the required number of 0s to complete the octet, then convert the result to decimal
		final += str(int(pcalc[0:partial].ljust(8,"0"),2))


		
		#finally, append empty octets to complete the ip address if necessary
		final = final+".0"*(3-full)
		return final
	except ValueError:
		return 0

def getMaxHosts(ip):
	parts = ip.split("/")
	partial = int(parts[1])%8 #calculate shift on partial octet
	hosts = int(("0"*partial).ljust(8,"1"),2)
	return hosts-1

def getRange(ip):
	gateway = getGateWay(ip)
	hosts = getMaxHosts(ip)
	octets = gateway.split(".")
	last = octets[3];
	octets.pop();
	return {"min":".".join(octets)+"."+str(int(last)+1), "max":".".join(octets)+"."+str(int(last)+hosts)}

def getBroadcastAddress(ip):
	gateway = getGateWay(ip)
	hosts = getMaxHosts(ip)
	octets = gateway.split(".")
	octets[3] = str(int(octets[3])+(hosts+1))
	return ".".join(octets)



def mainLoop():
	ip = raw_input("Enter an ip address with slash notation, or Q to quit: ")
	if(ip != "q" and ip != "Q"):
		parts = ip.split("/")
		print("Subnet Mask: " + getSubnetMask(parts[1]))
		print("Gateway: " + getGateWay(ip))
		print("Max Hosts: " + str(getMaxHosts(ip)))
		range = getRange(ip);
		print("Host Min: " + str(range['min']))
		print("Host Max: " + str(range['max']))
		print("broadcast: " + getBroadcastAddress(ip))
	else:
		exit()

while(1):
	mainLoop()