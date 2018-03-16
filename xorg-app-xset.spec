Summary:	xset application - user preference utility for X
Summary(pl.UTF-8):	Aplikacja xset - narzędzie do ustawień użytkownika dla X
Name:		xorg-app-xset
Version:	1.2.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xset-%{version}.tar.bz2
# Source0-md5:	70ea7bc7bacf1a124b1692605883f620
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXfontcache-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xset program is used to set various user preference options of the
display.

%description -l pl.UTF-8
Program xset służy do ustawiania różnych opcji ekranu przez
użytkownika.

%prep
%setup -q -n xset-%{version}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xset
%{_mandir}/man1/xset.1*
