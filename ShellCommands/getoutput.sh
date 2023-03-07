#!/bin/bash
current_directory="."


username="clopton@bridges2.psc.edu:"
remote_path_prefix="/ocean/projects/mat220011p/clopton"
system=$(basename $(dirname $(dirname $(dirname $(pwd)))))
charge=$(basename $(dirname $(dirname $(pwd))))
functional=$(basename $(dirname $(pwd)))
remote_path_postfix=$system/$charge/$functional
remote_path=$remote_path_prefix/$remote_path_postfix
files=("/OUTCAR" "/OSZICAR" "/jobstd.err" "/jobstd.out")

for file in "${files[@]}"
do
    scp "${username}${remote_path}${file}" "${current_directory}"
done

touch magnetization_table.txt
touch magnetization_stripped.txt

