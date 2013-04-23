#!/bin/bash
## This script is used to take the data created by sc2Replayer and 
## put it into the ARFF format 
## usage:
## getBuild file.txt

#Remove data file to do house cleaning
rm data.txt
echo "Processing Files: $@"
COUNTER=0
for file in $@ 
do
    echo "Processing file #: " $COUNTER
    let COUNTER=COUNTER+1
    buildNo=`head -1 $file`
    map=`head -2 $file | tail -1`
    player1=`head -3 $file | tail -1`
    player1result=`head -4 $file | tail -1`
    player1race=`head -5 $file | tail -1`
    player1apm=`head -6 $file | tail -1`
    player2=`head -8 $file | tail -1`
    player2result=`head -9 $file | tail -1`  
    player2race=`head -10 $file | tail -1`
    player2apm=`head -11 $file | tail -1`
    gamelength=`head -12 $file | tail -1 | sed 's/\./:/'`
    data="$player1,$player1result,$player1race,$player1apm,$player2,$player2result,$player2race,$player2apm,$gamelength"
    
    buildings=`grep $player1 $file | tr -s ' ' | cut -d ' ' -f 5 | head -11 | tail -10 | sed 's/Build//g' | sed 's/;//g'`
    player1buildings=$buildings
   
    buildings=`grep $player2 $file | tr -s ' ' | cut -d ' ' -f 5 | head -11 | tail -10 | sed 's/Build//g' | sed 's/;//g'`
    player2buildings=$buildings
    
    for building in $player1buildings
    do
	data+=",$building"
    done
    for building in $player2buildings
    do
	data+=",$building"
    done
	
	## Header has 8 commas
	## Each player has 10 commas
	## Overall 28 commas per line
	if test `echo $data | tr -cd , | wc -c` -eq 28
	then
		echo "$data" >> data.txt
	fi	
    
done