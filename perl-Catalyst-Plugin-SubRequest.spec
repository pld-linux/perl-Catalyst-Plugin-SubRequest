#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-SubRequest
Summary:	Catalyst::Plugin::SubRequest - Make subrequests to actions in Catalyst
#Summary(pl.UTF-8):	
Name:		perl-Catalyst-Plugin-SubRequest
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MR/MRAMBERG/Catalyst-Plugin-SubRequest-0.10.tar.gz
# Source0-md5:	1b706b07d4270188516c0a97a6375cfc
URL:		http://search.cpan.org/dist/Catalyst-Plugin-SubRequest/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(File::Slurp)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make subrequests to actions in Catalyst. Uses the  catalyst
dispatcher, so it will work like an external url call.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
