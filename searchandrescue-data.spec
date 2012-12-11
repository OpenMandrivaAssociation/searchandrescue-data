%define		base_name	searchandrescue
%define		Base_Name	SearchAndRescue

Name:		%{base_name}-data
Version:	1.3.0
Release:	%mkrel 2
Summary:	Data package for Search and Rescue
License:	GPLv2
Group:		Games/Other
Url:		http://searchandrescue.sourceforge.net
Source:		http://sourceforge.net/projects/searchandrescue/files/Data_Files/%{Base_Name}-data-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is data package for Search and Rescue.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}
rm -f %{buildroot}%{_gamesdatadir}/%{base_name}/LICENSE

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}



%changelog
* Fri Dec 16 2011 Andrey Bondrov <abondrov@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 743140
- Fix game data installation path

* Sat Jul 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1
+ Revision: 688551
- new version

* Fri Jul 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 554156
- new version

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.8.2-7mdv2010.0
+ Revision: 433685
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.2-6mdv2009.0
+ Revision: 242680
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-4mdv2008.0
+ Revision: 67141
- rebuild


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-3mdv2007.0
- %%mkrel

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-2mdk
- fix data files location (fix bug #17634)

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdk
- first distinct release

