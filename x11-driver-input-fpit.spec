Name: x11-driver-input-fpit
Version: 1.3.0
Release: %mkrel 3
Summary: X.org input driver for Fujitsu Stylistic Tablet PCs
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
Patch0: xf86-input-fpit-1.3.0-cope-with-xinput-abi-7.patch
Patch1: xf86-input-fpit-1.3.0-fix-module-unloading.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.

%prep
%setup -q -n xf86-input-fpit-%{version}
%patch0 -p1
%patch1 -p1

%build
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
