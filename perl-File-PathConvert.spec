%include	/usr/lib/rpm/macros.perl
Summary:	File-PathConvert perl module
Summary(pl):	Modu� perla File-PathConvert
Name:		perl-File-PathConvert
Version:	0.85
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-PathConvert-%{version}.tar.gz
Patch0:		perl-File-PathConvert-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-PathConvert provides functions to convert between a variety of
paths.

%description -l pl
File-PathConvert udost�pnia funkcje konwersji pomi�dzy r�nymi
scie�kami.

%prep
%setup -q -n File-PathConvert-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
