%define _disable_ld_no_undefined 1

%define major	2
%define libname	%mklibname ast %{major}
%define devname	%mklibname ast -d
%define _disable_lto 1

Summary:	Library of Assorted Spiffy Things
Name:		libast
Version:	0.8
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.eterm.org/
Source0:	https://github.com/mej/libast/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(xt)

%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%package -n	%{libname}
Summary:	Library of Assorted Spiffy Things
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%package -n	%{devname}
Summary:	Development related files for LibAST
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Install this package if you need to compile applications that needs
%{name}.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure
%make_build LIBS='-lX11 -lpcre'

%install
%make_install

%files -n %{libname}
%{_libdir}/libast.so.%{major}*

%files  -n %{devname}
%doc README
%{_libdir}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4
%{_bindir}/libast-config

