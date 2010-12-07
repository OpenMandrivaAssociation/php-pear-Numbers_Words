%define		_class		Numbers
%define		_subclass	Words
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PHPUnit

Name:		php-pear-%{upstream_name}
Version:	0.16.1
Release:	%mkrel 4
Summary:	Provides methods for spelling numerals in words
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Numbers_Words/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-gd
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
With Numbers_Words class you can convert numbers written in arabic
digits to words in several languages. You can convert an integer
between -infinity and infinity. If your system does not support such
long numbers you can call Numbers_Words::toWords() with just a string.

The following languages are supported (in alphabetical order):
- bg (Bulgarian) by Kouber Saparev
- de (German)
- ee (Estonian) by Erkki Saarniit
- en_100 (Donald Knuth system, English)
- en_GB (Britich English)
- en_US (American English)
- es (Spanish Castellano) by Xavier Noguer
- es_AR (Argentinian Spanish) by Martin Marrese
- fr (French) by Kouber Saparev
- id (Indonesian) by Ernas M. Jamil
- it_IT (Italian) by Filippo Beltramini and Davide Caironi
- pl (Polish)
- pt_BR (Brazilian Portuguese) by Marcelo Subtil Marcal
- ru (Russian) by Andrey Demenev
- sv (Swedish) by Robin Ericsson


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/ChangeLog
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
