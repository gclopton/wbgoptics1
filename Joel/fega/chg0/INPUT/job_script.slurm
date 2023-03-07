#!/bin/bash

#SBATCH --nodes=1                  # the number of nodes
#SBATCH --tasks-per-node=24                 # the number of cores
#SBATCH --job-name="Ga2O3 SC 555"     # sets job name
#SBATCH -o %x.o%A
#SBATCH -e %x.e%A
#SBATCH -t 72:00:00          # sets maximum total CPU time
#SBATCH -p mrsec	# job partition

cd $SLURM_SUBMIT_DIR

module load fftw-3.3.8/intel-18.0/intel_mpi-2018

mpirun -np $SLURM_NTASKS /home/gclopton/vasp > stdout	# change path to your vasp binary location

