%{?scl:%scl_package perl-Unicode-UTF8}

# Rebuild build script using Module::Install::ReadmeFromPod
%if "%{?rhel}" != "6" && ! (0%{?scl:1})
%bcond_without perl_Unicode_UTF8_enables_Module_Install_ReadmeFromPod
%else
%bcond_with perl_Unicode_UTF8_enables_Module_Install_ReadmeFromPod
%endif
# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Unicode_UTF8_enables_optional_test
%else
%bcond_with perl_Unicode_UTF8_enables_optional_test
%endif

Summary:	Encoding and decoding of UTF-8 encoding form
Name:		%{?scl_prefix}perl-Unicode-UTF8
Version:	0.62
Release:	11%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Unicode-UTF8
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Unicode-UTF8-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl-devel
BuildRequires:	%{?scl_prefix}perl-generators
%if %{with perl_Unicode_UTF8_enables_Module_Install_ReadmeFromPod}
BuildRequires:	%{?scl_prefix}perl(inc::Module::Install)
BuildRequires:	%{?scl_prefix}perl(Module::Install::ReadmeFromPod)
%else
BuildRequires:	%{?scl_prefix}perl(base)
BuildRequires:	%{?scl_prefix}perl(Config)
BuildRequires:	%{?scl_prefix}perl(Cwd)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(Fcntl)
BuildRequires:	%{?scl_prefix}perl(File::Basename)
BuildRequires:	%{?scl_prefix}perl(File::Find)
BuildRequires:	%{?scl_prefix}perl(File::Path)
BuildRequires:	%{?scl_prefix}perl(Pod::Text)
BuildRequires:	%{?scl_prefix}perl(vars)
%endif
# Module Runtime
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(warnings)
BuildRequires:	%{?scl_prefix}perl(XSLoader)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(Encode) >= 1.9801
BuildRequires:	%{?scl_prefix}perl(IO::File)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Scalar::Util)
BuildRequires:	%{?scl_prefix}perl(Test::Builder)
BuildRequires:	%{?scl_prefix}perl(Test::Fatal) >= 0.006
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.47
%if %{with perl_Unicode_UTF8_enables_optional_test}
# Optional Tests
BuildRequires:	%{?scl_prefix}perl(Taint::Runtime) >= 0.03
BuildRequires:	%{?scl_prefix}perl(Test::LeakTrace) >= 0.10
BuildRequires:	%{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:	%{?scl_prefix}perl(Variable::Magic)
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:	%{?scl_prefix}perl(Exporter)
Requires:	%{?scl_prefix}perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides functions to encode and decode UTF-8 encoding form as
specified by Unicode and ISO/IEC 10646:2011.

%prep
%setup -q -n Unicode-UTF8-%{version}

# Unbundle inc::Module::Install, we'll use system version instead
# unless we're on EL-6, where there's no Module::Install::ReadmeFromPod
%if %{with perl_Unicode_UTF8_enables_Module_Install_ReadmeFromPod}
rm -rf inc/
%endif

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorarch}/Unicode/
%{perl_vendorarch}/auto/Unicode/
%{_mandir}/man3/Unicode::UTF8.3*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-11
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-2
- Perl 5.26 rebuild

* Wed Apr 12 2017 Paul Howarth <paul@city-fan.org> - 0.62-1
- Update to 0.62
  - Only check for missing Module::Install related modules in Makefile.PL

* Mon Apr 10 2017 Paul Howarth <paul@city-fan.org> - 0.61-1
- Update to 0.61
  - Avoid relying on current working directory being in @INC
  - Documentation typo fixes
- Drop redundant Group: tag
- Simplify find commands using -empty and -delete

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-5
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 25 2013 Paul Howarth <paul@city-fan.org> - 0.60-1
- Update to 0.60
  - Added valid_utf8()
  - Skip copy-on-write tests on Perl 5.19

* Mon Sep  2 2013 Paul Howarth <paul@city-fan.org> - 0.59-3
- BR: perl(Scalar::Util) for the test suite (#1003650)
- Add buildreqs for deps of bundled inc::Module::Install for EL-6 build

* Mon Sep  2 2013 Paul Howarth <paul@city-fan.org> - 0.59-2
- Sanitize for Fedora submission

* Mon Sep  2 2013 Paul Howarth <paul@city-fan.org> - 0.59-1
- Initial RPM build
