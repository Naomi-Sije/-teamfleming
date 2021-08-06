#!/usr/bin/perl
$Name = "Maxwell Booker,";
$email = "alungamaxwell\@gmail.com,";
$username = "\@Max,";
$biostack = "drug development,";
$twitterhandle = "\@maxxisbooker,";
$c=0;
for $i (1..length($username)){
    if(length($username)==length($twitterhandle)){
        if ($username[i]!=$twitterhandle[i]){
        $c++;
        }
        else{
            continue;
        }
    }
}
print $Name;
print $email;
print $username;
print $biostack;
print $twitterhandle;
print $c;
