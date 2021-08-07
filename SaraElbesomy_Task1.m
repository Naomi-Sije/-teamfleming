clc
clear



name = 'Sara Elbesomy';
email = 'sara.f.elbesomy@gmail.com';
slack = '@SaraElbesomy';
biostack = 'Data science';
twitter = '@Saraelbesomy';
hamm_dis = hamming(slack,twitter);


fprintf('%s,%s,%s,%s,%s,%d',name,email,slack,biostack,twitter,hamm_dis)

function d = hamming(s1,s2)
d = 0;
i = 1;
while i <= length(s1)
    if s1(i) ~= s2(i)
        d = d + 1;
    end
    i = i+1;
end
  
end