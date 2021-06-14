# Simul
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

