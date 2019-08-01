#!/bin/bash

datasize=${1}
num_thread=${2}

for bench in blackscholes bodytrack canneal dedup facesim ferret fluidanimate freqmine streamcluster swaptions x264
do
  ./gen_rcs.sh -p $bench -i $datasize -n $num_thread
done
