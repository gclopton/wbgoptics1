#!/bin/bash
current_directory="."


username="clopton@bridges2.psc.edu:"
remote_path_prefix="/ocean/projects/mat220011p/clopton"
system=$(basename $(dirname $(dirname $(dirname $(pwd)))))
charge=$(basename $(dirname $(dirname $(pwd))))
functional=$(basename $(dirname $(pwd)))
remote_path_postfix=$system/$charge/$functional
remote_path=$remote_path_prefix/$remote_path_postfix
files=("/OUTCAR" "/OSZICAR" "/jobstd.err" "/jobstd.out" "INCAR")
copy_destination=${remote_path_prefix}/${system}/${charge}/2_HSE


scp -r "${username}${remote_path}" "${username}${copy_destination}"




