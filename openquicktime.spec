Summary:	Library to load, create, manipulate QuickTime files
Summary(pl):	Biblioteka do czytania, robienia i modyfikowania plikÛw QuickTime
Name:		openquicktime
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
OpenQuicktime jest ma≥± bibliotek± pozwalaj±c± na czytanie, tworzenie
i modyfikowanie plikÛw QuickTime. Kodowanie i dekodowanie audio i
video jest obs≥ugiwane poprzez mechanizm wtyczek. Niestety na razie
jest dostÍpnych tylko kilka codekÛw.

%package devel
Summary:	OpenQuicktime development package
Summary(pl):	Pakiet dla programistÛw OpenQuicktime
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for OpenQuicktime library.

%description devel -l pl
Pliki nag≥Ûwkowe biblioteki OpenQuicktime.

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
