name = 'kerishnee naicker,'
email = 'kerrynaicker@gmail.com,'
slackusername = '@kerishnee,'
biostack = 'drug development,'
Twitterhandle = '@kerishnee,'

def hamming_distance(slackusername,twitterhandle):
    count=0
    for i in range (len(slackusername)):
	    if slackusername[i] != twitterhandle[i]:
	       count += 1
	    return count
				
print (name,email,slackusername,biostack,Twitterhandle,(hamming_distance(slackusername, Twitterhandle)))
