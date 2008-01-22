Name: x11-driver-input-fpit
Version: 1.1.0
Release: %mkrel 6
Summary: X.org input driver for Fujitsu Stylistic Tablet PCs
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-fpit-1.1.0@mandriva suggested on upstream
# Tag at git checkout 47ecabff271fc1b8dfcc40656934fb70264b7a0e
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-fpit xorg/drivers/xf86-input-fpit
# cd xorg/drivers/xf86-input/fpit
# git-archive --format=tar --prefix=xf86-input-fpit-1.1.0/ xf86-input-fpit-1.1.0@mandriva | bzip2 -9 > xf86-input-fpit-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-fpit-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-fpit-1.1.0@mandriva..origin/mandriva+custom
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Don-t-call-missing-symbol-xf86IsCorePointer.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.

%prep
%setup -q -n xf86-input-fpit-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.*
