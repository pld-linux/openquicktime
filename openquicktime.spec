Summary:	Library to load, create, manipulate QuickTime files
Summary(pl):	Biblioteka do czytania, robienia i modyfikowania plik�w QuickTime
Name:		openquicktime
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/openquicktime/%{name}-%{version}-src.tgz
URL:		http://openquicktime.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenQuicktime is a small library that allows you to load, create and
manipulate QuickTime files. Audio and video decoding and encoding is
provided using a plug-in mechanism. Unfortunately, there are very few
codecs available by now.

%description -l pl
OpenQuicktime jest ma�� bibliotek� pozwalaj�c� na czytanie, tworzenie
i modyfikowanie plik�w QuickTime. Kodowanie i dekodowanie audio i
video jest obs�ugiwane poprzez mechanizm wtyczek. Niestety na razie
jest dost�pnych tylko kilka codek�w.

%package devel
Summary:	OpenQuicktime development package
Summary(pl):	Pakiet dla programist�w OpenQuicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for OpenQuicktime library.

%description devel -l pl
Pliki nag��wkowe biblioteki OpenQuicktime.

%prep
%setup -q -n %{name}-%{version}-src

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \

mv -f audioplugin/MP3/README README.MP3
gzip -9nf AUTHORS ChangeLog NEWS README* TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/openquicktime
