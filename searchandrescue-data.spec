%define base_name   searchandrescue
%define Base_Name   SearchAndRescue
%define name        %{base_name}-data
%define version     1.0.0
%define release     %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Data package for Search and Rescue
License:    GPL
Group:      Games/Other
Url:        http://searchandrescue.sourceforge.net
Source:     http://sourceforge.net/projects/searchandrescue/files/Data_Files/%{Base_Name}-data-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This is data package for Search and Rescue.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{Base_Name}
cp -pr * %{buildroot}%{_gamesdatadir}/%{Base_Name}
rm -f %{buildroot}%{_gamesdatadir}/%{Base_Name}/LICENSE

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_gamesdatadir}/%{Base_Name}

