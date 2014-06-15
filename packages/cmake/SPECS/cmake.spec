%define rpm_macros_dir %{_sysconfdir}/rpm

Name: cmake
Version: 3.0.0
Release: 1%{?dist}
Summary: Cross-platform make system

Group: Development/Tools

License: BSD and MIT and zlib
URL: http://www.cmake.org
Source0: http://www.cmake.org/files/v3.0/cmake-%{version}%{?rcver}.tar.gz
Source1:        cmake-init.el
Source2:        macros.cmake

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++
BuildRequires: ncurses-devel
BuildRequires: python-devel


%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%package        doc
Summary:        Documentation for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for CMake.


%prep
%setup -q -n cmake-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
mkdir build
pushd build
../bootstrap --prefix=%{_prefix} --datadir=/share/%{name} \
             --docdir=/share/doc/%{name}-%{version} --mandir=/share/man \
             --no-system-libs \
             --parallel=`/usr/bin/getconf _NPROCESSORS_ONLN` \
             --sphinx-man
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT/%{_datadir}/%{name}/Modules -type f | xargs chmod -x
popd

# Install bash completion symlinks
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
for f in %{buildroot}%{_datadir}/%{name}/completions/*
do
  ln -s ../../%{name}/completions/$(basename $f) %{buildroot}%{_datadir}/bash-completion/completions/
done

# Install emacs cmake mode
#mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
#install -p -m 0644 Auxiliary/cmake-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/
#%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/%{name}/cmake-mode.el
#mkdir -p %{buildroot}%{_emacs_sitestartdir}
#install -p -m 0644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}/

# RPM macros
install -p -m0644 -D %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.cmake
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" %{buildroot}%{rpm_macros_dir}/macros.cmake
touch -r %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.cmake
mkdir -p %{buildroot}%{_libdir}/%{name}

# Install copyright files for main package
cp -p Copyright.txt %{buildroot}/%{_docdir}/%{name}/
find Source Utilities -type f -iname copy\* | while read f
do
  fname=$(basename $f)
  dir=$(dirname $f)
  dname=$(basename $dir)
  cp -p $f %{buildroot}/%{_docdir}/%{name}/${fname}_${dname}
done


%check
unset DISPLAY
pushd build
# ModuleNotices fails for some unknown reason, and we don't care
# CMake.HTML currently requires internet access
# CTestTestUpload requires internet access
bin/ctest -V -E ModuleNotices -E CMake.HTML -E CTestTestUpload %{?_smp_mflags}
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/Copyright.txt*
%{_docdir}/%{name}/COPYING*
%{rpm_macros_dir}/macros.cmake
%{_bindir}/ccmake
%{_bindir}/cmake
%{_bindir}/cpack
%{_bindir}/ctest
%{_datadir}/aclocal/cmake.m4
%{_datadir}/bash-completion/
%{_datadir}/%{name}/
%{_mandir}/man1/ccmake.1.gz
%{_mandir}/man1/cmake.1.gz
%{_mandir}/man1/cpack.1.gz
%{_mandir}/man1/ctest.1.gz
%{_mandir}/man7/*.7.gz
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/%{name}-init.el
%{_libdir}/%{name}/

%files doc
%{_docdir}/%{name}/


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.11.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.10.rc6
- Update to 3.0.0-rc6
