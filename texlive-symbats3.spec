Name:		texlive-symbats3
Version:	63833
Release:	1
Summary:	Macros to use the Symbats3 dingbats fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/symbats3
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/symbats3.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/symbats3.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes available for LaTeX the glyphs in Feorag's
OpenType Symbats3 neopagan dingbats fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/symbats3
%doc %{_texmfdistdir}/doc/fonts/symbats3

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
