Name:		marsshooter
Version:	0.7.4
Release:	%mkrel 1
License:	GPLv3
Summary:	M.A.R.S. - A Ridiculous Shooter
Url:		http://mars-game.sourceforge.net/
Group:		Games/Arcade
Source0:	http://sourceforge.net/projects/mars-game/files/mars_source_%{version}.tar.gz
Source1:	%{name}.desktop
# PATCH-FIX-UPSTREAM marsshooter-0.7.4-version.patch adam@mizerski.pl -- update version number in CMakeLists.txt
Patch0:		marsshooter-0.7.4-version.patch
BuildRequires:	cmake
BuildRequires:	fribidi-devel >= 0.19.2
BuildRequires:	gcc-c++
BuildRequires:	hicolor-icon-theme
BuildRequires:	sfml2-devel >= 2.0
BuildRequires:	taglib-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
It is a game for two players, flying with ships in a two-dimensional space setting, governed by the laws of gravity.
It features:
    * awesome 2D-graphics with an unique style
    * a stunning amount of particles
    * single- and multiplayer-support
    * an artificial intelligence using an aggro-system, which reacts differentlyupon varying situations
    * many impressive weapons
    * customizable ships
    * a very sexy GUI
    * several game modes: Sacceball, TeamDeathmatch, Cannonkeep, Deathmatch, Grave-Itation Pit

%prep
%setup -q -n mars-game
%patch0 -p1
chmod -x data/locales/Polish.txt
dos2unix credits.txt license.txt

%build
%cmake
%make VERBOSE=1

%install
install -D -m 755 mars %{buildroot}%{_gamesbindir}/%{name}
install -D -d %{buildroot}%{_gamesdatadir}/%{name}
cp -r data/* %{buildroot}%{_gamesdatadir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -d %{buildroot}%{_datadir}/pixmaps
ln -s %{_gamesdatadir}/%{name}/tex/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc credits.txt license.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

