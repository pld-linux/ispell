Summary:	ispell - interactive spelling checker
Summary(de):	ispell - interaktive RechtschreibprЭfung
Summary(fr):	ispell - vИrificateur orthographique interactif
Summary(pl):	ispell - interaktywny program do sprawdzania pisowni
Summary(ru):	ispell - интерактивная программа проверки орфографии
Summary(tr):	Etkilmli yazЩm denetleyici
Summary(uk):	ispell - ╕нтерактивна програма перев╕рки орфограф╕╖
Name:		ispell
Version:	3.3.02
Release:	1
License:	BSD-like
Group:		Applications/Text
Source0:	http://fmg-www.cs.ucla.edu/geoff/tars/%{name}-%{version}.tar.gz
# Source0-md5:	12087d7555fc2b746425cd167af480fe
Source1:	spell
Source2:	%{name}-local.h
URL:		http://ficus-www.cs.ucla.edu/geoff/ispell.html
BuildRequires:	bison
BuildRequires:	ncurses-devel
Conflicts:	vim-ispell <= 4:6.1.212-4
Conflicts:	ispell-pl < 20021127-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the interactive spelling checker. You can run it on text files
and it will interactively spell check. This means it will tell you
about words it doesn't know, and will suggest alternatives when it
can.

%description -l de
Dies ist die interaktive RechtschreibprЭfung. Sie kann auf Textdateien
angewendet werden und prЭft interaktiv auf orthographische Fehler. Das
heiъt, das Programm meldet, MЖglichkeit eine Alternative vor.

%description -l fr
Le correcteur orthographique interactif. Vous pouvez le lancer sur des
fichiers texte et il les vИrifiera de maniХre interactive. Cela
sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et vous
proposera des solutions de remplacement s'il le peut.

%description -l pl
Program ten to interaktywny pakiet do sprawdzania pisowni. Mo©na
u©ywaФ go do sprawdzania pisowni plikСw tekstowych. DziaЁa on w ten
sposСb, ©e informuje o napotkanych, nieznanych sЁowach i sugeruje ich
zamienniki znajduj╠ce siЙ w sЁowniku.

%description -l uk
Ispell - це ╕нтерактивна програма перев╕рки орфограф╕╖. Ispell
перев╕ря╓ текстовий файл в пошуку орфограф╕чних помилок. Коли вона
знаходить слово, якого нема╓ в словнику, вона пропону╓ близьк╕ до
нього коректн╕ слова для зам╕ни.

Зверн╕ть увагу, що цей пакет м╕стить лише програму перев╕рки. Вам буде
потр╕бно встановити ще пакети з файлами словник╕в для тих мов,
правильн╕сть текст╕в на яких ви хочете перев╕ряти.

%description -l tr
ispell, metin dosyalarЩ Эzerinde sЖzcЭk yazЩmЩ denetimleri yapan ve
hatalЩ olduПunu dЭЧЭndЭПЭ sЖzcЭkleri kullanЩcЩya bildirerek
etkileЧimli olarak dЭzeltilmesine ГalЩЧan bir yazЩlЩmdЩr. DЭzeltme
Жnerilerinde bulunma yeteneПi de vardЩr.

%description -l ru
Ispell - это интерактивная программа проверки орфографии. Ispell
проверяет текстовый файл в поиске орфографических ошибок и опечаток.
Когда она находит слово, которого нет в словаре, она предлагает
близкие к нему корректные слова для замены.

Обратите внимание, что этот пакет содержит только программу проверки,
к ней необходимо установить пакеты с файлами словарей для тех языков,
правильность текстов на которых вы хотите проверять.

%package en
Summary:	English dictionary for ispell
Summary(pl):	Angielski sЁownik dla ispella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description en
English dictionary (i.e. word list) for ispell.

%description en -l pl
Angielski sЁownik (lista sЁСw) dla ispella.

%prep
%setup -q

install %{SOURCE2} local.h
sed -i -e 's#define[ \t]CC[ \t].*#define CC "%{__cc}"#g' local.h
sed -i -e 's#define[ \t]CFLAGS[ \t].*#define CFLAGS "%{rpmcflags}"#g' local.h
sed -i -e 's#define[ \t]LDFLAGS[ \t].*#define LDFLAGS "%{rpmldflags}"#g' local.h
sed -i -e 's#define[ \t]BINDIR[ \t].*#define BINDIR "%{_bindir}"#g' local.h
sed -i -e 's#define[ \t]LIBDIR[ \t].*#define LIBDIR "%{_libdir}/%{name}"#g' local.h
sed -i -e 's#define[ \t]MAN1DIR[ \t].*#define MAN1DIR "%{_mandir}/man1"#g' local.h
sed -i -e 's#define[ \t]MAN45DIR[ \t].*#define MAN45DIR "%{_mandir}/man5"#g' local.h
sed -i -e 's#define[ \t]TEXINFODIR[ \t].*#define TEXINFODIR "%{_infodir}"#g' local.h
sed -i -e 's#define[ \t]ELISPDIR[ \t].*#define ELISPDIR "%{_libdir}/emacs/site-lisp"#g' local.h

%build
# Make config.sh first
PATH=.:$PATH %{__make} config.sh

# Now save build-rooted version (with time-stamp) for install ...
sed -e "s,/usr/,$RPM_BUILD_ROOT%{_prefix}/,g"  < config.sh > config.sh.INSTALL

# and then make everything
PATH=.:$PATH TEMLIB="-lncurses" \
	%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir},%{_libdir}/{%{name},emacs/site-lisp}}

# Roll in the build-root'ed version (with time-stamp!)
mv -f config.sh.INSTALL config.sh
PATH=.:$PATH %{__make} install

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%preun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_libdir}/ispell

%files en
%defattr(644,root,root,755)
%{_libdir}/ispell/*
