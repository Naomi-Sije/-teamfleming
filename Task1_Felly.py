Name = 'Nnabugwu Felicity Chidinma,'
email = 'felicitychidinma13@gmail.com,'
Slackusername = '@fellyfresh,'
Biostack = 'Drug development,'
Twitterhandle = '@IamFelly01,'

def hammingDist(Slackusername, Twitterhandle):
    i = 0
    count = 0
    while (i < len(Slackusername)):
        if (Slackusername[i] != Twitterhandle[i]):
            count += 1
        i = i+1
    return count
  
print(Name,email,Slackusername,Biostack,Twitterhandle,hammingDist(Slackusername, Twitterhandle))

