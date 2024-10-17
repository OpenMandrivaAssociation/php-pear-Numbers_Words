%define		_class		Numbers
%define		_subclass	Words
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.16.3
Release:	5
Summary:	Provides methods for spelling numerals in words
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Numbers_Words/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-gd
BuildArch:	noarch
BuildRequires:	php-pear

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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/ChangeLog
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.3-3mdv2012.0
+ Revision: 741805
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.3-2
+ Revision: 741145
- rebuild

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.3-1
+ Revision: 741092
- 0.16.3

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.1-5
+ Revision: 679551
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16.1-4mdv2011.0
+ Revision: 613744
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16.1-3mdv2010.1
+ Revision: 468730
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.16.1-2mdv2010.0
+ Revision: 441499
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.16.1-1mdv2009.1
+ Revision: 368336
- Update php pear Numbers_Words to 0.16.1 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-3mdv2009.1
+ Revision: 322508
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-2mdv2009.0
+ Revision: 237038
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.15.0-1mdv2008.0
+ Revision: 15472
- 0.15.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-1mdv2007.0
+ Revision: 82486
- Import php-pear-Numbers_Words

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-1mdk
- 0.14.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-2mdk
- fix spec file to conform with the others

* Sun May 29 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.1-1mdk
- initial Mandriva package

