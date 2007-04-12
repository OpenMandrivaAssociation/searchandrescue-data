%define base_name   searchandrescue
%define Base_Name   SearchAndRescue
%define name        %{base_name}-data
%define version     0.8.2
%define release     %mkrel 3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Data package for Search and Rescue
License:    GPL
Group:      Games/Other
Url:        http://wolfpack.twu.net/SearchAndRescue/index.html
Source:     http://wolfpack.twu.net/users/wolfpack/%{Base_Name}-data-%{version}.tar.bz2
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
%doc LICENSE
%{_gamesdatadir}/%{Base_Name}

