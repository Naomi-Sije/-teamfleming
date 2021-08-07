using Printf

function hamming(s1,s2)
    d = 0;
    i = 1;
    while i <= length(s1)
        if s1[i] != s2[i]
            d +=  1;
        end
        i = i+1;
    end
    return d
  
end


slack = "@SaraElbesomy"
twitter = "@Saraelbesomy"
hamm_dis = hamming(slack,twitter)





@printf("Sara Elbesomy,sara.f.elbesomy@gmail.com,@SaraElbesomy,Data science,@Saraelbesomy,%d", hamm_dis)