#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc
Name:		plasma6-akonadi-import-wizard
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadi-import-wizard/-/archive/%{gitbranch}/akonadi-import-wizard-%{gitbranchd}.tar.bz2#/akonadi-import-wizard-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/akonadi-import-wizard-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6MailImporterAkonadi)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	boost-devel
Provides:	importwizard = %{EVRD}
Conflicts:	importwizard < 3:16.12
Obsoletes:	importwizard < 3:16.12

%define libname %mklibname KPim6ImportWizard
%define devname %mklibname KPim6ImportWizard -d

%description
Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc.

%files -f akonadiimportwizard.lang
%{_datadir}/applications/org.kde.akonadiimportwizard.desktop
%{_bindir}/akonadiimportwizard
%{_datadir}/importwizard/pics/step1.png
%{_docdir}/*/*/importwizard
%{_iconsdir}/hicolor/*/apps/kontact-import-wizard.*
%{_datadir}/qlogging-categories6/importwizard.categories
%{_datadir}/qlogging-categories6/importwizard.renamecategories
%{_libdir}/qt6/plugins/pim6/importwizard/*.so

%package -n %{libname}
Summary:	KDE Pim Import Wizard library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
KDE Pim Import Wizard library

%files -n %{libname}
%{_libdir}/libKPim6ImportWizard.so.*

%package -n %{devname}
Summary:	Development files for the KPim import library
Group:	Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the KPim import library

%files -n %{devname}
%{_libdir}/libKPim6ImportWizard.so
%{_includedir}/KPim6/ImportWizard
%{_libdir}/cmake/KPim6ImportWizard

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-import-wizard-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang akonadiimportwizard
