%define		pkgname	diff
%define		php_min_version 5.3.3
Summary:	Diff implementation for PHP
Name:		php-sebastian-%{pkgname}
Version:	1.1.0
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/sebastianbergmann/diff/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	61b8db69978590e046d31586dff73997
URL:		https://github.com/sebastianbergmann/diff
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diff implementation for PHP, factored out of PHPUnit into a
stand-alone component.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/SebastianBergmann/Diff
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/SebastianBergmann/Diff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE composer.json
%dir %{php_data_dir}/SebastianBergmann
%{php_data_dir}/SebastianBergmann/Diff
