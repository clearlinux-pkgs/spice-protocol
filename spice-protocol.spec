#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice-protocol
Version  : 0.12.12
Release  : 6
URL      : http://www.spice-space.org/download/releases/spice-protocol-0.12.12.tar.bz2
Source0  : http://www.spice-space.org/download/releases/spice-protocol-0.12.12.tar.bz2
Summary  : SPICE protocol headers
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : pyparsing
BuildRequires : six

%description


%package dev
Summary: dev components for the spice-protocol package.
Group: Development
Provides: spice-protocol-devel

%description dev
dev components for the spice-protocol package.


%prep
%setup -q -n spice-protocol-0.12.12

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spice-1/spice/barrier.h
/usr/include/spice-1/spice/controller_prot.h
/usr/include/spice-1/spice/end-packed.h
/usr/include/spice-1/spice/enums.h
/usr/include/spice-1/spice/error_codes.h
/usr/include/spice-1/spice/foreign_menu_prot.h
/usr/include/spice-1/spice/ipc_ring.h
/usr/include/spice-1/spice/macros.h
/usr/include/spice-1/spice/protocol.h
/usr/include/spice-1/spice/qxl_dev.h
/usr/include/spice-1/spice/qxl_windows.h
/usr/include/spice-1/spice/start-packed.h
/usr/include/spice-1/spice/stats.h
/usr/include/spice-1/spice/types.h
/usr/include/spice-1/spice/vd_agent.h
/usr/include/spice-1/spice/vdi_dev.h
/usr/lib64/pkgconfig/*.pc
