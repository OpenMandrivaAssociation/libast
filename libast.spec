%define major		2
%define libname		%mklibname ast %{major}
%define develname	%mklibname ast -d

Summary:	Library of Assorted Spiffy Things
Name:		libast
Version:	0.7
Release:	16
URL:		http://www.eterm.org/
Group:		System/Libraries
License:	BSD
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(xt)

%package -n	%{libname}
Summary:	Library of Assorted Spiffy Things
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%package -n	%{develname}
Summary:	Development related files for LibAST
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

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
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libast-config

%multiarch_includes %{buildroot}%{_includedir}/libast/sysdefs.h

%files -n %{libname}
%doc README
%{_libdir}/lib*.so.%{major}*

%files  -n %{develname}
%doc README
%{_libdir}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4
%{_bindir}/libast-config
%{multiarch_bindir}/libast-config


%changelog
* Fri Jun 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7-16
+ Revision: 807487
- source libast-0.7.tar.gz
- rebuild
- rel up

  + Oden Eriksson <oeriksson@mandriva.com>
    - various fixes
    - rebuilt for new pcre

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-13
+ Revision: 686314
- avoid pulling 32 bit libraries on 64 bit arch

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.7-12
+ Revision: 660600
- fix  multiarch usge
- fix multiarch usage

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-11mdv2011.0
+ Revision: 602521
- rebuild

* Thu Apr 22 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.7-10mdv2010.1
+ Revision: 537843
- disabled static build
  cleaned up specfile

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-9mdv2010.1
+ Revision: 520751
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7-8mdv2010.0
+ Revision: 425516
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7-7mdv2009.1
+ Revision: 301470
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.7-6mdv2009.0
+ Revision: 222503
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7-5mdv2008.1
+ Revision: 170945
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 17 2007 Adam Williamson <awilliamson@mandriva.org> 0.7-3mdv2008.0
+ Revision: 53054
- rebuild for 2008
- new devel policy
- Import libast

