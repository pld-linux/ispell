Summary:	GNU ispell - interactive spelling checker
Summary(de):	GNU ispell - interaktive Rechtschreibprüfung
Summary(fr):	ispell de GNU - vérificateur orthographique interactif
Summary(pl):	GNU ispell - interaktywny program do sprawdzania pisowni
Summary(tr):	Etkilmli yazým denetleyici
Name:		ispell
Version:	3.1.20
Release:	14
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	%{name}.info
Source2:	spell
Patch0:		%{name}-config.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-termio.patch
Patch3:		%{name}-mask.patch
Patch4:		%{name}-mask.axp.patch
Patch5:		%{name}-gets.patch
Patch6:		%{name}-german.patch
Patch7:		%{name}-ncurses.patch
Patch8:		%{name}-munchlist.patch
Patch9:		%{name}-no-EXTRADICT.patch
PreReq:		/sbin/install-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
 
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1

echo "Getting prebuilt ispell.info file :-(."
cp $RPM_SOURCE_DIR/ispell.info .

%build
sed "s/CFLAGS \"-O0\"/CFLAGS \"$RPM_OPT_FLAGS\"/" <local.h >local.h.tmp
mv local.h.tmp local.h

# Make config.sh first
PATH=.:$PATH make config.sh

# Now save build-rooted version (with time-stamp) for install ...
cp config.sh config.sh.BUILD
sed -e "s,/usr/,$RPM_BUILD_ROOT/usr/,g" < config.sh.BUILD > config.sh.INSTALL

# and then make everything
PATH=.:$PATH TERMLIB="-lncurses" make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir},%{_libdir}/emacs/site-lisp}

# Roll in the build-root'ed version (with time-stamp!)
mv config.sh.INSTALL config.sh
PATH=.:$PATH make install

install %{SOURCE1} $RPM_BUILD_ROOT%{_infodir}/ispell.info
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
