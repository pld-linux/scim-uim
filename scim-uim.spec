Summary:	SCIM IMEngine module based on UIM
Summary(pl.UTF-8):	Moduł silnika IM platformy SCIM oparty na bibliotece UIM
Name:		scim-uim
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	3841556bc0e5a94b1a268751432712d3
Patch0:		%{name}-uim.patch
URL:		http://www.scim-im.org/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.4.0
BuildRequires:	uim-devel >= 1.1.0
Requires:	scim >= 1.4.0
Requires:	uim >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a SCIM IMEngine module which uses UIM input method library as
the backend.

%description -l pl.UTF-8
Ten pakiet zawiera moduł IM platformy SCIM wykorzystujący jako backend
bibliotekę metod wprowadzania UIM.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/IMEngine/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/uim.so
%{_datadir}/scim/icons/scim-uim.png
