Summary:	Driver for the Lexmark 2050 printer
Name:		c2050
Version:	0.4
Release:	%mkrel 5
Group:		System/Printing
License:	GPL
URL:		http://www.prato.linux.it/~mnencia/lexmark2050
Source0:	http://www.prato.linux.it/~mnencia/lexmark2050/%{name}-%{version}.tar.gz
Patch0:		c2050-0.3-looplimits.patch
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Lexmark 2050 Color Jetprinter printer driver.

%prep

%setup -q
%patch -p1 -b .looplimits

%build
%{__cc} %{optflags} -o c2050 c2050.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 c2050 %{buildroot}%{_bindir}/
install -m0755 ps2lexmark %{buildroot}%{_bindir}/
install -m0755 ps2monolexmark %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README COPYING
%attr(0755,root,root) %{_bindir}/*
