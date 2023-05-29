%global qt_version 5.15.9
%global kf5_version 5.106.0

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
BuildRequires:  qqc2-breeze-style
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kdbusaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kservice-devel >= %{kf5_version}
BuildRequires:  opt-kf5-knotifications-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kirigami2-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcodecs-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kio-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kitemmodels-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kquickimageeditor-devel 
BuildRequires:  opt-kf5-kquickimageeditor-imports 
BuildRequires:  opt-kf5-libqxmpp
BuildRequires:  zxing-cpp-devel
BuildRequires:  opt-qca-qt5-devel 

%global __requires_exclude ^libQXmppOmemo.*$
%global __requires_exclude ^libqca-qt5.*$
%global __requires_exclude ^libqxmpp.*$
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

Requires:       opt-qt5-qtdeclarative
Requires:       opt-qt5-qtquickcontrols2
Requires:       opt-kf5-kconfig-gui >= %{kf5_version}
Requires:       opt-kf5-kirigami2 >= %{kf5_version}
Requires:       opt-kf5-kirigami-addons >= %{kf5_version}
Requires:       opt-kf5-kcoreaddons >= %{kf5_version}
Requires:       opt-kf5-knotifications >= %{kf5_version}
Requires:       opt-qt5-qtmultimedia
Requires:       opt-qt5-qtlocation
Requires:       opt-qt5-qtlocation-pos-geoclue2
Requires:       opt-qt5-qtlocation-pos-geoclue
Requires:       opt-qt5-qtlocation-pos-positionpoll
Requires:       opt-kf5-libqxmpp 
Requires:       qt-runner
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

