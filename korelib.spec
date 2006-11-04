#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Korelib - C++ framework for developing plugin-based applications
Summary(pl):	Korelib - framework C++ do tworzenia aplikacji bazowanych na pluginach
Name:		korelib
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	ee220ca3cf6efddf0427ff6a3a5cad36
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Korelib is a extensible C++ framework for developing plugin-based
applications.

%description -l pl
Korelib jest rozszerzalnym frameworkiem C++ do tworzenai aplikacji
bazowanych na pluginach.

%package devel
Summary:	Header files for Korelib library
Summary(pl):	Pliki nag��wkowe biblioteki Korelib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Korelib library.

%description devel -l pl
Pliki nag��wkowe biblioteki Korelib.

%package static
Summary:	Static Korelib library
Summary(pl):	Statyczna biblioteka Korelib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Korelib library.

%description static -l pl
Statyczna biblioteka Korelib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no} \
	--program-prefix=korelib	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korelibdemo
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/kore

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif