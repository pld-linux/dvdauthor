Summary:	dvdauthor - a program that will generate a DVD movie
Summary(pl.UTF-8):	dvdauthor - program generujący filmy DVD
Name:		dvdauthor
Version:	0.6.14
Release:	10
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
# Source0-md5:	bd646b47950c4091ffd781d43fd2c5e9
URL:		http://dvdauthor.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdauthor is a program that will generate a DVD movie from a valid
MPEG-2 stream that should play when you put it in a DVD player.

%description -l pl.UTF-8
dvdauthor to program generujący z poprawnych strumieni MPEG-2 filmy
DVD, które powinny odtwarzać się po włożeniu do odtwarzacza DVD.

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
%{_mandir}/man1/*.1.*
