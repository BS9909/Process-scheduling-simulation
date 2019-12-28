#!/bin/bash

#skrypt liczy czas przetwarzania procesow, jesli chcesz czas oczekiwania odejmij ostatnia linie

sum=0
while read line;do
	sum=$(($sum+$line))
done <$1

echo $sum