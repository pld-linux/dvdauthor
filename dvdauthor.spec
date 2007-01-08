Summary:	dvdauthor - a program that will generate a DVD movie
Summary(pl):	dvdauthor - program generuj±cy filmy DVD
Name:		dvdauthor
Version:	0.6.12
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
# Source0-md5:	be29593967eb26aa3237bc772b6e1946
URL:		http://dvdauthor.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdauthor is a program that will generate a DVD movie from a valid
MPEG-2 stream that should play when you put it in a DVD player.

%description -l pl
dvdauthor to program generuj±cy z poprawnych strumieni MPEG-2 filmy
DVD, które powinny odtwarzaæ siê po w³o¿eniu do odtwarzacza DVD.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dvdauthor
%{_mandir}/man1/*
