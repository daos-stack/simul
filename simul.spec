%global with_mpich 1

%if (0%{?rhel} >= 8)
%global with_openmpi 1
%global with_openmpi3 0
%else
%global with_openmpi 0
%global with_openmpi3 1
%endif


%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
%if %{with_openmpi3}
%global mpi_list %{?mpi_list} openmpi3
%endif

%global source_vars() if [ "%{1}" == "mpich" ]; then source %{_libdir}/mpi/gcc/mpich/bin/mpivars.sh; elif [ "%{1}" == "openmpi3" ]; then source %{_libdir}/mpi/gcc/mpich/bin/mpivars.sh; else echo "no vars";fi

%if (0%{?suse_version} >= 1500)
%global module_load() if [ "%{1}" == "openmpi3" ]; then MODULEPATH=/usr/share/modules module load gnu-openmpi; else MODULEPATH=/usr/share/modules module load gnu-%{1}; fi
%global mpi_libdir %{_libdir}/mpi/gcc
%else
%global module_load() module load mpi/%{1}-%{_arch}
%global mpi_libdir %{_libdir}
%endif

Name:    simul
Version: 1.16
Release: 1%{?commit:.git%{shortcommit}}%{?dist}
Summary: "simul" is an MPI coordinated test of parallel filesystem system calls and library functions.

License: GPLV2
URL:     https://github.com/LLNL/simul/
Source0: https://github.com/LLNL/%{name}/archive/refs/tags/%{version}.tar.gz
Patch1: 0001-find-inline.patch

%description
"simul" is an MPI coordinated test of parallel filesystem system calls and
library functions.  It was designed to perform filesystem operations
simultaneously from many nodes and processes to test the correctness
and coherence of parallel filesystems.

%if %{with_mpich}
%package mpich
Summary: Simul for MPICH
%if "%{_host_vendor}" == "suse"
BuildRequires: mpich-devel%{?_isa} lua-lmod
%endif
%if "%{_host_vendor}" == "redhat"
BuildRequires: mpich-devel%{?_isa}
%endif
Requires: %{name}%{?_isa} = %{version}-%{release}

%description mpich
Simul for MPICH
%endif

%if %{with_openmpi}
%package openmpi
Summary: Simul for OpenMPI
%if "%{_host_vendor}" == "suse"
BuildRequires: openmpi-devel%{?_isa} lua-lmod
%endif
%if "%{_host_vendor}" == "redhat"
BuildRequires: openmpi-devel%{?_isa}
%endif
Requires: %{name}%{?_isa} = %{version}-%{release}

%description openmpi
Simul for openmpi
%endif



%if %{with_openmpi3}
%package openmpi3
Summary: Simul for OpenMPI 3
%if "%{_host_vendor}" == "suse"
BuildRequires: openmpi3-devel%{?_isa} lua-lmod
%endif
%if "%{_host_vendor}" == "redhat"
BuildRequires: openmpi3-devel%{?_isa}
%endif
Requires: %{name}%{?_isa} = %{version}-%{release}

%description openmpi3
Simul for OpenMPI 3
%endif

%prep

%autosetup -p1

%build

for mpi in %{?mpi_list}
do
    mkdir $mpi
    %module_load $mpi
    %source_vars $mpi
    make simul
    mv simul $mpi/simul
    module purge
done

%install
for mpi in %{?mpi_list}
do
    pushd $mpi
    install -d %{buildroot}/%{mpi_libdir}/$mpi/bin/
    install -m 633 simul %{buildroot}/%{mpi_libdir}/$mpi/bin
    popd
done

%files

%license COPYING

%if %{with_mpich}
%files mpich
%{mpi_libdir}/mpich/bin/*
%endif

%if %{with_openmpi}
%files openmpi
%{mpi_libdir}/openmpi/bin/*
%endif

%if %{with_openmpi3}
%files openmpi3
%{mpi_libdir}/openmpi3/bin/*
%endif

%changelog
* Wed Jun 23 2021 Omar Ocampo <omar.ocampo.coronado@intel.com> - $version-$release
- Initial version
