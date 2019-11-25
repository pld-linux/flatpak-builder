Summary:	Tool for building flatpaks from sources
Summary(pl.UTF-8):	Narzędzie do budowania pakietów flatpak ze źródeł.
Name:		flatpak-builder
Version:	1.0.9
Release:	1
License:	LGPL v2.1+
Group:		Applications
#Source0Download: https://github.com/flatpak/flatpak-builder/releases
Source0:	https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	89c8759aa0b78eb6d029c459f9312255
Patch0:		%{name}-reqs.patch
URL:		https://github.com/flatpak/flatpak-builder
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.13.4
BuildRequires:	curl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl-nons
# or libelf-devel >= 0.8.12
BuildRequires:	elfutils-devel
BuildRequires:	gettext-tools >= 0.18.2
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	json-glib-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.4
BuildRequires:	ostree-devel >= 2017.14
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
Requires:	flatpak >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flatpak-builder is a tool for building flatpaks from sources.

%description -l pl.UTF-8
Flatpak-builder to narzędzie do budowania pakietów flatpak ze źródeł.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libglnx
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	FLATPAK=%{_bindir}/flatpak \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/flatpak-builder

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md doc/{*.css,*.html}
%attr(755,root,root) %{_bindir}/flatpak-builder
%{_mandir}/man1/flatpak-builder.1*
%{_mandir}/man5/flatpak-manifest.5*
