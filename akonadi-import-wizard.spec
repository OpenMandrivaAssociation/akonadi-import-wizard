%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc
Name:		akonadi-import-wizard
Version:	23.08.5
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	cmake(KPim5MailImporterAkonadi)
BuildRequires:	cmake(KPim5MessageViewer)
BuildRequires:	cmake(KPim5PimCommonAkonadi)
BuildRequires:	cmake(KPim5Libkdepim)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	boost-devel
Provides:	importwizard = %{EVRD}
Conflicts:	importwizard < 3:16.12
Obsoletes:	importwizard < 3:16.12

%define oldname %mklibname KPimImportWizard 5
%define olddevname %mklibname KPimImportWizard -d
%define libname %mklibname KPim5ImportWizard
%define devname %mklibname KPim5ImportWizard -d

%description
Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc.

%files -f akonadiimportwizard.lang
%{_kde5_applicationsdir}/org.kde.akonadiimportwizard.desktop
%{_bindir}/akonadiimportwizard
%{_datadir}/importwizard/pics/step1.png
%{_docdir}/*/*/importwizard
%{_iconsdir}/hicolor/*/apps/kontact-import-wizard.*
%{_datadir}/qlogging-categories5/importwizard.categories
%{_datadir}/qlogging-categories5/importwizard.renamecategories
%{_libdir}/qt5/plugins/pim5/importwizard/*.so

%package -n %{libname}
Summary:	KDE Pim Import Wizard library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%mklibname importwizard 5
%rename %{oldname}

%description -n %{libname}
KDE Pim Import Wizard library

%files -n %{libname}
%{_libdir}/libKPim5ImportWizard.so.5*

%package -n %{devname}
Summary:	Development files for the KPim import library
Group:	Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files for the KPim import library

%files -n %{devname}
%{_libdir}/libKPim5ImportWizard.so
%{_includedir}/KPim5/ImportWizard
%{_libdir}/cmake/KPimImportWizard
%{_libdir}/cmake/KPim5ImportWizard

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang akonadiimportwizard
