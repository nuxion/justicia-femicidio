#!/bin/bash

NEWFILE='/home/nuxion/Proyects/femicidio/femicidio.csv'
base_dir='/home/nuxion/Proyects/femicidio/datasets'
declare -a datasets
echo $base_dir
i=0
for x in `ls $base_dir | grep -v *.txt`:
do
    dos2unix $base_dir/$x
    cat $base_dir/$x | grep -v tipo_victima >> $base_dir/newfile.txt

done
echo datasets[@]

