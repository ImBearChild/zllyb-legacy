%define         _electronver        electron20

Name:           nodejs-%{_electronver}-bin
Version:        20.0.2
Release:        1%{?dist}
Summary:        Build cross-platform desktop apps with JavaScript, HTML, and CSS
License:        MIT
Url:            https://github.com/electron/electron
Source0:        %{url}/releases/download/v%{version}/electron-v%{version}-linux-x64.zip
Source1:        electron-launcher.sh
Source2:        https://raw.githubusercontent.com/electron/electron/main/LICENSE

BuildRequires:  bsdtar

Provides:       nodejs-%{_electronver} %{_electronver}

AutoReqProv: no

%description
Build cross-platform desktop apps with JavaScript, HTML, and CSS

%prep
install -Dm644 %{S:2} %{_builddir}/

%build
sed -i "s|@ELECTRONVER@|%{_electronver}|" %{S:1}

%install
install -dm755 %{buildroot}%{_datadir}/%{_electronver}
bsdtar -xf %{SOURCE0} -C %{buildroot}%{_datadir}/%{_electronver}

chmod u+s %{buildroot}%{_datadir}/%{_electronver}/chrome-sandbox

install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{_electronver}

%files
%license LICENSE
%{_bindir}/%{_electronver}
%{_datadir}/%{_electronver}/

%changelog
* Thu Aug 11 2022 zhullyb <zhullyb@outlook.com> - 20.0.2-1
- new version

* Tue Aug 02 2022 zhullyb <zhullyb@outlook.com> - 20.0.0-1
- new version
