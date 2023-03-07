#!/bin/bash
current_directory="."


joelshome="../../../../../../Joel/"
chanshome="../../../../../../HSE_cal"
remote_path_prefix="/ocean/projects/mat220011p/clopton"
system=$(basename $(dirname $(dirname $(dirname $(pwd)))))
charge=$(basename $(dirname $(dirname $(pwd))))
functional=$(basename $(dirname $(pwd)))
remote_path_postfix=$system/$charge/$functional
remote_path=$remote_path_prefix/$remote_path_postfix
files=("/CONTCAR" "/KPOINTS")
chansfiles=("/INCAR" "/vasp5_submit")


for file in "${chansfiles[@]}"
do
    cp "${chanshome}/${functional}${file}" "."
    echo "${chanshome}/${functional}${file}" "."
done

touch INCAR_updated
touch INCAR_final