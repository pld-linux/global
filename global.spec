#
# Conditional build:
%bcond_without	xemacs		# without xemacs subpackage
%bcond_without	pgsql		# without PostgreSQL support
%bcond_without	home_etc	# don't use home_etc
Summary:	GNU GLOBAL - Common source code tag system
Summary(pl):	GNU GLOBAL - system list odwo�a� powszechnego u�ytku
Name:		global
Version:	4.6.1
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6430ca736a74a734b10201d28fe0a64a
#Source1:	http://www.vim.org/scripts/download_script.php?src_id=2708
Source1:	gtags.vim
# Source1-md5:	d97027efcd44458bd7fbd4b255f620f1
Patch10:	%{name}-acinclude-fix.patch
Patch20:	%{name}-ac-shared-pgsql.patch
Patch30:	%{name}-home_etc.patch
Patch40:	%{name}-globash-altercfg.patch
URL:		http://www.gnu.org/software/global/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_home_etc:BuildRequires:	home-etc-devel}
Requires:	coreutils
Requires:	findutils
Requires:	id-utils
Provides:	gtags-%{version}-%{release}
Provides:	htags-%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# definitions useful for vim-global-tags subpackage
%define vimver		6.2
%define	vimnver		6.3
%define vimepoch	4

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
using the PostgreSQL database.
%endif
You can also find some subpackages, containing support for additional
GLOBAL's features, and for compliance with common code editors
(symbols' completion, jumping).

%description -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.
Mo�esz z jego pomoc� odszuka� podan� funkcj� lub metod� w plikach
�r�d�owych i w �atwy spos�b si� do niej przenie��. Narz�dzie to jest
przydatne do d�ubania w du�ych projektach, zawieraj�cych mn�stwo
podkatalog�w, wiele funkcji g��wnych w stylu main(). Pozwala Ci on
utworzy� jeden kontener ze znacznikami dla du�ego drzewa kodu.
%if %{with pgsql}
Informacje o znacznikach mog� by� przechowywane w postaci plik�w db,
lub te� wsp�dzielone przy pomocy bazy danych PostgreSQL.
%endif
Mo�esz tak�e znale�� kilka podpakiet�w, kt�re zawieraj� wsparcie
dla dodatkowych mechanizm�w GLOBAL, a tak�e pozwalaj� na wsp�prac�
ze niekt�rymi znanymi edytorami kodu (dope�nianie nazw symboli, przeskakiwanie).

%package htags
Summary:	GNU GLOBAL - programs for making hypertext from source code
Summary(pl):	GNU GLOBAL - programy produkuj�ce hypertext z kod�w �r�d�owych
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
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Htags jest narz�dziem generuj�cym hypertext z kod�w. Pakiet ten
zawiera tak�e program wyskakuj�cy o nazwie gozilla, kt�ry zmusza
przegl�darki bazuj�ce na Mozilla, aby wy�wietla�y kod �r�d�owy w
elegancki spos�b. Htags potrafi r�wnie� wsp�pracowa� z repozytorium
CVS u�atwiaj�c nawigacj� w kodach poprzez WWW.

%package gtags-perl-wrapper
Summary:	GNU GLOBAL - gtags wrapper for tools which use Perl
Summary(pl):	GNU GLOBAL - program pomocniczy dla narz�dzi u�ywaj�cych Perl
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
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet zawiera program pomocniczy, kt�ry pozwala u�ywa� tego
systemu niekt�rym narz�dziom i edytorom.

%package globash
Summary:	GNU GLOBAL - Bash customization to walk though the source trees
Summary(pl):	GNU GLOBAL - usprawnienie dla Bash do poruszania si� po drzewach �r�de�
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
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala wywo�ywa� odpowiednio przystosowan� wersj� pow�oki
Bash z udogodnieniami, kt�re czyni� nawigowanie po drzewku �r�de�
rzecz� �atw�. Do tych udogodnie� nale��: stos znacznik�w w stylu Vi,
dope�nianie nazw w styly edytora Emacs, automatyczne wywo�ywanie
edytor�w lub przegl�darek, mechanizm wyr�niania znacznik�w, oraz
mechanizm ciasteczek pomagaj�cy zarz�dza� katalogami.

%if %{with xemacs}
%package -n xemacs-gtags-mode-pkg
Summary:	XEmacs mode for the GNU GLOBAL source tag system
Summary(pl):	Tryb systemu list odwo�a� GNU GLOBAL dla edytora XEmacs
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
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala zintegrowa� system GLOBAL z edytorem XEmacs.
%endif

%define	vimshv		%(echo %{vimver} | tr -d .)
%define	_vimdatadir	%{_datadir}/vim/vim%{vimshv}

%package -n vim-global-tags
Summary:	ViM editor plugin for GNU GLOBAL source tag system
Summary(pl):	wtyczka dla edytora ViM do systemu odwo�a� GNU GLOBAL
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	vim >= %{vimepoch}:%{vimver}
Conflicts:	vim >= %{vimepoch}:%{vimnver}

%description -n vim-global-tags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to use GLOBAL tag system in ViM editor.

%description -n vim-global-tags -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala u�ytkownikom na u�ywanie systemu znacznik�w i
odwo�a� GLOBAL w edytorze ViM.

%package -n less-global-tags
Summary:	less pager's helper for GNU GLOBAL source tag system
Summary(pl):	wsparcie dla polecenia less do systemu odwo�a� GNU GLOBAL
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description -n less-global-tags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

This package allows users to navigate through GLOBAL tags and
references system using less pager.

%description -n less-global-tags -l pl
GNU GLOBAL jest powszechnym systemem generowania list odwo�a� dla
kod�w �r�d�owych napisanych w C, C++, Yacc, Java, PHP i asemblerze.

Ten pakiet pozwala u�ytkownikom na nawigacj� poprzez system znacznik�w
i odwo�a� systemu GLOBAL u�ywaj�c polecenia less.

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
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags \
	$RPM_BUILD_ROOT%{_vimplugindir} \
	$RPM_BUILD_ROOT/etc/profile.d

# vim support
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimplugindir}

