Name: ddcui
Version: 0.5.4
Release: 1
Source0: https://github.com/rockowitz/ddcui/archive/refs/tags/v%{version}.tar.gz
Summary: Graphical interface for controlling monitor settings
URL: https://ddcutil.com/
License: GPL-2.0
Group: User interface/Desktops
BuildRequires: cmake(DDCUtil)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(glib-2.0)
BuildSystem: cmake
BuildOption: -DUSE_QT6:BOOL=ON

%patchlist
ddcui-0.5.4-compile.patch

%description
Graphical interface for controlling monitor settings

%files
%{_bindir}/ddcui
%{_prefix}/lib/modules-load.d/ddcui.conf
%{_datadir}/applications/ddcui.desktop
%{_datadir}/icons/hicolor/*/apps/ddcui.*
%{_datadir}/metainfo/ddcui.appdata.xml
%{_mandir}/man1/ddcui.1*
%doc %{_docdir}/ddcui
