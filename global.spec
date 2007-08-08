#
# Conditional build:
%bcond_without	xemacs		# without xemacs subpackage
%bcond_without	pgsql		# without PostgreSQL support
%bcond_without	home_etc	# don't use home_etc
#
Summary:	GNU GLOBAL - common source code tag system
Summary(pl.UTF-8):	GNU GLOBAL - system list odwołań powszechnego użytku
Name:		global
Version:	4.7
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz
# Source0-md5:	1662792366fa44adec3577b2d7ee33a4
#Source1:	http://www.vim.org/scripts/download_script.php?src_id=2708
Patch10:	%{name}-acinclude-fix.patch
Patch20:	%{name}-ac-shared-pgsql.patch
Patch30:	%{name}-home_etc.patch
Patch40:	%{name}-globash-altercfg.patch
URL:		http://www.gnu.org/software/global/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_home_etc:BuildRequires:	home-etc-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
Requires:	coreutils
Requires:	findutils
Requires:	idutils
Requires:	setup >= 2.4.6-2
Provides:	gtags-%{version}-%{release}
Provides:	htags-%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# definitions useful for vim-global-tags subpackage
%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code. You can locate the specified function or method
in source files and move there easily. It is useful to hack a large
project containing many subdirectories, many general, main()-type
functions. It allows you to create one tags container for a big code
tree.
%if %{with pgsql}
Tagging information may be keept in the traditional db files, or shared
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code. You can locate the specified function or method
in source files and move there easily. It is useful to hack a large
project containing many subdirectories, many general, main()-type
functions. It allows you to create one tags container for a big code
tree. using the PostgreSQL database.
%endif
You can also find some subpackages, containing support for additional
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code. You can locate the specified function or method
in source files and move there easily. It is useful to hack a large
project containing many subdirectories, many general, main()-type
functions. It allows you to create one tags container for a big code
tree. using the PostgreSQL database. GLOBAL's features, and for
compliance with common code editors (symbols' completion, jumping).

%description -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Umożliwia on odszukanie podanej funkcji lub metody w plikach
źródłowych i przeniesienie się do niej w łatwy sposób. Narzędzie to
jest przydatne do dłubania w dużych projektach, zawierających mnóstwo
podkatalogów, wiele funkcji głównych w stylu main(). Pozwala on
utworzyć jeden kontener ze znacznikami dla dużego drzewa kodu.
%if %{with pgsql}
Informacje o znacznikach mogą być przechowywane w postaci plików db,
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Umożliwia on odszukanie podanej funkcji lub metody w plikach
źródłowych i przeniesienie się do niej w łatwy sposób. Narzędzie to
jest przydatne do dłubania w dużych projektach, zawierających mnóstwo
podkatalogów, wiele funkcji głównych w stylu main(). Pozwala on
utworzyć jeden kontener ze znacznikami dla dużego drzewa kodu. lub też
współdzielone przy pomocy bazy danych PostgreSQL.
%endif
Można także znaleźć kilka podpakietów, które zawierają wsparcie dla
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Umożliwia on odszukanie podanej funkcji lub metody w plikach
źródłowych i przeniesienie się do niej w łatwy sposób. Narzędzie to
jest przydatne do dłubania w dużych projektach, zawierających mnóstwo
podkatalogów, wiele funkcji głównych w stylu main(). Pozwala on
utworzyć jeden kontener ze znacznikami dla dużego drzewa kodu. lub też
współdzielone przy pomocy bazy danych PostgreSQL. dodatkowych
mechanizmów GLOBAL, a także pozwalają na współpracę z niektórymi
znanymi edytorami kodu (dopełnianie nazw symboli, przeskakiwanie).

%package htags
Summary:	GNU GLOBAL - programs for making hypertext from source code
Summary(pl.UTF-8):	GNU GLOBAL - programy produkujące hypertext z kodów źródłowych
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

%description htags -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Htags jest narzędziem generującym hypertext z kodów. Pakiet ten
zawiera także program wyskakujący o nazwie gozilla, który zmusza
przeglądarki bazujące na Mozilla, aby wyświetlały kod źródłowy w
elegancki sposób. Htags potrafi również współpracować z repozytorium
CVS ułatwiając nawigację w kodach poprzez WWW.

%package gtags-perl-wrapper
Summary:	GNU GLOBAL - gtags wrapper for tools which use Perl
Summary(pl.UTF-8):	GNU GLOBAL - program pomocniczy dla narzędzi używających Perl
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

%description gtags-perl-wrapper -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet zawiera program pomocniczy, który pozwala używać tego
systemu niektórym narzędziom i edytorom.

%package globash
Summary:	GNU GLOBAL - Bash customization to walk though the source trees
Summary(pl.UTF-8):	GNU GLOBAL - usprawnienie dla Bash do poruszania się po drzewach źródeł
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

%description globash -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala wywoływać odpowiednio przystosowaną wersję powłoki
Bash z udogodnieniami, które czynią nawigowanie po drzewku źródeł
rzeczą łatwą. Do tych udogodnień należą: stos znaczników w stylu Vi,
dopełnianie nazw w stylu edytora Emacs, automatyczne wywoływanie
edytorów lub przeglądarek, mechanizm wyróżniania znaczników, oraz
mechanizm ciasteczek pomagający zarządzać katalogami.

%package -n xemacs-gtags-mode-pkg
Summary:	XEmacs mode for the GNU GLOBAL source tag system
Summary(pl.UTF-8):	Tryb systemu list odwołań GNU GLOBAL dla edytora XEmacs
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description -n xemacs-gtags-mode-pkg
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows to integrate the GLOBAL source tag system with the
XEmacs editor.

%description -n xemacs-gtags-mode-pkg -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala zintegrować system GLOBAL z edytorem XEmacs.

%package -n vim-global-tags
Summary:	ViM editor plugin for GNU GLOBAL source tag system
Summary(pl.UTF-8):	wtyczka dla edytora ViM do systemu odwołań GNU GLOBAL
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	vim >= 4:6.3.058-3

%description -n vim-global-tags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to use GLOBAL tag system in ViM editor.

%description -n vim-global-tags -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala użytkownikom na używanie systemu znaczników i
odwołań GLOBAL w edytorze ViM.

%package -n less-global-tags
Summary:	less pager's helper for GNU GLOBAL source tag system
Summary(pl.UTF-8):	wsparcie dla polecenia less do systemu odwołań GNU GLOBAL
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description -n less-global-tags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to navigate through GLOBAL tags and
references system using less pager.

%description -n less-global-tags -l pl.UTF-8
GNU GLOBAL jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala użytkownikom na nawigację poprzez system znaczników
i odwołań systemu GLOBAL używając polecenia less.

%prep
%setup -q
%patch10 -p1
%patch20 -p1
%{?with_home_etc:%patch30 -p1}
%patch40 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_pgsql:--with-postgres=shared} \
	%{?with_home_etc:--with-home-etc=shared}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/gtags \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/{xemacs-packages/lisp/gtags,gtags} \
	$RPM_BUILD_ROOT%{_vimdatadir}/plugin \
	$RPM_BUILD_ROOT%{_infodir} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT/etc/profile.d \
	$RPM_BUILD_ROOT/etc/shrc.d \

