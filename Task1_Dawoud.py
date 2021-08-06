name = "Usman Dawoud,"
email = "dawoudusman6@gmail.com,"
slack_username = "@Dawoud,"
biostack = "Transcriptomics,"
twitter_handle = "@usman_dawoud,"

def hamming_distance(slack_username, twitter_handle):
    if len(slack_username) != len(twitter_handle):
        return "string lengths are not equal!"
    else:
        return sum(1 for (a,b) in zip(slack_username, twitter_handle))

print(name, email, slack_username, biostack, twitter_handle, hamming_distance(slack_username, twitter_handle))
