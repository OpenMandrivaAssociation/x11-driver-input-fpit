%define gitdate 20110609

Name: x11-driver-input-fpit
Version: 1.3.99
Release: %mkrel 1.%gitdate
Summary: X.org input driver for Fujitsu Stylistic Tablet PCs
Group: System/X11
URL: http://xorg.freedesktop.org
%if 0%{?gitdate}
Source: xf86-input-fpit-%{gitdate}.tar.bz2
%else
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
%endif
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.

%prep
%if 0%{?gitdate}
%setup -q -n xf86-input-fpit-%{gitdate}
%else
%setup -q -n xf86-input-fpit-%{version}
%endif

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/fpit_drv.la
%{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.*
