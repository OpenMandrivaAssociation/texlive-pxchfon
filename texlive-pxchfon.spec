Name:		texlive-pxchfon
Version:	68103
Release:	1
Summary:	Japanese font setup for pLaTeX and upLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/pxchfon
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxchfon.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/sfd/pxchfon
%{_texmfdistdir}/fonts/tfm/public/pxchfon
%{_texmfdistdir}/fonts/vf/public/pxchfon
%{_texmfdistdir}/tex/platex/pxchfon
%doc %{_texmfdistdir}/doc/platex/pxchfon

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
