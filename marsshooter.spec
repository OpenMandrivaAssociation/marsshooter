Name:		marsshooter
Version:	0.7.4
Release:	4
License:	GPLv3
Summary:	M.A.R.S. - A Ridiculous Shooter
Url:		http://mars-game.sourceforge.net/
Group:		Games/Arcade
Source0:	http://sourceforge.net/projects/mars-game/files/mars_source_%{version}.tar.gz
Source1:	%{name}.desktop
# PATCH-FIX-UPSTREAM marsshooter-0.7.4-version.patch adam@mizerski.pl -- update version number in CMakeLists.txt
Patch0:		marsshooter-0.7.4-version.patch
Patch1:		marsshooter-0.7.4-cflags.patch
BuildRequires:	cmake
BuildRequires:	sfml2-devel >= 2.0
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	dos2unix

%description
It is a game for two players, flying with ships in a
two-dimensional space setting, governed by the laws of gravity.
It features:
    * awesome 2D-graphics with an unique style
    * a stunning amount of particles
    * single- and multiplayer-support
    * an artificial intelligence using an aggro-system, which
      reacts differentlyupon varying situations
    * many impressive weapons
    * customizable ships
    * a very sexy GUI
    * several game modes: Sacceball, TeamDeathmatch, Cannonkeep,
      Deathmatch, Grave-Itation Pit

%prep
%setup -q -n mars-game
%patch0 -p1
%patch1 -p1
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

%files
%doc credits.txt license.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

