%global tl_name symbats3
%global tl_revision 63833

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros to use the Symbats3 dingbats fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/symbats3
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/symbats3.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/symbats3.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes available for LaTeX the glyphs in Feorag's OpenType
Symbats3 neopagan dingbats fonts.

