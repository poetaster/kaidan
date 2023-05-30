Name:           kaidan
Version:        0.8.0
Release:        0
Summary:        A XMPP client based on KDE Framework
License:        GPL-3.0-or-later AND SUSE-GPL-3.0+-with-openssl-exception AND MIT AND AML AND CC-BY-SA-4.0
URL:            https://www.kaidan.im
Source:         kaidan-%{version}.tar.xz
Source2:        org.kde.kaidan.png


# PATCH-FIX-UPSTREAM
#Patch0:         0001-QrCodeDecoder-Replace-deprecated-BarcodeFormat-QR_CO.patch
# PATCH-FIX-UPSTREAM
#Patch1:         0001-QrCodeGenerator-Replace-deprecated-BarcodeFormat-QR_.patch
# PATCH-FIX-UPSTREAM
#Patch2:         0001-Support-ZXing-2.0.patch
# SFOS
Patch0:          0001-remove-qq2-desktop-style.patch
Patch1:          0002-desktop-qtrunner.patch

%global __requires_exclude ^libQXmppOmemo.*$
%global __requires_exclude ^libqca-qt5.*$
%global __requires_exclude ^libqxmpp.*$

%{?opt_kf5_default_filter}

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.3
BuildRequires:  extra-cmake-modules >= 5.40.0
BuildRequires:  qt5-qttools-linguist
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  opt-qt5-qtbase-devel  
BuildRequires:  opt-qt5-qttools-devel 
BuildRequires:  opt-qt5-qtbase-gui 
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtlocation-devel
BuildRequires:  opt-qt5-qtlocation-pos-geoclue2
BuildRequires:  opt-qt5-qtlocation-pos-geoclue
BuildRequires:  opt-qt5-qtlocation-pos-positionpoll
BuildRequires:  opt-kf5-kwindowsystem-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons
BuildRequires:  opt-kf5-kcoreaddons-devel 
BuildRequires:  opt-kf5-kdbusaddons-devel 
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kservice-devel 
BuildRequires:  opt-kf5-knotifications-devel 
BuildRequires:  opt-kf5-kcodecs-devel 
BuildRequires:  opt-kf5-kio-devel 
BuildRequires:  opt-kf5-kconfig-devel 
BuildRequires:  opt-kf5-ki18n-devel 
BuildRequires:  opt-kf5-kitemmodels-devel 
BuildRequires:  opt-kf5-kquickimageeditor-devel 
BuildRequires:  opt-kf5-kquickimageeditor-imports 
BuildRequires:  opt-kf5-libqxmpp
BuildRequires:  zxing-cpp-devel
BuildRequires:  opt-qca-qt5-devel 

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

Requires: opt-kf5-kirigami2%{_isa} 
Requires: opt-qt5-qtwayland%{_isa}
Requires: opt-kf5-kconfig-gui
Requires: opt-kf5-kcoreaddons
Requires: opt-kf5-kdbusaddons
Requires: opt-kf5-ki18n
Requires: opt-kf5-kirigami2
Requires: opt-kf5-kirigami-addons
Requires: opt-kf5-knotifications
Requires: opt-kf5-kwindowsystem
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtmultimedia
Requires: opt-qt5-qtquickcontrols2
Requires: opt-qt5-qtsvg
Requires: opt-qt5-qtwebengine
Requires: opt-qt5-qtlocation
Requires: qt-runner
Requires: breeze-icons

Requires:       opt-kf5-kquickimageeditor-imports 
Requires:       opt-kf5-libqxmpp 
Requires:       libomemo-c

%description
Kaidan is a simple Jabber/XMPP client providing a user-interface using
Kirigami and QtQuick. The back-end of Kaidan is entirely written in C++
using the qxmpp XMPP client library and Qt 5.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/ \
        -DI18N:BOOL=ON \
        -DQUICK_COMPILER:BOOL=OFF

%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}/%{_datadir}/applications/im.kaidan.kaidan.desktop

install -p -m644 -D %{SOURCE2} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/im.kaidan.kaidan.png

%files
%license LICENSE
%doc README.md NEWS
%dir %{_datadir}/%{name}
%dir %{_datadir}/knotifications5
%{_bindir}/%{name}
%{_datadir}/applications/im.kaidan.kaidan.desktop
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/images
%{_datadir}/%{name}/servers.json
%{_opt_kf5_metainfodir}/im.kaidan.kaidan.appdata.xml
%{_datadir}/knotifications5/kaidan.notifyrc

%changelog