# /etc/shrc.d/*.sh hook for globash
cat << EOF > $RPM_BUILD_ROOT/etc/shrc.d/globash.sh
alias globash='%{?with_home_etc:GLOBASH_HOME="\$HOME_ETC" }/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/shrc.d/*.csh hook for globash
cat << EOF > $RPM_BUILD_ROOT/etc/shrc.d/globash.csh
alias globash '%{?with_home_etc:setenv GLOBASH_HOME = "\$HOME_ETC" ; }/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/profile.d/*sh hooks for less-global-tags
echo 'LESSGLOBALTAGS="global"'	     > $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'export LESSGLOBALTAGS'	    >> $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'setenv LESSGLOBALTAGS global'  > $RPM_BUILD_ROOT/etc/profile.d/less-global.csh

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# documentation and other stuff
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/{AUTHORS,NEWS,COPYING,ChangeLog,FAQ,INSTALL,LICENSE,README,THANKS} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_datadir}/gtags/{dir.gz,nvi*gtags.diff}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# vim support
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

# perl wrapper
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.pl $RPM_BUILD_ROOT%{_bindir}

# globash
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/globash.rc $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# default config
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.conf $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# emacs support
%if %{with xemacs}
mv -f $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags/gtags.el
find $RPM_BUILD_ROOT%{_datadir} -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/g*tags
%attr(755,root,root) %{_bindir}/global
%dir %{_sysconfdir}/gtags
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/gtags/gtags.conf
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
%attr(755,root,root) %config %{_sysconfdir}/shrc.d/globash*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtags/globash.rc

%if %{with xemacs}
%files -n xemacs-gtags-mode-pkg
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%endif

%files -n less-global-tags
%defattr(644,root,root,755)
%attr(755,root,root) %config /etc/profile.d/less-global*

%files -n vim-global-tags
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/*
