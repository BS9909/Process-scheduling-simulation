#!/bin/bash

for((i=0;i<100;++i));do
	for((j=0;j<100;++j));do
		echo -e "$((1+RANDOM%20))" >>$1
	done
	#echo -e "\n \n \n \n" >> $1
done