Summary:     GNU ispell - interactive spelling checker
Name:        ispell
Version:     3.1.20
Release:     11d
Copyright:   GPL
Group:       Utilities/Text
Group(pl):   U�ytki/Tekst
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:     %{name}.info
Source2:     spell
Patch:       %{name}-3.1.20-config.patch
Patch1:      %{name}-3.1-info.patch
Patch2:      %{name}-3.1.20-termio.patch
Patch3:      %{name}-mask.patch
Patch4:      %{name}-mask.axp.patch
Patch5:      %{name}-gets.patch
PreReq:      /sbin/install-info
BuildRoot:   /var/tmp/%{name}-%{version}-%{release}-root
Summary(de): GNU ispell - interaktive Rechtschreibpr�fung
Summary(fr): ispell de GNU - v�rificateur orthographique interactif
Summary(pl): GNU ispell -interaktywny program do sprawdzania pisowni
Summary(tr): Etkilmli yaz�m denetleyici

%description
This is the GNU interactive spelling checker.  You can run 
it on text files and it will interactively spell check.  This
means it will tell you about words it doesn't know, and will
suggest alternatives when it can.

%description -l pl
Program ten to interaktywny pakiet do sprawdzania pisowni. Mo�na
u�ywa� go do sprawdzania pisowni plik�w tekstowych. Dzia�a on w ten
pos�b, �e informuje o napotkanych, nieznanych s�owach i sugeruje
ich zamienniki znajduj�ce si� w s�owniku.

%description -l de
Dies ist die interaktive GNU-Rechtschreibpr�fung. Sie kann
auf Textdateien angewendet werden und pr�ft interaktiv auf
orthographische Fehler. Das hei�t, das Programm meldet, 
M�glichkeit eine Alternative vor.

%description -l fr
Le correcteur orthographique interactif de GNU. Vous pouvez le
lancer sur des fichiers texte et il les v�rifiera de mani�re interactive.
Cela sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et
vous proposera des solutions de remplacement s'il le peut.

%description -l tr
ispell, metin dosyalar� �zerinde s�zc�k yaz�m� denetimleri yapan ve hatal�
oldu�unu d���nd��� s�zc�kleri kullan�c�ya bildirerek etkile�imli olarak
d�zeltilmesine �al��an bir yaz�l�md�r. D�zeltme �nerilerinde bulunma yetene�i
de vard�r.

%prep
%setup -q -n ispell-3.1

%patch  -p1
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

install -d $RPM_BUILD_ROOT/usr/man
install -d $RPM_BUILD_ROOT/usr/lib/emacs/site-lisp
install -d $RPM_BUILD_ROOT/usr/info

# Roll in the build-root'ed version (with time-stamp!)
mv config.sh.INSTALL config.sh
PATH=.:$PATH make install

mv $RPM_BUILD_ROOT/usr/info/ispell $RPM_BUILD_ROOT/usr/info/ispell.info
gzip -9nf $RPM_BUILD_ROOT/usr/info/ispell.info

install ${RPM_SOURCE_DIR}/spell $RPM_BUILD_ROOT/usr/bin/

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man[14]/*
    
%files
%defattr(644,root,root,755)
%doc README

%attr(755,root,root) /usr/bin/*

%attr(644,root,man) /usr/man/man1/*
%attr(644,root,man) /usr/man/man4/*

/usr/lib/ispell

/usr/info/ispell.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/ispell.info.gz /etc/info-dir \
	--entry="* ispell: (ispell)		Interactive spelling checking."

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/ispell.info.gz /etc/info-dir \
    	--entry="* ispell: (ispell)           Interactive spelling checking."
fi

%changelog
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