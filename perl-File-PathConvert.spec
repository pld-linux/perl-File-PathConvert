%include	/usr/lib/rpm/macros.perl
Summary:	File-PathConvert perl module
Summary(pl):	Modu� perla File-PathConvert
Name:		perl-File-PathConvert
Version:	0.85
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-PathConvert-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz mkshadow
%{perl_sitelib}/File/PathConvert.pm
%{_mandir}/man3/*
