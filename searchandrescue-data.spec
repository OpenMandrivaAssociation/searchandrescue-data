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

