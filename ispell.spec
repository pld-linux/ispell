Summary:	GNU ispell - interactive spelling checker
Summary(de):	GNU ispell - interaktive RechtschreibprЭfung
Summary(fr):	ispell de GNU - vИrificateur orthographique interactif
Summary(pl):	GNU ispell - interaktywny program do sprawdzania pisowni
Summary(ru):	GNU ispell - интерактивная программа проверки орфографии
Summary(tr):	Etkilmli yazЩm denetleyici
Summary(uk):	GNU ispell - ╕нтерактивна програма перев╕рки орфограф╕╖
Name:		ispell
Version:	3.1.20
Release:	34
License:	BSD
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	╔╒╔в╔Й╔╠║╪╔╥╔Г╔С/╔ф╔╜╔╧╔х
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaГУes/Texto
Group(ru):	Приложения/Текстовые утилиты
Group(sl):	Programi/Besedilo
Group(sv):	TillДmpningar/Text
Group(uk):	Прикладн╕ Програми/Текстов╕ утил╕ти
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	spell
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
Patch10:	%{name}-glibc.patch
Patch11:	%{name}-config2.patch
Patch12:	%{name}-noprotosplease2.patch
Patch13:	%{name}-texlongspace.patch
Patch14:	%{name}-isohtml.patch
BuildRequires:	bison
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNU interactive spelling checker. You can run it on text
files and it will interactively spell check. This means it will tell
you about words it doesn't know, and will suggest alternatives when it
can.

%description -l de
Dies ist die interaktive GNU-RechtschreibprЭfung. Sie kann auf
Textdateien angewendet werden und prЭft interaktiv auf orthographische
Fehler. Das heiъt, das Programm meldet, MЖglichkeit eine Alternative
vor.

%description -l fr
Le correcteur orthographique interactif de GNU. Vous pouvez le lancer
sur des fichiers texte et il les vИrifiera de maniХre interactive.
Cela sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et
vous proposera des solutions de remplacement s'il le peut.

%description -l pl
Program ten to interaktywny pakiet do sprawdzania pisowni. Mo©na
u©ywaФ go do sprawdzania pisowni plikСw tekstowych. DziaЁa on w ten
sposСb, ©e informuje o napotkanych, nieznanych sЁowach i sugeruje ich
zamienniki znajduj╠ce siЙ w sЁowniku.

%description -l uk
Ispell - це ╕нтерактивна програма перев╕рки орфограф╕╖ GNU. Ispell
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
Ispell - это интерактивная программа проверки орфографии GNU. Ispell
проверяет текстовый файл в поиске орфографических ошибок и опечаток.
Когда она находит слово, которого нет в словаре, она предлагает
близкие к нему корректные слова для замены.

Обратите внимание, что этот пакет содержит только программу проверки,
к ней необходимо установить пакеты с файлами словарей для тех языков,
правильность текстов на которых вы хотите проверять.

%prep
%setup -q -n %{name}-3.1

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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
sed "s/CFLAGS \"-O\"/CFLAGS \"%{rpmcflags}\"/" <local.h >local.h.tmp
mv -f local.h.tmp local.h

# Make config.sh first
PATH=.:$PATH %{__make} config.sh

# Now save build-rooted version (with time-stamp) for install ...
cp -f config.sh config.sh.BUILD
sed -e "s,/usr/,$RPM_BUILD_ROOT%{_prefix}/,g" < config.sh.BUILD > config.sh.INSTALL

# and then make everything
PATH=.:$PATH TEMLIB="-lncurses" %{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir},%{_libdir}/emacs/site-lisp}

# Roll in the build-root'ed version (with time-stamp!)
mv -f config.sh.INSTALL config.sh
PATH=.:$PATH %{__make} install

install ispell.info $RPM_BUILD_ROOT%{_infodir}/ispell.info
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%preun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_libdir}/ispell
%{_infodir}/ispell.info*
