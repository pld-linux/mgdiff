Summary:	Mgdiff - graphical front end to the diff
Summary(pl):	Mgdiff - graficzna nak³adka dla diff
Name:		mgdiff
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-misc.patch
Patch1:		%{name}-readme.patch
BuildRequires:	motif-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Mgdiff is a graphical front end to the diff command.

%description -l pl
Mgdiff jest graficzn± nak³adk± dla polecenia diff.

%prep
%setup -q -n mgdiff
%patch0 -p0
%patch1 -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	XAPPLOADDIR=%{_libdir}/X11/app-defaults \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/mgdiff
%config %{_libdir}/X11/app-defaults/Mgdiff

%{_mandir}/man1/*
%{_applnkdir}/Utilities/mgdiff.desktop
