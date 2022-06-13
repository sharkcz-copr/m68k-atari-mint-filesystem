%global debug_package %{nil}

Summary:        MiNT base filesystem and environment
Name:           m68k-atari-mint-filesystem
Version:        4
Release:        1%{?dist}
License:        GPLv2+
URL:            http://vincent.riviere.free.fr/soft/m68k-atari-mint/
Source0:        COPYING
Source1:        macros.m68k-atari-mint
BuildArch:      noarch


%description
This package contains the base filesystem layout, RPM macros and
environment for all m68k-atari-mint packages.


%prep
%setup -q -c -T
cp %{SOURCE0} COPYING


%build
# nothing to do


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.m68k-atari-mint

mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/include
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/lib

# The system root which will contain MiNT native binaries
# and MiNT-specific header files, pkgconfig, etc.
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/include
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/include/sys
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/lib
mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/lib/pkgconfig

mkdir -p $RPM_BUILD_ROOT%{_prefix}/m68k-atari-mint/sys-root/usr/share/man/man{1,2,3,4,5,6,7,8,9}


%files
%license COPYING
%config(noreplace) %{_sysconfdir}/rpm/macros.m68k-atari-mint
%{_prefix}/m68k-atari-mint


%changelog
* Mon Jun 13 2022 Dan Horák <dan[at]danny.cz> - 4-1
- mark COPYING as a license file

* Sat Jan 05 2013 Dan Horák <dan[at]danny.cz> - 3-1
- own man page dirs

* Sun Mar 25 2012 Dan Horák <dan[at]danny.cz> - 2-1
- use macros without underscore
- spec cleanup

* Wed Aug 03 2011 Dan Horák <dan[at]danny.cz> - 1-1
- initial Fedora release
