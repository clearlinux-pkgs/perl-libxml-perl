#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-libxml-perl
Version  : 0.08
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-0.08.tar.gz
Summary  : Collection of Perl modules for working with XML
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-libxml-perl-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::Parser)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libxml-perl is a collection of Perl modules for working with XML.

%package dev
Summary: dev components for the perl-libxml-perl package.
Group: Development
Provides: perl-libxml-perl-devel = %{version}-%{release}
Requires: perl-libxml-perl = %{version}-%{release}

%description dev
dev components for the perl-libxml-perl package.


%package perl
Summary: perl components for the perl-libxml-perl package.
Group: Default
Requires: perl-libxml-perl = %{version}-%{release}

%description perl
perl components for the perl-libxml-perl package.


%prep
%setup -q -n libxml-perl-0.08
cd %{_builddir}/libxml-perl-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Grove.3
/usr/share/man/man3/Data::Grove::Parent.3
/usr/share/man/man3/Data::Grove::Visitor.3
/usr/share/man/man3/XML::ESISParser.3
/usr/share/man/man3/XML::Handler::CanonXMLWriter.3
/usr/share/man/man3/XML::Handler::Sample.3
/usr/share/man/man3/XML::Handler::Subs.3
/usr/share/man/man3/XML::Handler::XMLWriter.3
/usr/share/man/man3/XML::Parser::PerlSAX.3
/usr/share/man/man3/XML::PatAct::ActionTempl.3
/usr/share/man/man3/XML::PatAct::Amsterdam.3
/usr/share/man/man3/XML::PatAct::MatchName.3
/usr/share/man/man3/XML::PatAct::PatternTempl.3
/usr/share/man/man3/XML::PatAct::ToObjects.3
/usr/share/man/man3/XML::Perl2SAX.3
/usr/share/man/man3/XML::SAX2Perl.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
