%include	/usr/lib/rpm/macros.perl
Summary:	File-PathConvert perl module
Summary(pl):	Modu³ perla File-PathConvert
Name:		perl-File-PathConvert
Version:	0.85
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-PathConvert-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-PathConvert provides functions to convert between a variety of
paths.

%description -l pl
File-PathConvert udostêpnia funkcje konwersji pomiêdzy ró¿nymi
scie¿kami.

%prep
%setup -q -n File-PathConvert-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz mkshadow
%{perl_sitelib}/File/PathConvert.pm
%{_mandir}/man3/*
