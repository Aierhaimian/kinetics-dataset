#!/bin/bash

filename=$1
dataset=${filename:12:4}
var=${filename:17}
types=${var%%_*}

if [ "$dataset" = "k400" ];
then
    dataset_dir="kinetics_400"
elif [ "$dataset" = "k600" ];
then
    dataset_dir="kinetics_600"
elif [ "$dataset" = "k700" ];
then
    dataset_dir="kinetics_700"
else
    echo "Error: There is no such data set."
    exit 1
fi


while read one;
do
    echo ${one##*/}
    cd "./${dataset_dir}/${types}"
    tar zxvf ${one##*/}
    cd -
done < $1

rm -rf "./${dataset_dir}/${types}/*.tar.gz"

