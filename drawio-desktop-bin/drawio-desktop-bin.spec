Name:           drawio-desktop-bin
Version:        20.2.3
Release:        1%{?dist}
Summary:        Diagram drawing application built on web technology

License:        ASL 2.0
URL:            https://github.com/jgraph/drawio-desktop
Source0:        %{url}/releases/download/v%{version}/drawio-amd64-%{version}.deb
Source1:        https://raw.githubusercontent.com/jgraph/drawio-desktop/release/LICENSE
Source2:        drawio-launcher.sh

Requires:       electron18

%description
%{summary}.

%prep
ar x %{S:0}
tar -xf data.tar.xz

%build
sed -i "s|/opt/drawio/drawio|drawio|g" usr/share/applications/drawio.desktop
cp %{S:1} .

%install
%{__install} -Dm644 opt/drawio/resources/app.asar -t %{buildroot}/%{_datadir}/drawio-desktop
%{__install} -d %{buildroot}%{_datadir}
%{__cp} -a usr/share/{applications,icons,mime} -t %{buildroot}%{_datadir}
%{__install} -Dm755 %{S:2} %{buildroot}%{_bindir}/drawio


%files
%license LICENSE
%{_bindir}/drawio
%{_datadir}/drawio-desktop/app.asar
%{_datadir}/applications/drawio.desktop
%{_datadir}/icons/hicolor/*/apps/drawio.png
%{_datadir}/mime/packages/drawio.xml

%changelog
* Fri Aug 05 2022 zhullyb <zhullyb@outlook.com> - 20.2.3-1
- new version

* Wed Jun 08 2022 zhullyb <zhullyb@outlook.com> - 19.0.3-1
- new version

* Tue Jun 07 2022 zhullyb <zhullyb@outlook.com> - 19.0.2-1
- new version

* Fri Jun 03 2022 zhullyb <zhullyb@outlook.com> - 19.0.0-1
- new version

* Sat May 28 2022 zhullyb <zhullyb@outlook.com> - 18.1.3-1
- new version

* Wed May 18 2022 zhullyb <zhullyb@outlook.com> - 18.0.6-1
- new version

* Sun May 15 2022 zhullyb <zhullyb@outlook.com> - 18.0.4-1
- new version

* Thu May 05 2022 zhullyb <zhullyb@outlook.com> - 18.0.1-1
- new version

* Mon Apr 11 2022 zhullyb <zhullyb@outlook.com> - 17.4.2-1
- new version

* Sun Apr 03 2022 zhullyb <zhullyb@outlook.com> - 17.2.4-2
- Move the path of the software

* Mon Mar 28 2022 zhullyb <zhullyb@outlook.com> - 17.2.4-1
- new version

* Fri Mar 25 2022 zhullyb <zhullyb@outlook.com> - 17.2.1-1
- First build.
