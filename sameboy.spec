%define _empty_manifest_terminate_build 0
%define oname SameBoy

Name:           sameboy
Version:        1.0.1
Release:        1
Summary:        Game Boy and Game Boy Color emulator written in C
Group:          Emulator/Games
License:        MIT
URL:            https://github.com/LIJI32/SameBoy
Source0:        https://github.com/LIJI32/SameBoy/archive/v%{version}/%{oname}-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires: make
BuildRequires: rgbds
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(gl)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)

%description
SameBoy is an open source Game Boy (DMG) and Game Boy Color (CGB) emulator,
written in portable C. It has a native Cocoa front-end for MacOS,
an SDL front-end for other operating systems, and a libretro core.
It also includes a text-based debugger with expression evaluation.

%prep
%autosetup -n SameBoy-%{version}

%build
%make_build sdl DATA_DIR=%{_datadir}/%{name}/


%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{_datadir}

%make_install FREEDESKTOP=true \
              PREFIX=%{_prefix} \
              DATA_DIR=%{_datadir}/%{name}/

cd FreeDesktop

cp %{name}.desktop %{name}-terminal.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install \
    --set-key=Name --set-value='SameBoy (Terminal)' \
    --set-key=Terminal --set-value='true' \
    --dir=%{buildroot}/%{_datadir}/applications \
    %{name}-terminal.desktop

%files
%{_bindir}/sameboy-thumbnailer
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.sym
%{_datadir}/%{name}/background.bmp
%dir %{_datadir}/%{name}/Shaders
%{_datadir}/%{name}/Shaders/*.fsh
%{_datadir}/%{name}/LICENSE
%{_datadir}/sameboy/Palettes
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-terminal.desktop
%{_datadir}/mime/sameboy.xml
%{_datadir}/thumbnailers/sameboy.thumbnailer
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/x-gameboy*rom.png
%license LICENSE
%doc README.md
