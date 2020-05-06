%define		package	Validator
%define		php_min_version 5.3.9
Summary:	Symfony2 Validator Component
Name:		php-symfony2-Validator
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	55df7096d08e082027f1b2af08e32bba
URL:		http://symfony.com/doc/2.7/book/validation.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(filter)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
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
%setup -q -n validator-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Validator
%{php_data_dir}/Symfony/Component/Validator/*.php
%{php_data_dir}/Symfony/Component/Validator/Constraints
%{php_data_dir}/Symfony/Component/Validator/Context
%{php_data_dir}/Symfony/Component/Validator/Exception
%{php_data_dir}/Symfony/Component/Validator/Mapping
%{php_data_dir}/Symfony/Component/Validator/Util
%{php_data_dir}/Symfony/Component/Validator/Validator
%{php_data_dir}/Symfony/Component/Validator/Violation

%dir %{php_data_dir}/Symfony/Component/Validator/Resources
%dir %{php_data_dir}/Symfony/Component/Validator/Resources/translations
%lang(af) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.af.xlf
%lang(ar) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.ar.xlf
%lang(az) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.az.xlf
%lang(bg) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.bg.xlf
%lang(ca) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.ca.xlf
%lang(cs) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.cs.xlf
%lang(cy) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.cy.xlf
%lang(da) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.da.xlf
%lang(de) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.de.xlf
%lang(el) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.el.xlf
%lang(en) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.en.xlf
%lang(es) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.es.xlf
%lang(et) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.et.xlf
%lang(eu) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.eu.xlf
%lang(fa) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.fa.xlf
%lang(fi) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.fi.xlf
%lang(fr) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.fr.xlf
%lang(gl) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.gl.xlf
%lang(he) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.he.xlf
%lang(hr) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.hr.xlf
%lang(hu) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.hu.xlf
%lang(hy) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.hy.xlf
%lang(id) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.id.xlf
%lang(it) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.it.xlf
%lang(ja) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.ja.xlf
%lang(lb) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.lb.xlf
%lang(lt) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.lt.xlf
%lang(lv) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.lv.xlf
%lang(mn) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.mn.xlf
%lang(nb) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.nb.xlf
%lang(nl) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.nl.xlf
%lang(nn) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.nn.xlf
%lang(no) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.no.xlf
%lang(pl) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.pl.xlf
%lang(pt) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.pt.xlf
%lang(pt_BR) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.pt_BR.xlf
%lang(ro) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.ro.xlf
%lang(ru) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.ru.xlf
%lang(sk) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sk.xlf
%lang(sl) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sl.xlf
%lang(sq) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sq.xlf
%lang(sr@cyrillic) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sr_Cyrl.xlf
%lang(sr@latin) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sr_Latn.xlf
%lang(sv) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.sv.xlf
%lang(th) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.th.xlf
%lang(tl) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.tl.xlf
%lang(tr) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.tr.xlf
%lang(uk) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.uk.xlf
%lang(vi) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.vi.xlf
%lang(zh_CN) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.zh_CN.xlf
%lang(zh_TW) %{php_data_dir}/Symfony/Component/Validator/Resources/translations/validators.zh_TW.xlf
