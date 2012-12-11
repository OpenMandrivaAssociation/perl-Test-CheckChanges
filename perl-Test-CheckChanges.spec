%define upstream_name    Test-CheckChanges
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Check that the Changes file matches the dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module checks that you _Changes_ file has an entry for the current
version of the *Module* being tested.

The version information for the distribution being tested is taken out of
the Build data, or if that is not found, out of the Makefile.

It then attempts to open, in order, a file with the name _Changes_ or
_CHANGES_.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.140.0-3mdv2011.0
+ Revision: 655225
- rebuild for updated spec-helper

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 528120
- rebuild
- import perl-Test-CheckChanges


* Sat Mar 27 2010 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist
