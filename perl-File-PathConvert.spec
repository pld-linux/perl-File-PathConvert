%include	/usr/lib/rpm/macros.perl
Summary:	File-PathConvert perl module
Summary(pl):	Modu³ perla File-PathConvert
Name:		perl-File-PathConvert
Version:	0.85
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-PathConvert-%{version}.tar.gz
Patch:		perl-File-PathConvert-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
File-PathConvert provides functions to convert between a variety of paths.

%description -l pl
File-PathConvert udostêpnia funkcje konwersji pomiêdzy ró¿nymi scie¿kami.

%prep
%setup -q -n File-PathConvert-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/PathConvert
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz mkshadow

%{perl_sitelib}/File/PathConvert.pm
%{perl_sitearch}/auto/File/PathConvert

%{_mandir}/man3/*
