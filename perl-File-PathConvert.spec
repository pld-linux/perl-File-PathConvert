%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	PathConvert
Summary:	File::PathConvert perl module
Summary(pl):	Modu³ perla File::PathConvert
Name:		perl-File-PathConvert
Version:	0.9
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64e731d1165a0bd5e8f3de93775d7795
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::PathConvert provides functions to convert between a variety of
paths.

%description -l pl
File::PathConvert udostêpnia funkcje konwersji pomiêdzy ró¿nymi
scie¿kami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README mkshadow
%{perl_vendorlib}/File/PathConvert.pm
%{_mandir}/man3/*
