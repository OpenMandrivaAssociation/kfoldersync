%define kdeappsver 164092

Name:				kfoldersync
Version:			2.7.1
Release:			2
Summary:			Folder synchronization and backup tool
License:			GPLv2+
Group:				Archiving/Backup
Url:				https://kde-apps.org/content/show.php/KFolderSync?content=%{kdeappsver}
Source:				http://kde-apps.org/CONTENT/content-files/%{kdeappsver}-%{name}_%{version}.orig.tar.xz

BuildRequires:		desktop-file-utils
BuildRequires:		gettext
BuildRequires:		kdelibs4-devel



%description
Folder synchronization and backup tool for KDE.

%prep
%setup -q
find . -type f -exec chmod 644 {} \;

%build
export CXXFLAGS="%{optflags} -std=gnu++11"
%cmake_kde4 
%make


%install
%makeinstall_std -C build
%find_lang %{name} --with-kde || touch %{name}.lang

%check
for i in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate "$i"
done
chmod -x %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop


%files -f %{name}.lang
%doc COPYING
%{_kde_bindir}/*
%{_kde_appsdir}/*
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_datadir}/applications/kde4/*

