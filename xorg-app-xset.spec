# $Rev: 3418 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xset application
Summary(pl):	Aplikacja xset
Name:		xorg-app-xset
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xset-%{version}.tar.bz2
# Source0-md5:	d8768517c5b49e18aa412cff56f46e9e
Patch0:		xset-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xset-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xset application.

%description -l pl
Aplikacja xset.


%prep
%setup -q -n xset-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
