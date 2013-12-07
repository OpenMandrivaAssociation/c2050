Summary:	Driver for the Lexmark 2050 printer
Name:		c2050
Version:	0.4
Release:	14
Group:		System/Printing
License:	GPL
URL:		http://www.prato.linux.it/~mnencia/lexmark2050
Source0:	http://www.prato.linux.it/~mnencia/lexmark2050/%{name}-%{version}.tar.gz
Patch0:		c2050-0.3-looplimits.patch
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lexmark 2050 Color Jetprinter printer driver.

%prep

%setup -q
%patch0 -p0 -b .looplimits

%build
%{__cc} %{optflags} %{ldflags} -o c2050 c2050.c

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4-11mdv2011.0
+ Revision: 663348
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-10mdv2011.0
+ Revision: 603814
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-9mdv2010.1
+ Revision: 522310
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4-8mdv2010.0
+ Revision: 413208
- rebuild

* Wed Dec 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdv2009.1
+ Revision: 318447
- rediffed P0
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2009.0
+ Revision: 220496
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2008.1
+ Revision: 149065
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4-4mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdv2008.0
+ Revision: 75320
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2008.0
+ Revision: 64141
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdv2008.0
+ Revision: 61073
- rebuild

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2008.0
+ Revision: 60969
- Import c2050



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-1mdv2008.0
- initial Mandriva package

* Tue Jun 01 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-06-01 14:29:10 (62216)
- This driver was seg. faulting and no corrections seems to available.
  I hope this fixes it the right way, since no one can test it.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:23:46 (7426)
- Imported package from 8.0.
