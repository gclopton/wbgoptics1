#!/bin/bash

# Define the top-level directory
top_dir="irga"

# Define the subdirectories and sub-subdirectories
subdirs=("chg0" "chg1" "chg2")
subsubdirs=("1_PBE" "2_HSE")

# Loop over the subdirectories and sub-subdirectories to create the directories
for subdir in "${subdirs[@]}"; do
    for subsubdir in "${subsubdirs[@]}"; do
        mkdir -p "${top_dir}/${subdir}/${subsubdir}/INPUT"
        mkdir -p "${top_dir}/${subdir}/${subsubdir}/OUTPUT"
        mkdir -p "${top_dir}/${subdir}/${subsubdir}/POST"
        mkdir -p "${top_dir}/${subdir}/${subsubdir}/SEND"
    done
done

# Create the empty directories
#mkdir -p "${top_dir}/chgn3/1_PBE/INPUT"
#mkdir -p "${top_dir}/chgn3/1_PBE/OUTPUT"
