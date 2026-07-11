%global tl_name pxchfon
%global tl_revision 79479

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Japanese font setup for pLaTeX and upLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxchfon
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables users to declare in their document which physical
fonts should be used for the standard Japanese (logical) fonts of pLaTeX
and upLaTeX. Font setup is realized by changing the font mapping of
dvipdfmx, and thus users can use any (monospaced) physical fonts they
like, once they properly install this package, without creating helper
files for each new font. This package also supports setup for the fonts
used in the japanese-otf package. System requirements: TeX format:
LaTeX. TeX engine: pTeX or upTeX. DVIware: dvipdfmx. Prerequisite
packages: atbegshi.

