Summary:	Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc
Name:		akonadi-import-wizard
Version:	17.04.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	boost-devel
Provides:	importwizard = %{EVRD}
Conflicts:	importwizard < 3:16.12
Obsoletes:	importwizard < 3:16.12

%description
Import Wizard allows to migrate data from mailer as Thunderbird/Evolution etc.

%files -f importwizard.lang
%{_kde5_applicationsdir}/org.kde.importwizard.desktop
%{_bindir}/importwizard
%{_datadir}/importwizard/pics/step1.png
%{_datadir}/kconf_update/importwizard*
%{_docdir}/*/*/importwizard
%{_iconsdir}/hicolor/*/apps/kontact-import-wizard.*
%{_sysconfdir}/xdg/importwizard.categories
%{_sysconfdir}/xdg/importwizard.renamecategories

%dependinglibpackage importwizard 5

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang importwizard
