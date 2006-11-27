
Summary:	Mgdiff - graphical front end to the diff
Summary(pl):	Mgdiff - graficzna nak³adka dla diff
Name:		mgdiff
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	da896496dcb9ef2947496472f094b65f
#Source0:	ftp://ftp.x.org/contrib/applications/%{name}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-misc.patch
Patch1:		%{name}-readme.patch
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	XAPPLOADDIR=%{_libdir}/X11/app-defaults \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mgdiff
%config %{_libdir}/X11/app-defaults/Mgdiff
%{_mandir}/man1/*
%{_desktopdir}/mgdiff.desktop
