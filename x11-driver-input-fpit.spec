Name: x11-driver-input-fpit
Version: 1.1.0
Release: %mkrel 5
Summary: X.org input driver for Fujitsu Stylistic Tablet PCs
Group: Development/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-fpit  xorg/drivers/xf86-input-fpit
# cd xorg/drivers/xf86-input/fpit
# git-archive --format=tar --prefix=xf86-input-fpit-1.1.0/ master | bzip2 -9 > xf86-input-fpit-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-fpit-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
X.org input driver for Fujitsu Stylistic Tablet PCs. This driver
supports the touchscreen of the Stylistic LT and (with special
options) of the Stylistic 500, 1000 and 2300.
THIS DRIVER IS BROKEN:
Missing symbols xf86IsCorePointer longer present due to X Input Hotplug rework,
and RRGetRotation from previous X Randr version.

%prep
%setup -q -n xf86-input-fpit-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
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