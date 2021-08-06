name = 'Stephanie Ezirim,'
email = 'ezirimstephanie53@gmail.com,'
slackusername = '@Stephanie,'
biostack = 'Medicinal chemistry and Chemoinformatics,'
twitter = '@StephanieEzirim,'

#code_for_hamming_distance
def hammingDist(slackusername, twitter):
    i = 0
    count = 0

    while (i < len(slackusername)):
        if (slackusername[i] != twitter[i]):
            count += 1
            i += 1
            return count

print (name, email, slackusername, biostack, twitter, (hammingDist(slackusername, twitter)))