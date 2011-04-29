%define major		2
%define libname		%mklibname ast %{major}
%define develname	%mklibname ast -d

Summary:	Library of Assorted Spiffy Things 
Name:		libast
Version:	0.7
Release:	%mkrel 12
URL:		http://www.eterm.org/
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	imlib2-devel
BuildRequires:	pcre-devel
BuildRequires:	libxt-devel

%package -n	%{libname}
Summary:	Library of Assorted Spiffy Things
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%package -n	%{develname}
Summary:	Development related files for LibAST
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname ast 2 -d}

%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%description -n	%{libname}
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%description -n	%{develname}
Install this package if you need to compile applications that needs
%{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libast-config
%multiarch_includes %{buildroot}%{_includedir}/libast/sysdefs.h

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc README 
%{_libdir}/lib*.so.*

%files  -n %{develname}
%defattr(-,root,root)
%doc README
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/*
%{multiarch_includedir}/libast/sysdefs.h
%{_datadir}/aclocal/*.m4
%{_bindir}/libast-config
%{multiarch_bindir}/libast-config
