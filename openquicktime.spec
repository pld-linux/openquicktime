Summary:	Library to load, create, manipulate QuickTime files
Summary(pl):	Biblioteka do czytania, robienia i modyfikowania plików QuickTime
Name:		openquicktime
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openquicktime/%{name}-%{version}-src.tgz
# Source0-md5: f90bc78b8632c6c254cddf70b4726644
URL:		http://openquicktime.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	glib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenQuicktime is a small library that allows you to load, create and
manipulate QuickTime files. Audio and video decoding and encoding is
provided using a plug-in mechanism. Unfortunately, there are very few
codecs available by now.

%description -l pl
OpenQuicktime jest ma³± bibliotek± pozwalaj±c± na czytanie, tworzenie
i modyfikowanie plików QuickTime. Kodowanie i dekodowanie audio i
video jest obs³ugiwane poprzez mechanizm wtyczek. Niestety na razie
jest dostêpnych tylko kilka codeków.

%package devel
Summary:	OpenQuicktime development package
Summary(pl):	Pakiet dla programistów OpenQuicktime
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for OpenQuicktime library.

%description devel -l pl
Pliki nag³ówkowe biblioteki OpenQuicktime.

%prep
%setup -q -n %{name}-%{version}-src

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \

mv -f audioplugin/MP3/README README.MP3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/openquicktime
