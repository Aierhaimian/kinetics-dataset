#!/bin/bash

filename=$1

dataset=${filename:12:4}

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

var=${filename:17}
types=${var%%_*}

if [ ! -d "${types}" ];
then
    mkdir -p "${dataset_dir}/${types}"
fi

while read one;
do
    echo $one
    wget -c -P "./${dataset_dir}/${types}" "$one"
done < $1

