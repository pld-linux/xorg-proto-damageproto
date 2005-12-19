Summary:	Damage protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Damage i pomocnicze
Name:		xorg-proto-damageproto
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/proto/damageproto-%{version}.tar.bz2
# Source0-md5:	9b0b8b18259d67ec868336ca5bfd5228
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Damage protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Damage i pomocnicze.

%package devel
Summary:	Damage protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Damage i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel
Obsoletes:	damageext

%description devel
Damage protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Damage i pomocnicze.

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
%doc ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/damageproto.pc
