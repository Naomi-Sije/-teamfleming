name = 'Chukwuemelie Aginah'
email = 'chukwuemelie.aginah@gmail.com'
biostack = 'Data science'

import hashlib

def hamming_distance(slack_username, twitter_username):
    return sum(c1 != c2 for c1, c2 in zip(slack_username, twitter_username)) 

def hamming_distance2(slack_username, twitter_username):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(slack_username, twitter_username))))

if __name__=="__main__":    
    slack_username = hashlib.md5("slack_username".encode()).hexdigest()
    twitter_username = hashlib.md5("twitter_username".encode()).hexdigest()

    slack_username = "@Chukwu_emeliela"
    twitter_username = "@Chukwu_emeliela"

    assert len(slack_username) == len(twitter_username)

list = (name, email, slack_username, biostack, twitter_username, hamming_distance(slack_username, twitter_username))

string = ",".join(map(str, list))

print(string)
