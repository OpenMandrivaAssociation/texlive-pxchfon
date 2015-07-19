# revision 30635
# category Package
# catalog-ctan /language/japanese/pxchfon
# catalog-date 2013-05-18 17:41:16 +0200
# catalog-license other-free
# catalog-version 0.7a
Name:		texlive-pxchfon
Version:	0.7a
Release:	9
Summary:	Japanese font setup for pLaTeX and upLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/pxchfon
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pxchfon package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/sfd/pxchfon/PXcjk0.sfd
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-l-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjar-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/cfjas-x-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-l-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjar-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-b-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-r-l0j.tfm
%{_texmfdistdir}/fonts/tfm/public/pxchfon/r-cfjas-x-l0j.tfm
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-b-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-l-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjar-r-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-b-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-r-l0j.vf
%{_texmfdistdir}/fonts/vf/public/pxchfon/cfjas-x-l0j.vf
%{_texmfdistdir}/tex/platex/pxchfon/pxchfon.sty
%{_texmfdistdir}/tex/platex/pxchfon/pxchfon0.def
%{_texmfdistdir}/tex/platex/pxchfon/pxjafont.sty
%doc %{_texmfdistdir}/doc/platex/pxchfon/LICENSE
%doc %{_texmfdistdir}/doc/platex/pxchfon/README-ja
%doc %{_texmfdistdir}/doc/platex/pxchfon/pxchfon.pdf
%doc %{_texmfdistdir}/doc/platex/pxchfon/pxchfon.tex
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-2000jis.pdf
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-2000jis.tex
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-2004jis.pdf
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-2004jis.tex
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-pxchfon.pdf
%doc %{_texmfdistdir}/doc/platex/pxchfon/sample-pxchfon.tex
#- source
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjar-b-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjar-l-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjar-r-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjas-b-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjas-r-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/cfjas-x-l0j.vpl
%doc %{_texmfdistdir}/source/platex/pxchfon/gen-cfja.bat
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjar-b-l0j.pl
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjar-l-l0j.pl
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjar-r-l0j.pl
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjas-b-l0j.pl
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjas-r-l0j.pl
%doc %{_texmfdistdir}/source/platex/pxchfon/r-cfjas-x-l0j.pl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
