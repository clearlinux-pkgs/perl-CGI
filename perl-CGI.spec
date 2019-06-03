#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CGI
Version  : 4.44
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-4.44.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-4.44.tar.gz
Summary  : Handle Common Gateway Interface requests and responses
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-CGI-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::NoWarnings)
BuildRequires : perl(Test::Warn)

%description
# NAME
CGI - Handle Common Gateway Interface requests and responses
<div>
<a href='https://travis-ci.org/leejo/CGI.pm?branch=master'><img src='https://travis-ci.org/leejo/CGI.pm.svg?branch=master' alt='Build Status' /></a>
<a href='https://coveralls.io/r/leejo/CGI.pm'><img src='https://coveralls.io/repos/leejo/CGI.pm/badge.png?branch=master' alt='Coverage Status' /></a>
</div>

%package dev
Summary: dev components for the perl-CGI package.
Group: Development
Provides: perl-CGI-devel = %{version}-%{release}
Requires: perl-CGI = %{version}-%{release}
Requires: perl-CGI = %{version}-%{release}

%description dev
dev components for the perl-CGI package.


%package license
Summary: license components for the perl-CGI package.
Group: Default

%description license
license components for the perl-CGI package.


%prep
%setup -q -n CGI-4.44

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CGI
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-CGI/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/CGI.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI.pod
/usr/lib/perl5/vendor_perl/5.28.2/CGI/Carp.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/Cookie.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/File/Temp.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/HTML/Functions.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/HTML/Functions.pod
/usr/lib/perl5/vendor_perl/5.28.2/CGI/Pretty.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/Push.pm
/usr/lib/perl5/vendor_perl/5.28.2/CGI/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/Fh.pm

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
/usr/share/package-licenses/perl-CGI/LICENSE
