#!/bin/bash


start_time=$(date +"%s")

while [ $(( $time_s- $start_time )) -lt 120 ]; do 

time_s=$(date +"%s")
sleep_time=$(echo "1 / ($time_s- $start_time)" | bc -l )
#echo "0$sleep_time"
echo "$(( $time_s - $start_time))" | figlet
sleep "0$sleep_time"

done
