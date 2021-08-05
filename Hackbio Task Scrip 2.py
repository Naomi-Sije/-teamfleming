def hamming_distance(s1, s2):
    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


name = "Godspower Tochukwu Isaac,"
email = "godspowerisaac33@gmail.com,"
slack_username = "@GeePee,"
biostack = "Drug Development,"
twitter_handle = "@Tochey,"


print(name, email, slack_username, biostack, twitter_handle, hamming_distance('@GeePee', '@Tochey'))







