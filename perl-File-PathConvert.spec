#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	PathConvert
Summary:	File::PathConvert - convert absolute/relative and logical/physical paths
Summary(pl.UTF-8):	File::PathConvert - konwersja (bez-)względnych i logicznych/fizycznych ścieżek
Name:		perl-File-PathConvert
Version:	0.9
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64e731d1165a0bd5e8f3de93775d7795
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::PathConvert provides functions to convert between absolute and
relative paths, and from logical paths to physical paths on a variety
of filesystems, including the URL 'filesystem'.

*** THIS MODULE (File::PathConvert) IS DEPRECATED. ***

%description -l pl.UTF-8
File::PathConvert udostępnia funkcje do konwersji między ścieżkami
bezwzględnymi i względnymi oraz z logicznych na fizyczne dla wielu
systemów plików, włącznie z "systemem plików" URL.

** TEN MODUŁ (File::PathConvert) JEST ZARZUCONY. ***

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README mkshadow
%{perl_vendorlib}/File/PathConvert.pm
%{_mandir}/man3/*
