const details = {
    name: "Osho Ridwan",
    email: "oshoridwan@gmail.com",
    slackUsername: "@Osho",
    biostack: "Public Health and Genomic Epidemiology",
    twitterHandle: "@readone98"
}

function hammer(){
    let slack = details.slackUsername.toLowerCase();
    let twitter = details.twitterHandle;
    let hamming = 0;

    for (let i =0; i <= slack.length; i++){
        if( twitter[i] !== slack[i]){
            hamming++ 
        };
    };
    return hamming;
}
hammingDistance = hammer();


console.log(details.name, details.email, details.slackUsername, details.biostack, details.twitterHandle, hammingDistance)