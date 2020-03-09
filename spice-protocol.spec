#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice-protocol
Version  : 0.14.1
Release  : 14
URL      : https://gitlab.freedesktop.org/spice/spice-protocol/uploads/a6996e70f63cbfa0327b44d23003b87e/spice-protocol-0.14.1.tar.bz2
Source0  : https://gitlab.freedesktop.org/spice/spice-protocol/uploads/a6996e70f63cbfa0327b44d23003b87e/spice-protocol-0.14.1.tar.bz2
Summary  : Spice protocol header files
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1+
Requires: spice-protocol-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pyparsing
BuildRequires : six

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

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
%setup -q -n spice-protocol-0.14.1
cd %{_builddir}/spice-protocol-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583787442
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1583787442
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spice-protocol
cp %{_builddir}/spice-protocol-0.14.1/COPYING %{buildroot}/usr/share/package-licenses/spice-protocol/7e915fa295db356dc2f82929681d82ac4f7f961d
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
/usr/lib64/pkgconfig/spice-protocol.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spice-protocol/7e915fa295db356dc2f82929681d82ac4f7f961d
