Summary:	GNU ispell - interactive spelling checker
Summary(de):	GNU ispell - interaktive Rechtschreibprüfung
Summary(fr):	ispell de GNU - vérificateur orthographique interactif
Summary(pl):	GNU ispell - interaktywny program do sprawdzania pisowni
Summary(tr):	Etkilmli yazým denetleyici
Name:		ispell
Version:	3.1.20
Release:	12
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	%{name}.info
Source2:	spell
Patch0:		%{name}-3.1.20-config.patch
Patch1:		%{name}-3.1-info.patch
Patch2:		%{name}-3.1.20-termio.patch
Patch3:		%{name}-mask.patch
Patch4:		%{name}-mask.axp.patch
Patch5:		%{name}-gets.patch
PreReq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is the GNU interactive spelling checker. You can run it on text files
and it will interactively spell check. This means it will tell you about
words it doesn't know, and will suggest alternatives when it can.

%description -l de
Dies ist die interaktive GNU-Rechtschreibprüfung. Sie kann auf Textdateien
angewendet werden und prüft interaktiv auf orthographische Fehler. Das
heißt, das Programm meldet, Möglichkeit eine Alternative vor.

%description -l fr
Le correcteur orthographique interactif de GNU. Vous pouvez le lancer sur
des fichiers texte et il les vérifiera de manière interactive. Cela
sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et vous
proposera des solutions de remplacement s'il le peut.

%description -l pl
Program ten to interaktywny pakiet do sprawdzania pisowni. Mo¿na u¿ywaæ go
do sprawdzania pisowni plików tekstowych. Dzia³a on w ten sposób, ¿e
informuje o napotkanych, nieznanych s³owach i sugeruje ich zamienniki
znajduj±ce siê w s³owniku.

%description -l tr
ispell, metin dosyalarý üzerinde sözcük yazýmý denetimleri yapan ve hatalý
olduðunu düþündüðü sözcükleri kullanýcýya bildirerek etkileþimli olarak
düzeltilmesine çalýþan bir yazýlýmdýr. Düzeltme önerilerinde bulunma yeteneði
de vardýr.

%prep
%setup -q -n ispell-3.1

%patch0 -p1
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%ifarch alpha
%patch4 -p1 
%endif
 
%patch5 

echo "Getting prebuilt ispell.info file :-(."
cp $RPM_SOURCE_DIR/ispell.info .

%build
sed "s/CFLAGS \"-O\"/CFLAGS \"$RPM_OPT_FLAGS\"/" <local.h >local.h.tmp
mv local.h.tmp local.h

# Make config.sh first
PATH=.:$PATH make config.sh

# Now save build-rooted version (with time-stamp) for install ...
cp config.sh config.sh.BUILD
sed -e "s,/usr/,$RPM_BUILD_ROOT/usr/,g" < config.sh.BUILD > config.sh.INSTALL

# and then make everything
PATH=.:$PATH make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir},%{_libdir}/emacs/site-lisp}

# Roll in the build-root'ed version (with time-stamp!)
mv config.sh.INSTALL config.sh
PATH=.:$PATH make install

mv $RPM_BUILD_ROOT%{_infodir}/ispell $RPM_BUILD_ROOT/usr/info/ispell.info
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/ispell.info

install ${RPM_SOURCE_DIR}/spell $RPM_BUILD_ROOT%{_bindir}/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[14]/* README
    
%post
/sbin/install-info %{_infodir}/ispell.info.gz /etc/info-dir \
	--entry="* ispell: (ispell)		Interactive spelling checking."

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_infodir}/ispell.info.gz /etc/info-dir \
    	--entry="* ispell: (ispell)           Interactive spelling checking."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_libdir}/ispell
%{_infodir}/ispell.info.gz

%changelog
* Wed Jun 23 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.1.20-12]
- gzipping documentation instead bzipping
- fixed Group(pl)
- cosmetic changes for common l&f

* Sun Dec 20 1998 Artur Frysiak <wiget@usa.net>
- add missing -l pl to polish %%description
- change source name to %%{name}-%%{version}.tar.gz
- change man pages group to man
- change BuildRoot to /var/tmp/%%{name}-%%{version}-%%{release}-root
- split ispell-2.1.30-mask.patch to ispell-mask.axp.patch and ispell-mask.patch
- add ispell-gets.patch
-- remove posible buffer overflow in sq/unsq

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /usr/lib/emacs/site-lisp/ispell.el -- use emacs-20.3 version.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- use posix termios (problem #558)
- add build root.

* Sat Jun 27 1998 Trent Jarvi <jarvi@ezlink.com>
- alphahack patch no longer required. struct winsize now in <ioctl-types.h>.
- change MASKWIDTH apropriately on alpha

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 09 1998 Erik Troan <ewt@redhat.com>
- have two Source1 lines isn't terribly brilliant

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to avoid remaking ispell.info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added a spell program.
- Configured for 8-bit use.
