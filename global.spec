#
# Conditional build:
%bcond_without	pgsql		# without PostgreSQL support
%bcond_without	home_etc	# don't use home_etc
#				# (btw, home-etc is supported here by profile.d hooks)
Summary:	GNU GLOBAL - Common source code tag system
Summary(pl):	GNU GLOBAL - system list odwo³añ powszechnego u¿ytku
Name:		global
Version:	4.6
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/global/%{name}-%{version}.tar.gz
# Source0-md5:	513418bc88a7c0051992b5345bae10bc
Patch10:	%{name}-acinclude-fix.patch
Patch20:	%{name}-pgsql-shared.patch
Patch30:	%{name}-globash-altercfg.patch
URL:		http://www.gnu.org/software/global/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	xemacs
Requires:	coreutils
Requires:	findutils
%{?with_home_etc:Requires:	home-etc >= 1.0.8}
Provides:	gtags-%{version}-%{release}
Provides:	htags-%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code. You can locate the specified function or method
in source files and move there easily. It is useful to hack a large
project containing many subdirectories, many general, main()-type
functions. It allows you to create one tags container for a big code
tree.
%if %{with pgsql}

Tagging information may be keeped in the traditional db files, or shared
using the PostgreSQL database.
%endif

You can also find some subpackages, containing support for additional
GLOBAL's features, and for compliance with common code editors (symbols' completion,
jumping).

%description -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo³añ dla
kodów ¼ród³owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Mo¿esz z jego pomoc± odszukaæ podan± funkcjê lub metodê w plikach
¼ród³owych i w ³atwy sposób siê do niej przenie¶æ. Narzêdzie to jest
przydatne do d³ubania w du¿ych projektach, zawieraj±cych mnóstwo
podkatalogów, wiele funkcji g³ównych w stylu main(). Pozwala Ci on
utworzyæ jeden kontener ze znacznikami dla du¿ego drzewa kodu.
%if %{with pgsql}

Informacje o znacznikach mog± byæ przechowywane w postaci plików db,
lub te¿ wspó³dzielone przy pomocy bazy danych PostgreSQL.
%endif

Mo¿esz tak¿e znale¼æ kilka podpakietów, które zawieraj± wsparcie
dla dodatkowych mechanizmów GLOBAL, a tak¿e pozwalaj± na wspó³pracê
ze niektórymi znanymi edytorami kodu (dope³nianie nazw symboli, przeskakiwanie).

%package htags
Summary:	GNU GLOBAL - programs for making hypertext from source code
Summary(pl):	GNU GLOBAL - programy produkuj±ce hypertext z kodów ¼ród³owych
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl-base >= 5.005
Provides:	gozilla-%{version}-%{release}
Provides:	htags-%{version}-%{release}

%description htags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

Htags makes hypertext from source code. The package also contains the
gozilla wrapper, which enforces Mozilla-based web browsers to display
source code in an elegant way. Htags can also work with a CVS
repository, which makes it more easy to navigate though the code over
the Web.

%description htags -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo³añ dla
kodów ¼ród³owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Htags jest narzêdziem generuj±cym hypertext z kodów. Pakiet ten
zawiera tak¿e program wyskakuj±cy o nazwie gozilla, który zmusza
przegl±darki bazuj±ce na Mozilla, aby wy¶wietla³y kod ¼ród³owy w
elegancki sposób. Htags potrafi równie¿ wspó³pracowaæ z repozytorium
CVS u³atwiaj±c nawigacjê w kodach poprzez WWW.

%package gtags-perl-wrapper
Summary:	GNU GLOBAL - gtags wrapper for tools which use Perl
Summary(pl):	GNU GLOBAL - program pomocniczy dla narzêdzi u¿ywaj±cych Perl
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl-base >= 5.005
Provides:	gtags-perl-wrapper-%{version}-%{release}

%description gtags-perl-wrapper
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package contains simple Perl wrapper, which allows to use the
system for some tools and editors.

