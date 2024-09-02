# DISCONTINUATION OF PROJECT #  
This project will no longer be maintained by Intel.  
Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.  
Intel no longer accepts patches to this project.  
 If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the open source software community, please create your own fork of this project.  
  
# Simul

What is Simul?
    From: https://github.com/LLNL/simul

    "simul" is an MPI coordinated test of parallel filesystem system calls and
    library functions.  It was designed to perform filesystem operations
    simultaneously from many nodes and processes to test the correctness
    and coherence of parallel filesystems.

How is simul used in DAOS?

    Simul can let us know what POSIX operations are working or not
    in a POSIX container.

    There should be an automated test for this.


RPM packaging of Simul

Generates 5 rpms:
    simul-src
    simul
    simul-mpich
    simul-openmpi3
    simul-debuginfo

Binaries to be used by tests are within simul-mpich
and simul-openmpi3. Test should load the appropiate 
mpi module and run the following command:
    simul

