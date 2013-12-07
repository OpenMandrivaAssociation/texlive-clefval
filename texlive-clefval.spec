# revision 16549
# category Package
# catalog-ctan /macros/latex/contrib/clefval
# catalog-date 2006-12-07 15:13:33 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-clefval
Version:	20061207
Release:	6
Summary:	Key/value support with a hash
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clefval
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides only two macros viz. \TheKey and
\TheValue to define then use pairs of key/value and gives a
semblance of a hash. Syntax: \TheKey{key}{value} to define the
value associated to the key, does not produce text;
\TheValue{key} to return the value linked to the key. Both
arguments of \TheKey are 'moving' as LaTeX defines the term and
we have sometimes to protect them.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/clefval/clefval.sty
%doc %{_texmfdistdir}/doc/latex/clefval/Changements
%doc %{_texmfdistdir}/doc/latex/clefval/Changes
%doc %{_texmfdistdir}/doc/latex/clefval/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/clefval/README
%doc %{_texmfdistdir}/doc/latex/clefval/clefval.pdf
%doc %{_texmfdistdir}/doc/latex/clefval/example.pdf
%doc %{_texmfdistdir}/doc/latex/clefval/example.tex
%doc %{_texmfdistdir}/doc/latex/clefval/exemple.pdf
%doc %{_texmfdistdir}/doc/latex/clefval/exemple.tex
#- source
%doc %{_texmfdistdir}/source/latex/clefval/Makefile
%doc %{_texmfdistdir}/source/latex/clefval/clefval.dtx
%doc %{_texmfdistdir}/source/latex/clefval/clefval.ins
%doc %{_texmfdistdir}/source/latex/clefval/fra-clefval.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061207-2
+ Revision: 750252
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061207-1
+ Revision: 718069
- texlive-clefval
- texlive-clefval
- texlive-clefval
- texlive-clefval
- texlive-clefval