%description gtags-perl-wrapper -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo³añ dla
kodów ¼ród³owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet zawiera program pomocniczy, który pozwala u¿ywaæ tego
systemu niektórym narzêdziom i edytorom.

%package globash
Summary:	GNU GLOBAL - Bash customization to walk though the source trees
Summary(pl):	GNU GLOBAL - usprawnienie dla Bash do poruszania siê po drzewach ¼róde³
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	bash >= 2.05
Provides:	globash-%{version}-%{release}

%description globash
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows you to invoke a customized Bash with features that
makes easy to navigate in the sources trees. These are: Vi-like tag
stack, Emacs-like tag name completion, editor or viewer automatic
invocation, tag mark facility, and a cookie facility for managing
directories.

%description globash -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo³añ dla
kodów ¼ród³owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala wywo³ywaæ odpowiednio przystosowan± wersjê pow³oki
Bash z udogodnieniami, które czyni± nawigowanie po drzewku ¼róde³
rzecz± ³atw±. Do tych udogodnieñ nale¿±: stos znaczników w stylu Vi,
dope³nianie nazw w styly edytora Emacs, automatyczne wywo³ywanie
edytorów lub przegl±darek, mechanizm wyró¿niania znaczników, oraz
mechanizm ciasteczek pomagaj±cy zarz±dzaæ katalogami.

%package -n xemacs-gtags-mode-pkg
Summary:	XEmacs mode for the GNU GLOBAL source tag system
Summary(pl):	Tryb systemu list odwo³añ GNU GLOBAL dla edytora XEmacs
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description -n xemacs-gtags-mode-pkg
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows to integrate the GLOBAL source tag system with the
XEmacs editor.

%description -n xemacs-gtags-mode-pkg -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo³añ dla
kodów ¼ród³owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala zintegrowaæ system GLOBAL z edytorem XEmacs.

%prep
%setup -q
%patch10 -p1
%patch20 -p1
%patch30 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_pgsql:--with-postgres=%{_prefix}} \
	%{?with_home_etc:--with-home-etc}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/gtags \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags \
	$RPM_BUILD_ROOT/etc/profile.d

# perl wrapper
cp gtags.pl $RPM_BUILD_ROOT%{_bindir}

# globash
cp globash.rc $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# default config
cp gtags.conf $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# emacs support
cp gtags.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags/gtags.el
find $RPM_BUILD_ROOT%{_datadir} -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

# /etc/profile.d hooks for globash
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/globash.sh
%if %{with home_etc}
GLOBASH_HOME="\$HOME_ETC"
export GLOBASH_HOME
%endif
alias globash='/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF
%if %{with home_etc}
set GLOBASH_HOME = "\$HOME_ETC"
setenv GLOBASH_HOME
%endif
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/globash.csh
alias globash '/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/profile.d hooks for home-etc support
# note: naming convention home-etc_hook-* makes us sure that
#       the scriptlet will occur _after_ home-etc main scriptlet
%if %{with home_etc}
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/home-etc_hook-global.sh
GTAGSCONF="\$HOME_ETC/.globalrc"
export GTAGSCONF
EOF
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/home-etc_hook-global.csh
set GTAGSCONF = "\$HOME_ETC/.globalrc"
setenv GTAGSCONF
EOF
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ LICENSE NEWS README THANKS
%attr(755,root,root) %{_bindir}/g*tags
%attr(755,root,root) %{_bindir}/global
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%dir %{_sysconfdir}/gtags
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/gtags/*
%{_mandir}/man1/global*
%{_mandir}/man1/g*tags*
%{_infodir}/*.info*

%files htags
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htags
%attr(755,root,root) %{_bindir}/gozilla
%{_mandir}/man1/htags*
%{_mandir}/man1/gozilla*

%files gtags-perl-wrapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtags.pl

%files globash
%defattr(644,root,root,755)
%attr(755,root,root) %config /etc/profile.d/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gtags/globash.rc

%files -n xemacs-gtags-mode-pkg
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
