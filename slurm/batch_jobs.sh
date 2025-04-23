#!/bin/bash

n=100
for i in $(seq 1 $n); do
    sbatch ./slurm_estimate_pi.sh
done

