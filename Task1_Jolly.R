
#Create vectors

us = c('@', 'j', 'o', 'l', 'l', 'y')
tw = c('@', 'd', 'o', 'l', 'e', 'y')

#Hamming distance
sum(us != tw)

#Create CSV
HB = data.frame(name = ('Adole Jolly Amoche,'),
                email = ('adolejolly@gmail.com,'),
                username = ('@jolly,'),
                biostack = ('GenomicData,'),
                twiter = ('@doley,'),
                hamm_dist = (2))
print(HB)
View(HB)
