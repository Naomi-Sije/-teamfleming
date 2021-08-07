#!/bin/bash

REPO_NAME=https://github.com/Naomi-Sije/-teamfleming.git
CSV_FILE=Fleming.csv
git clone $REPO_NAME
cd ./-teamfleming

echo "Name, Email, Slack, Biostak, Twitter, Hamming Distance" >> $CSV_FILE
for script in $(ls);
do
        if [[ $script == *.py ]]; 
              then
                echo $(python $script) >> $CSV_FILE
	elif [[ $script == *.jl ]];
		then
		 echo $(julia $script) >> $CSV_FILE
       
        elif [[ $script == *.cpp ]];
              then
                 g++ $script -o compiled_object   
                 echo $(./compiled_object) >> $CSV_FILE 
                 
        elif [[ $script == *.rb ]];
              then
                 echo $(ruby $script) >> $CSV_FILE  
	elif [[ $script == *.R ]];
              then
                 echo $(Rscript $script) >> $CSV_FILE 
	 elif [[ $script == *.pl ]];
              then
                 echo $(perl $script)  >> $CSV_FILE 
	 elif [[ $script == *.js ]];
              then
                echo $(node $script) >> $CSV_FILE   
          
        fi
done

rm compiled_object.exe




 




   

