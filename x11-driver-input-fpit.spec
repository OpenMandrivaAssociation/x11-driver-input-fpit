Summary:	X.org input driver for Fujitsu Stylistic Tablet PCs
Name:		x11-driver-input-fpit
Version:	1.4.0
Release:	13
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
Patch0:		fpit-automake-1.13.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.

%prep
%setup -q -n xf86-input-fpit-%{version}
%apply_patches

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_datadir}/X11/xorg.conf.d/*conf
%{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.*

