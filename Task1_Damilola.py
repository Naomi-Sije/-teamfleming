print('Damilola, ibrahimabdulmumin1997@gmail.com, @Damilola, Data Science, @Damlord7,')



def hamming_distance(s1,s2):
    result=0
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            result += 1
    return result
print('hamming distance=' + str(hamming_distance('@Damilola','@Damlord7')))
