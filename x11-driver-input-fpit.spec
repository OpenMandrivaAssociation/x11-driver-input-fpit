%define gitdate %nil

Name: x11-driver-input-fpit
Version: 1.4.0
Release: 6%{?gitdate:.%{gitdate}}
Summary: X.org input driver for Fujitsu Stylistic Tablet PCs
Group: System/X11
URL: http://xorg.freedesktop.org
%if 0%{?gitdate}
Source0: xf86-input-fpit-%{gitdate}.tar.bz2
%else
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-fpit-%{version}.tar.bz2
%endif
Patch0: fpit-automake-1.13.patch
License: MIT
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
%apply_patches

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc COPYING
%{_datadir}/X11/xorg.conf.d/*conf
%{_libdir}/xorg/modules/input/fpit_drv.so
%{_mandir}/man4/fpit.*


%changelog
* Tue Jun 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.4.0-1.mdv2011.0
+ Revision: 687822
- Updated to 1.4.0

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.99-1.20110609
+ Revision: 683675
- Update to latest git snapshot.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5
+ Revision: 671124
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2011.0
+ Revision: 595757
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jan 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-2mdv2010.1
+ Revision: 493596
- Add upstream patch to work with abi 7 (makes package build again)
- Add upstream patch to prevent segfaults
- Remove unused patch
- Don't autoreconf

* Wed Feb 18 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-1mdv2009.1
+ Revision: 342667
- New version 1.3.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265846
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194335
- Update to version 1.2.0.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-7mdv2008.1
+ Revision: 160482
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 156577
- re-enable rpm debug packages support

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 155667
- Added patch to mandriva+custom branch to not call missing symbol
  xf86IsCorePointer. Symbol RRGetRotation is exported from X Server
  now, this symbol is kept on upstream for binary compatibility, so
  Mandriva X Server visibility changes should export it.
- Disable debug package.
  Update BuildRequires.
  Driver still marked as broken and no updates upstream. A fix should be
  to made to "not crash" before 2008.1.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-input-fpit-1.1.0@mandriva suggested on upstream
 Tag at git checkout 47ecabff271fc1b8dfcc40656934fb70264b7a0e
  Notes about this package:
  Currently cooker has an x11-driver-input-fpit at version 1.1.0
  There isn't a 1.1.1 tag, but probably this package should have it's version
  updated.
  There is a fpit-1_1_0 tag upstream, that matches 2008 and current cooker
  version, i.e. the only "broken" symbol is xf86IsCorePointer, but since based
  on the logs the adition of RandR support seens logical and can be disabled
  with a proper option, it is currently also broken due to using older xrandr
  version, and even in the comments it says that probably it would be better
  to use another function/interface.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-4mdv2008.1
+ Revision: 98631
- minor spec cleanup
- build against xserver 1.4

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2008.0
+ Revision: 75661
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

