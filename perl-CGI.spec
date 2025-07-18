#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v27
# autospec commit: 65cf152
#
Name     : perl-CGI
Version  : 4.70
Release  : 64
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-4.70.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-4.70.tar.gz
Summary  : 'Handle Common Gateway Interface requests and responses'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-CGI-license = %{version}-%{release}
Requires: perl-CGI-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::NoWarnings)
BuildRequires : perl(Test::Warn)
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
CGI - Handle Common Gateway Interface requests and responses
# SYNOPSIS
use strict;
use warnings;

%package dev
Summary: dev components for the perl-CGI package.
Group: Development
Provides: perl-CGI-devel = %{version}-%{release}
Requires: perl-CGI = %{version}-%{release}

%description dev
dev components for the perl-CGI package.


%package license
Summary: license components for the perl-CGI package.
Group: Default

%description license
license components for the perl-CGI package.


%package perl
Summary: perl components for the perl-CGI package.
Group: Default
Requires: perl-CGI = %{version}-%{release}

%description perl
perl components for the perl-CGI package.


%prep
%setup -q -n CGI-4.70
cd %{_builddir}/CGI-4.70
pushd ..
cp -a CGI-4.70 buildavx2
popd

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CGI
cp %{_builddir}/CGI-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-CGI/4ddbe6ac3bfaee77fb2e3a1c0d53f744891f2aad || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CGI.3
/usr/share/man/man3/CGI::Carp.3
/usr/share/man/man3/CGI::Cookie.3
/usr/share/man/man3/CGI::HTML::Functions.3
/usr/share/man/man3/CGI::Pretty.3
/usr/share/man/man3/CGI::Push.3
/usr/share/man/man3/CGI::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CGI/4ddbe6ac3bfaee77fb2e3a1c0d53f744891f2aad

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
