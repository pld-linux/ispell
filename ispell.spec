Summary:	ispell - interactive spelling checker
Summary(de.UTF-8):	ispell - interaktive Rechtschreibprüfung
Summary(fr.UTF-8):	ispell - vérificateur orthographique interactif
Summary(pl.UTF-8):	ispell - interaktywny program do sprawdzania pisowni
Summary(ru.UTF-8):	ispell - интерактивная программа проверки орфографии
Summary(tr.UTF-8):	Etkilmli yazım denetleyici
Summary(uk.UTF-8):	ispell - інтерактивна програма перевірки орфографії
Name:		ispell
Version:	3.4.06
Release:	1
License:	BSD-like
Group:		Applications/Text
#Source0Download: https://www.cs.hmc.edu/~geoff/ispell.html
Source0:	https://www.cs.hmc.edu/~geoff/tars/%{name}-%{version}.tar.gz
# Source0-md5:	efd9ede43be1b8eb2a2e02023e373ecc
Source1:	spell
Source2:	%{name}-local.h
Patch0:		%{name}-nostrip.patch
URL:		https://www.cs.hmc.edu/~geoff/ispell.html
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

%description -l de.UTF-8
Dies ist die interaktive Rechtschreibprüfung. Sie kann auf Textdateien
angewendet werden und prüft interaktiv auf orthographische Fehler. Das
heißt, das Programm meldet, Möglichkeit eine Alternative vor.

%description -l fr.UTF-8
Le correcteur orthographique interactif. Vous pouvez le lancer sur des
fichiers texte et il les vérifiera de manière interactive. Cela
sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et vous
proposera des solutions de remplacement s'il le peut.

%description -l pl.UTF-8
Program ten to interaktywny pakiet do sprawdzania pisowni. Można
używać go do sprawdzania pisowni plików tekstowych. Działa on w ten
sposób, że informuje o napotkanych, nieznanych słowach i sugeruje ich
zamienniki znajdujące się w słowniku.

%description -l uk.UTF-8
Ispell - це інтерактивна програма перевірки орфографії. Ispell
перевіряє текстовий файл в пошуку орфографічних помилок. Коли вона
знаходить слово, якого немає в словнику, вона пропонує близькі до
нього коректні слова для заміни.

Зверніть увагу, що цей пакет містить лише програму перевірки. Вам буде
потрібно встановити ще пакети з файлами словників для тих мов,
правильність текстів на яких ви хочете перевіряти.

%description -l tr.UTF-8
ispell, metin dosyaları üzerinde sözcük yazımı denetimleri yapan ve
hatalı olduğunu düşündüğü sözcükleri kullanıcıya bildirerek
etkileşimli olarak düzeltilmesine çalışan bir yazılımdır. Düzeltme
önerilerinde bulunma yeteneği de vardır.

%description -l ru.UTF-8
Ispell - это интерактивная программа проверки орфографии. Ispell
проверяет текстовый файл в поиске орфографических ошибок и опечаток.
Когда она находит слово, которого нет в словаре, она предлагает
близкие к нему корректные слова для замены.

Обратите внимание, что этот пакет содержит только программу проверки,
к ней необходимо установить пакеты с файлами словарей для тех языков,
правильность текстов на которых вы хотите проверять.

%package en
Summary:	English dictionary for ispell
Summary(pl.UTF-8):	Angielski słownik dla ispella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description en
English dictionary (i.e. word list) for ispell.

%description en -l pl.UTF-8
Angielski słownik (lista słów) dla ispella.

%prep
%setup -q
%patch0 -p1

cp -f %{SOURCE2} local.h
sed -i -e 's#define[ \t]CC[ \t].*#define CC "%{__cc}"#g' local.h
sed -i -e 's#define[ \t]CFLAGS[ \t].*#define CFLAGS "%{rpmcflags}"#g' local.h
sed -i -e 's#define[ \t]LDFLAGS[ \t].*#define LDFLAGS "%{rpmldflags}"#g' local.h
sed -i -e 's#define[ \t]BINDIR[ \t].*#define BINDIR "%{_bindir}"#g' local.h
sed -i -e 's#define[ \t]LIBDIR[ \t].*#define LIBDIR "%{_libdir}/%{name}"#g' local.h
sed -i -e 's#define[ \t]MAN1DIR[ \t].*#define MAN1DIR "%{_mandir}/man1"#g' local.h
sed -i -e 's#define[ \t]MAN45DIR[ \t].*#define MAN45DIR "%{_mandir}/man5"#g' local.h

%build
# Make config.sh first
PATH=.:$PATH \
%{__make} -j1 config.sh

# and then make everything
PATH=.:$PATH \
	%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_libdir}/%{name}}

PATH=.:$PATH \
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# binaries not installed, sq conflicts with squirrel
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{sq,unsq}.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README WISHES
%attr(755,root,root) %{_bindir}/buildhash
%attr(755,root,root) %{_bindir}/defmt-c
%attr(755,root,root) %{_bindir}/defmt-sh
%attr(755,root,root) %{_bindir}/findaffix
%attr(755,root,root) %{_bindir}/icombine
%attr(755,root,root) %{_bindir}/ijoin
%attr(755,root,root) %{_bindir}/ispell
%attr(755,root,root) %{_bindir}/munchlist
%attr(755,root,root) %{_bindir}/spell
%attr(755,root,root) %{_bindir}/tryaffix
%{_mandir}/man1/buildhash.1*
%{_mandir}/man1/findaffix.1*
%{_mandir}/man1/ispell.1*
%{_mandir}/man1/munchlist.1*
%{_mandir}/man1/tryaffix.1*
%{_mandir}/man5/ispell.5*
%dir %{_libdir}/ispell

%files en
%defattr(644,root,root,755)
%{_libdir}/ispell/american.hash
%{_libdir}/ispell/americanmed.hash
%{_libdir}/ispell/english.aff
%{_libdir}/ispell/english.hash
