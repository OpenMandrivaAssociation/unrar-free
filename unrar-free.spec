Name:           unrar-free
Version:        0.3.1
Release:        1
Summary:        Free software version of the non-free unrar utility
License:        GPL-2.0-or-later
URL:            https://gitlab.com/bgermann/unrar-free
Source:         https://gitlab.com/bgermann/unrar-free/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(libarchive)

%description
unrar-free is a free software version of the non-free unrar utility. This
program is a simple command-line front-end to libarchive, and can list and
extract RAR archives but also other formats supported by libarchive. It does
not rival the non-free unrar in terms of features, but special care has been
taken to ensure it meets most user's needs.

%prep
%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO misc/tarar.pike
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
