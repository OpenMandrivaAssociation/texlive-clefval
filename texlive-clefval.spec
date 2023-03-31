Name:		texlive-clefval
Version:	55985
Release:	2
Summary:	Key/value support with a hash
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clefval
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clefval.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/clefval
%doc %{_texmfdistdir}/doc/latex/clefval
#- source
%doc %{_texmfdistdir}/source/latex/clefval

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
