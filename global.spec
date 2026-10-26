#
# Conditional build:
%bcond_without	xemacs		# xemacs mode subpackage
%bcond_without	sqlite		# SQLite 3 support
%bcond_without	home_etc	# home_etc support

Summary:	GNU Global - common source code tag system
Summary(pl.UTF-8):	GNU Global - system list odwołań powszechnego użytku
Name:		global
Version:	6.7
Release:	0.1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://ftp.gnu.org/gnu/global/%{name}-%{version}.tar.gz
# Source0-md5:	351b74744385530a1422da44b757728c
#Source1:	http://www.vim.org/scripts/download_script.php?src_id=2708
Patch0:		%{name}-link.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnu.org/software/global/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.9.3
%{?with_home_etc:BuildRequires:	home-etc-devel}
BuildRequires:	libltdl-devel >= 2:2.2.6b
BuildRequires:	libtool >= 2:2.2.6b
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3}
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
Requires:	coreutils
Requires:	findutils
Requires:	idutils
Requires:	python3 >= 1:3
Requires:	python3-pygments
Requires:	setup >= 2.4.6-2
Provides:	gtags-%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# definitions useful for vim-global-tags subpackage
%define		_vimdatadir	%{_datadir}/vim/vimfiles

%define		filterout_c	-Werror=format-security

%description
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code. You can locate the specified function or method
in source files and move there easily. It is useful to hack a large
project containing many subdirectories, many general, main()-type
functions. It allows you to create one tags container for a big code
tree.

You can also find some subpackages, containing support for additional
Global's features, and for compliance with common code editors
(symbols' completion, jumping).

%description -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Umożliwia on odszukanie podanej funkcji lub metody w plikach
źródłowych i przeniesienie się do niej w łatwy sposób. Narzędzie to
jest przydatne do dłubania w dużych projektach, zawierających mnóstwo
podkatalogów, wiele funkcji głównych w stylu main(). Pozwala on
utworzyć jeden kontener ze znacznikami dla dużego drzewa kodu.

Można także znaleźć kilka podpakietów, które zawierają wsparcie dla
dodatkowych mechanizmów Global, a także pozwalają na współpracę z
niektórymi znanymi edytorami kodu (dopełnianie nazw symboli,
przeskakiwanie).

%package htags
Summary:	GNU Global - programs for making hypertext from source code
Summary(pl.UTF-8):	GNU Global - programy produkujące hypertext z kodów źródłowych
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl-base >= 5.005
Provides:	gozilla-%{version}-%{release}
Provides:	htags-%{version}-%{release}

%description htags
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

Htags makes hypertext from source code. The package also contains the
gozilla wrapper, which enforces Mozilla-based web browsers to display
source code in an elegant way. Htags can also work with a CVS
repository, which makes it more easy to navigate though the code over
the Web.

%description htags -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Htags jest narzędziem generującym hypertext z kodów. Pakiet ten
zawiera także program wyskakujący o nazwie gozilla, który zmusza
przeglądarki bazujące na Mozilla, aby wyświetlały kod źródłowy w
elegancki sposób. Htags potrafi również współpracować z repozytorium
CVS ułatwiając nawigację w kodach poprzez WWW.

%package gtags-perl-wrapper
Summary:	GNU Global - gtags wrapper for tools which use Perl
Summary(pl.UTF-8):	GNU Global - program pomocniczy dla narzędzi używających Perl
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl-base >= 5.005
Provides:	gtags-perl-wrapper-%{version}-%{release}

%description gtags-perl-wrapper
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package contains simple Perl wrapper, which allows to use the
system for some tools and editors.

%description gtags-perl-wrapper -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet zawiera program pomocniczy, który pozwala używać tego
systemu niektórym narzędziom i edytorom.

%package globash
Summary:	GNU Global - Bash customization to walk though the source trees
Summary(pl.UTF-8):	GNU Global - usprawnienie dla Bash do poruszania się po drzewach źródeł
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	bash >= 2.05
Provides:	globash-%{version}-%{release}

%description globash
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows you to invoke a customized Bash with features that
makes easy to navigate in the sources trees. These are: Vi-like tag
stack, Emacs-like tag name completion, editor or viewer automatic
invocation, tag mark facility, and a cookie facility for managing
directories.

%description globash -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala wywoływać odpowiednio przystosowaną wersję powłoki
Bash z udogodnieniami, które czynią nawigowanie po drzewku źródeł
rzeczą łatwą. Do tych udogodnień należą: stos znaczników w stylu Vi,
dopełnianie nazw w stylu edytora Emacs, automatyczne wywoływanie
edytorów lub przeglądarek, mechanizm wyróżniania znaczników, oraz
mechanizm ciasteczek pomagający zarządzać katalogami.

%package -n xemacs-gtags-mode-pkg
Summary:	XEmacs mode for the GNU Global source tag system
Summary(pl.UTF-8):	Tryb systemu list odwołań GNU Global dla edytora XEmacs
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description -n xemacs-gtags-mode-pkg
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows to integrate the Global source tag system with the
XEmacs editor.

%description -n xemacs-gtags-mode-pkg -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala zintegrować system Global z edytorem XEmacs.

%package -n vim-global-tags
Summary:	ViM editor plugin for GNU Global source tag system
Summary(pl.UTF-8):	wtyczka dla edytora ViM do systemu odwołań GNU Global
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3

%description -n vim-global-tags
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to use Global tag system in ViM editor.

%description -n vim-global-tags -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala użytkownikom na używanie systemu znaczników i
odwołań Global w edytorze ViM.

%package -n less-global-tags
Summary:	less pager's helper for GNU Global source tag system
Summary(pl.UTF-8):	wsparcie dla polecenia less do systemu odwołań GNU Global
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	less

%description -n less-global-tags
GNU Global is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to navigate through Global tags and
references system using less pager.

%description -n less-global-tags -l pl.UTF-8
GNU Global jest powszechnym systemem generowania list odwołań dla
kodów źródłowych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala użytkownikom na nawigację poprzez system znaczników
i odwołań systemu Global używając polecenia less.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' plugin-factory/maps2conf.pl

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_home_etc:--with-home-etc} \
	--with-python-interpreter=%{__python3} \
	%{?with_pgsql:--with-sqlite3=/usr}

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
alias globash='/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/shrc.d/*.csh hook for globash
cat << EOF > $RPM_BUILD_ROOT/etc/shrc.d/globash.csh
alias globash '/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/profile.d/*sh hooks for less-global-tags
echo 'LESSGLOBALTAGS="global"'	     > $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'export LESSGLOBALTAGS'	    >> $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'setenv LESSGLOBALTAGS global'  > $RPM_BUILD_ROOT/etc/profile.d/less-global.csh

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtags/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# documentation and other stuff
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gtags/{AUTHORS,BUILD_TOOLS,NEWS,COPYING,COPYING.LIB,ChangeLog,DONORS,FAQ,INSTALL,LICENSE,PLUGIN*,README*,SERVERSIDE_HOWTO,THANKS}

