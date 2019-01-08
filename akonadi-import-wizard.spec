%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc
Name:		akonadi-import-wizard
Version:	18.12.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5MailImporterAkonadi)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	boost-devel
Provides:	importwizard = %{EVRD}
Conflicts:	importwizard < 3:16.12
Obsoletes:	importwizard < 3:16.12

%define libname %mklibname KPimImportWizard 5
%define devname %mklibname KPimImportWizard -d

%description
Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc.

%files -f akonadiimportwizard.lang
%{_kde5_applicationsdir}/org.kde.akonadiimportwizard.desktop
%{_bindir}/akonadiimportwizard
%{_datadir}/importwizard/pics/step1.png
%{_datadir}/kconf_update/importwizard*
%{_docdir}/*/*/importwizard
%{_iconsdir}/hicolor/*/apps/kontact-import-wizard.*
%{_sysconfdir}/xdg/importwizard.categories
%{_sysconfdir}/xdg/importwizard.renamecategories
%{_libdir}/qt5/plugins/importwizard

%package -n %{libname}
Summary:	KDE Pim Import Wizard library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%mklibname importwizard 5

%description -n %{libname}
KDE Pim Import Wizard library

%files -n %{libname}
%{_libdir}/libKPimImportWizard.so.5*

%package -n %{devname}
Summary:	Development files for the KPim import library
Group:	Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the KPim import library

%files -n %{devname}
%{_libdir}/libKPimImportWizard.so
%{_includedir}/KF5/KPim/ImportWizard
%{_includedir}/KF5/KPim/importwizard
%{_includedir}/KPim/importwizard_version.h
%{_libdir}/cmake/KPimImportWizard

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang akonadiimportwizard
