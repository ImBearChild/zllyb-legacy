# Note: Npm depends on network. Network should be enabled when building this software.

%global debug_package %{nil}

%global forgeurl https://github.com/marktext/marktext/
Version:         0.17.1
%forgemeta

Name:    marktext
Release: 2%{?dist}
Summary: memoA simple and elegant markdown editor, available for Linux, macOS and Windows.
License: MIT
URL:	 %{forgeurl}
Source0: %{forgesource}
Source1: marktext-launcher.sh
Patch0:  marktext-arg-handling.patch

Requires:       electron15
Requires:       ripgrep
BuildRequires:  nodejs
BuildRequires:  /usr/bin/yarn
BuildRequires:  git
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  fontconfig-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libsecret-devel

%description
%{summary}.

%prep
%forgeautosetup -p1

%build
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
yarn
yarn run build:bin

%install
%{__install} -Dm755 %{S:1} %{buildroot}%{_bindir}/marktext

%{__install} -Dm644 build/linux-unpacked/resources/app.asar -t %{buildroot}%{_datadir}/marktext/
%{__cp} -a build/linux-unpacked/resources/{app.asar.unpacked,hunspell_dictionaries} %{buildroot}%{_datadir}/marktext/
ln -sf %{_bindir}/rg %{buildroot}%{_datadir}/marktext/app.asar.unpacked/node_modules/vscode-ripgrep/bin/

%{__install} -Dm644 resources/linux/marktext.appdata.xml -t %{buildroot}%{_datadir}/metainfo/
%{__install} -Dm644 resources/linux/marktext.desktop -t %{buildroot}%{_datadir}/applications/
for size in 16x16 32x32 48x48 64x64 128x128 256x256 512x512; do
    %{__install} -Dm644 resources/icons/${size}/marktext.png -t %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
done

%files
%license    LICENSE
%doc        docs
%{_bindir}/marktext
%{_datadir}/marktext/
%{_datadir}/metainfo/marktext.appdata.xml
%{_datadir}/applications/marktext.desktop
%{_datadir}/icons/hicolor/*/apps/marktext.png

%changelog
* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 0.17.1-2
-  Remove the path of this software

* Tue Mar 22 2022 zhullyb <zhullyb@outlook.com> - 0.17.1-1
- First build.