# patches for other software
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gtags/{elvis-2.2_0.patch,uctags-scheme.c-diff,vim74-gtags-cscope.patch}

# vim support
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtags/*.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

# perl wrapper
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.pl $RPM_BUILD_ROOT%{_bindir}

# globash
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtags/globash.rc $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# default config
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.conf $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# emacs support
%if %{with xemacs}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags/gtags.el
find $RPM_BUILD_ROOT%{_datadir} -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
%else
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gtags/gtags.el
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS ChangeLog DONORS FAQ LICENSE README THANKS plugin-factory/PLUGIN_HOWTO script/SERVERSIDE_HOWTO
%attr(755,root,root) %{_bindir}/global
%attr(755,root,root) %{_bindir}/gtags
%attr(755,root,root) %{_bindir}/gtags-cscope
%dir %{_sysconfdir}/gtags
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/gtags/gtags.conf
%dir %{_libdir}/gtags
%{_libdir}/gtags/exuberant-ctags.so
%{_libdir}/gtags/pygments-parser.so
%{_libdir}/gtags/universal-ctags.so
%{_libdir}/gtags/user-custom.so
%dir %{_datadir}/gtags
%{_datadir}/gtags/icons
%{_datadir}/gtags/jquery
%dir %{_datadir}/gtags/script
%attr(755,root,root) %{_datadir}/gtags/script/elvis-global
%attr(755,root,root) %{_datadir}/gtags/script/global-client
%attr(755,root,root) %{_datadir}/gtags/script/gtags-client
%attr(755,root,root) %{_datadir}/gtags/script/htags-client
%attr(755,root,root) %{_datadir}/gtags/script/less-global
%attr(755,root,root) %{_datadir}/gtags/script/maps2conf.pl
%attr(755,root,root) %{_datadir}/gtags/script/pygments_parser.py
%{_datadir}/gtags/*.cgi
%{_datadir}/gtags/dot_htaccess
%{_datadir}/gtags/elvis.rc
%{_datadir}/gtags/geco.rc
%{_datadir}/gtags/jscode_*
%{_datadir}/gtags/style.css
%{_mandir}/man1/global.1*
%{_mandir}/man1/gtags.1*
%{_mandir}/man1/gtags-cscope.1*
%{_mandir}/man5/gtags.conf.5*
%{_infodir}/global.info*

%files htags
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htags
%attr(755,root,root) %{_bindir}/htags-server
%attr(755,root,root) %{_bindir}/gozilla
%{_mandir}/man1/htags.1*
%{_mandir}/man1/htags-server.1*
%{_mandir}/man1/gozilla.1*

%files gtags-perl-wrapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtags.pl

%files globash
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/globash
%attr(755,root,root) %config %{_sysconfdir}/shrc.d/globash.csh
%attr(755,root,root) %config %{_sysconfdir}/shrc.d/globash.sh
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtags/globash.rc
%{_mandir}/man1/globash.1*

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
%{_vimdatadir}/plugin/gtags.vim
%{_vimdatadir}/plugin/gtags-cscope.vim
