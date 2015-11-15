Name: tomcat-native
Version: 1.2.2
Release: 1%{?dist}
Summary: Tomcat native library

License: ASL 2.0
URL: http://tomcat.apache.org/tomcat-7.0-doc/apr.html
Source0: http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz

BuildRequires: apr-devel >= 1.5.2
BuildRequires: openssl-devel >= 1.0.1e

Provides: tcnative = %{version}-%{release}

%description
Apache Tomcat native libaries (APR).


%prep
%setup -q -n %{name}-%{version}-src
f=CHANGELOG.txt ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
cd native
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-platform=2
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install -C native
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%files
%doc CHANGELOG.txt LICENSE NOTICE TODO.txt
%{_libdir}/libtcnative*.so*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