# perl wrapper
cp gtags.pl $RPM_BUILD_ROOT%{_bindir}

# globash
cp globash.rc $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# default config
cp gtags.conf $RPM_BUILD_ROOT%{_sysconfdir}/gtags

# emacs support
%if %{with xemacs}
cp gtags.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -no-autoloads -l autoload -f batch-update-directory \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags
xemacs -batch -vanilla -f batch-byte-compile \
	$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gtags/gtags.el
find $RPM_BUILD_ROOT%{_datadir} -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
%endif

# /etc/profile.d/*.sh hook for globash
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/globash.sh
alias globash='%{?with_home_etc:GLOBASH_HOME="\$HOME_ETC" }/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/profile.d/*.csh hook for globash
cat  << EOF > $RPM_BUILD_ROOT/etc/profile.d/globash.csh
alias globash '%{?with_home_etc:setenv GLOBASH_HOME = "\$HOME_ETC" ; }/bin/bash --rcfile %{_sysconfdir}/gtags/globash.rc'
EOF

# /etc/profile.d/*sh hooks for less-global-tags
echo 'LESSGLOBALTAGS="global"'	     > $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'export LESSGLOBALTAGS'	    >> $RPM_BUILD_ROOT/etc/profile.d/less-global.sh
echo 'setenv LESSGLOBALTAGS global'  > $RPM_BUILD_ROOT/etc/profile.d/less-global.csh

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ LICENSE NEWS README THANKS
%attr(755,root,root) %{_bindir}/g*tags
%attr(755,root,root) %{_bindir}/global
%dir %{_sysconfdir}/gtags
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/gtags/gtags.conf
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
%attr(755,root,root) %config /etc/profile.d/globash*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gtags/globash.rc

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
