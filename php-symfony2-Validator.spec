%define		package	Validator
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Validator Component
Name:		php-symfony2-Validator
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	e9f258150cfb0e564698e7d40c696be8
URL:		http://symfony.com/doc/2.7/book/validation.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(filter)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-Translation >= 2.4
#Suggests:	php-doctrine-Annotations
#Suggests:	php-doctrine-Cache
#Suggests:	php-egulias-EmailValidator
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-ExpressionLanguage
Suggests:	php-symfony2-HttpFoundation
Suggests:	php-symfony2-Intl
Suggests:	php-symfony2-PropertyAccess
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component is based on the JSR-303 Bean Validation specification
and enables specifying validation rules for classes using XML, YAML,
PHP or annotations, which can then be checked against instances of
these classes.

%prep
%setup -q -n %{package}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Validator
%{php_pear_dir}/Symfony/Component/Validator/*.php
%{php_pear_dir}/Symfony/Component/Validator/Constraints
%{php_pear_dir}/Symfony/Component/Validator/Context
%{php_pear_dir}/Symfony/Component/Validator/Exception
%{php_pear_dir}/Symfony/Component/Validator/Mapping
%{php_pear_dir}/Symfony/Component/Validator/Util
%{php_pear_dir}/Symfony/Component/Validator/Validator
%{php_pear_dir}/Symfony/Component/Validator/Violation

%dir %{php_pear_dir}/Symfony/Component/Validator/Resources
%dir %{php_pear_dir}/Symfony/Component/Validator/Resources/translations
%lang(af) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.af.xlf
%lang(ar) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.ar.xlf
%lang(az) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.az.xlf
%lang(bg) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.bg.xlf
%lang(ca) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.ca.xlf
%lang(cs) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.cs.xlf
%lang(cy) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.cy.xlf
%lang(da) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.da.xlf
%lang(de) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.de.xlf
%lang(el) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.el.xlf
%lang(en) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.en.xlf
%lang(es) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.es.xlf
%lang(et) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.et.xlf
%lang(eu) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.eu.xlf
%lang(fa) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.fa.xlf
%lang(fi) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.fi.xlf
%lang(fr) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.fr.xlf
%lang(gl) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.gl.xlf
%lang(he) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.he.xlf
%lang(hr) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.hr.xlf
%lang(hu) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.hu.xlf
%lang(hy) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.hy.xlf
%lang(id) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.id.xlf
%lang(it) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.it.xlf
%lang(ja) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.ja.xlf
%lang(lb) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.lb.xlf
%lang(lt) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.lt.xlf
%lang(mn) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.mn.xlf
%lang(nb) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.nb.xlf
%lang(nl) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.nl.xlf
%lang(no) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.no.xlf
%lang(pl) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.pl.xlf
%lang(pt) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.pt.xlf
%lang(pt_BR) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.pt_BR.xlf
%lang(ro) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.ro.xlf
%lang(ru) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.ru.xlf
%lang(sk) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sk.xlf
%lang(sl) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sl.xlf
%lang(sq) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sq.xlf
%lang(sr@cyrillic) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sr_Cyrl.xlf
%lang(sr@latin) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sr_Latn.xlf
%lang(sv) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.sv.xlf
%lang(th) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.th.xlf
%lang(tr) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.tr.xlf
%lang(uk) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.uk.xlf
%lang(vi) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.vi.xlf
%lang(zh_CN) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.zh_CN.xlf
%lang(zh_TW) %{php_pear_dir}/Symfony/Component/Validator/Resources/translations/validators.zh_TW.xlf
