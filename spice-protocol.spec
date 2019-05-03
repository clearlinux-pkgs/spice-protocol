#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice-protocol
Version  : 0.14.0
Release  : 13
URL      : https://gitlab.freedesktop.org/spice/spice-protocol/uploads/f18acfa4a10482062b3f3484bddeb9fa/spice-protocol-0.14.0.tar.bz2
Source0  : https://gitlab.freedesktop.org/spice/spice-protocol/uploads/f18acfa4a10482062b3f3484bddeb9fa/spice-protocol-0.14.0.tar.bz2
Summary  : SPICE protocol headers
Group    : Development/Tools
License  : BSD-3-Clause
Requires: spice-protocol-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pyparsing
BuildRequires : six

%description
spice-protocol
==============
The protocol definition for [SPICE] project used by:
* [spice-server]: A server side library used by [QEMU] and [x11spice];
* [spice-gtk]: A client side library used by [virt-viewer and virt-manager] and
[GNOME Boxes];
* [linux/vd-agent] and [win32/vd-agent]: Guest components for Linux and Windows
* [xf86-video-qxl], [gpu/drm/qxl], [win32/qxl], [win32/qxl-wddm-dod]: Guest video
drivers;

%package dev
Summary: dev components for the spice-protocol package.
Group: Development
Provides: spice-protocol-devel = %{version}-%{release}
Requires: spice-protocol = %{version}-%{release}

%description dev
dev components for the spice-protocol package.


%package license
Summary: license components for the spice-protocol package.
Group: Default

%description license
license components for the spice-protocol package.


%prep
%setup -q -n spice-protocol-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556920833
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1556920833
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spice-protocol
cp COPYING %{buildroot}/usr/share/package-licenses/spice-protocol/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spice-1/spice/barrier.h
/usr/include/spice-1/spice/controller_prot.h
/usr/include/spice-1/spice/end-packed.h
/usr/include/spice-1/spice/enums.h
/usr/include/spice-1/spice/foreign_menu_prot.h
/usr/include/spice-1/spice/ipc_ring.h
/usr/include/spice-1/spice/macros.h
/usr/include/spice-1/spice/protocol.h
/usr/include/spice-1/spice/qxl_dev.h
/usr/include/spice-1/spice/qxl_windows.h
/usr/include/spice-1/spice/start-packed.h
/usr/include/spice-1/spice/stats.h
/usr/include/spice-1/spice/stream-device.h
/usr/include/spice-1/spice/types.h
/usr/include/spice-1/spice/vd_agent.h
/usr/include/spice-1/spice/vdi_dev.h
/usr/lib64/pkgconfig/spice-protocol.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spice-protocol/COPYING
