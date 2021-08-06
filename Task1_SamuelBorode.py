# Hackbio Task 1

def hammingDst(slack, twitter):
	i = 0
	count = 0

	while(i < len(slack)):
		if(slack[i] != twitter[i]):
			count += 1
		i += 1
	return count

name = "Borode Samuel"
gmail = "samuelborode@gmail.com"
slack = "@Samuel"
bio = "Genomics"
twitter = "@psalms"
print (name, gmail, slack, bio, twitter, hammingDst(slack, twitter), sep=', ')


