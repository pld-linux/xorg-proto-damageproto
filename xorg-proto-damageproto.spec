Summary:	Damage extension headers
Summary(pl):	Nag��wki rozszerzenia Damage
Name:		xorg-proto-damageproto
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/damageproto-%{version}.tar.bz2
# Source0-md5:	33ee591e0b1ca5ad7902934541db7d24
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Damage extension headers.

%description -l pl
Nag��wki rozszerzenia Damage.

%package devel
Summary:	Damage extension headers
Summary(pl):	Nag��wki rozszerzenia Damage
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	damageext

%description devel
Damage extension headers.

%description devel -l pl
Nag��wki rozszerzenia Damage.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog damageproto.txt
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/damageproto.pc
