#
# spec file for package kaidan
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%global qt_version 5.15.9

Name:           kaidan
Version:        0.9.0
Release:        0
Summary:        A XMPP client based on KDE Framework
License:        GPL-3.0-or-later AND SUSE-GPL-3.0+-with-openssl-exception AND MIT AND AML AND CC-BY-SA-4.0
URL:            https://www.kaidan.im
Source:         kaidan-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-QrCodeDecoder-Replace-deprecated-BarcodeFormat-QR_CO.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-QrCodeGenerator-Replace-deprecated-BarcodeFormat-QR_.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Support-ZXing-2.0.patch
BuildRequires:  cmake >= 3.3
BuildRequires:  extra-cmake-modules >= 5.40.0
BuildRequires:  update-desktop-files
BuildRequires:  gcc-c++
BuildRequires:  qt5-qttools-linguist
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}

BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons-dateandtime
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-kpublictransport-devel
BuildRequires:  qqc2-breeze-stylea
BuildRequires:  opt-kf5-knotifications
BuildRequires:  opt-kf5-libqxmpp 
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel
BuildRequires:  opt-qt5-qtbase-gui
BuildRequires:  opt-qca-qt5-devel
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtlocation
#BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  zxing-cpp-devel
Requires:       opt-qt5-qtquickcontrols2

%description
Kaidan is a simple Jabber/XMPP client providing a user-interface using
Kirigami and QtQuick. The back-end of Kaidan is entirely written in C++
using the qxmpp XMPP client library and Qt 5.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build '-DI18N:BOOL=ON' '-DQUICK_COMPILER:BOOL=ON'
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file im.kaidan.kaidan

%files
%license LICENSE
%doc README.md NEWS
%dir %{_kf5_sharedir}/%{name}
%{_kf5_applicationsdir}/im.kaidan.kaidan.desktop
%{_kf5_appstreamdir}/im.kaidan.kaidan.appdata.xml
%{_kf5_bindir}/%{name}
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.*
%{_kf5_notifydir}/kaidan.notifyrc
%{_kf5_sharedir}/%{name}/images
%{_kf5_sharedir}/%{name}/servers.json

%changelog

