Summary:	Damage extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Damage
Name:		xorg-proto-damageproto
Version:	1.2.1
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/damageproto-%{version}.tar.bz2
# Source0-md5:	998e5904764b82642cc63d97b4ba9e95
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Damage extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Damage.

%package devel
Summary:	Damage extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Damage
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	damageext

%description devel
Damage extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Damage.

%prep
%setup -q -n damageproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README damageproto.txt
%{_includedir}/X11/extensions/damage*.h
%{_pkgconfigdir}/damageproto.pc
