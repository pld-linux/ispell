Summary:	ispell - interactive spelling checker
Summary(de):	ispell - interaktive Rechtschreibpr�fung
Summary(fr):	ispell - v�rificateur orthographique interactif
Summary(pl):	ispell - interaktywny program do sprawdzania pisowni
Summary(ru):	ispell - ������������� ��������� �������� ����������
Summary(tr):	Etkilmli yaz�m denetleyici
Summary(uk):	ispell - ������������ �������� ����צ��� �������Ʀ�
Name:		ispell
Version:	3.2.06
Release:	3
License:	BSD-like
Group:		Applications/Text
Source0:	http://fmg-www.cs.ucla.edu/geoff/tars/%{name}-%{version}.tar.gz
# Source0-md5:	d434e1aef1a815294d5012c60c4c414a
Source1:	spell
Patch0:		%{name}-config.patch
Patch1:		%{name}-termio.patch
Patch2:		%{name}-mask.axp.patch
Patch3:		%{name}-gets.patch
Patch4:		%{name}-german.patch
Patch5:		%{name}-ncurses.patch
Patch6:		%{name}-munchlist.patch
Patch7:		%{name}-config2.patch
Patch8:		%{name}-yuck.patch
Patch9:		%{name}-pmake.patch
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
Dies ist die interaktive Rechtschreibpr�fung. Sie kann auf Textdateien
angewendet werden und pr�ft interaktiv auf orthographische Fehler. Das
hei�t, das Programm meldet, M�glichkeit eine Alternative vor.

%description -l fr
Le correcteur orthographique interactif. Vous pouvez le lancer sur des
fichiers texte et il les v�rifiera de mani�re interactive. Cela
sisgnifie qu'il vous indiquera les mots qu'il ne reconnait pas et vous
proposera des solutions de remplacement s'il le peut.

%description -l pl
Program ten to interaktywny pakiet do sprawdzania pisowni. Mo�na
u�ywa� go do sprawdzania pisowni plik�w tekstowych. Dzia�a on w ten
spos�b, �e informuje o napotkanych, nieznanych s�owach i sugeruje ich
zamienniki znajduj�ce si� w s�owniku.

%description -l uk
Ispell - �� ������������ �������� ����צ��� �������Ʀ�. Ispell
����צ�Ѥ ��������� ���� � ������ �������Ʀ���� �������. ���� ����
��������� �����, ����� ����� � ��������, ���� ������դ �����˦ ��
����� ������Φ ����� ��� ��ͦ��.

����Φ�� �����, �� ��� ����� ͦ����� ���� �������� ����צ���. ��� ����
���Ҧ��� ���������� �� ������ � ������� ������˦� ��� ��� ���,
�������Φ��� ����Ԧ� �� ���� �� ������ ����צ����.

%description -l tr
ispell, metin dosyalar� �zerinde s�zc�k yaz�m� denetimleri yapan ve
hatal� oldu�unu d���nd��� s�zc�kleri kullan�c�ya bildirerek
etkile�imli olarak d�zeltilmesine �al��an bir yaz�l�md�r. D�zeltme
�nerilerinde bulunma yetene�i de vard�r.

%description -l ru
Ispell - ��� ������������� ��������� �������� ����������. Ispell
��������� ��������� ���� � ������ ��������������� ������ � ��������.
����� ��� ������� �����, �������� ��� � �������, ��� ����������
������� � ���� ���������� ����� ��� ������.

�������� ��������, ��� ���� ����� �������� ������ ��������� ��������,
� ��� ���������� ���������� ������ � ������� �������� ��� ��� ������,
������������ ������� �� ������� �� ������ ���������.

%package en
Summary:	English dictionary for ispell
Summary(pl):	Angielski s�ownik dla ispella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description en
English dictionary (i.e. word list) for ispell.

%description en -l pl
Angielski s�ownik (lista s��w) dla ispella.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%ifarch alpha
%patch2 -p1
%endif
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1

%build
sed "s/CFLAGS \"-O\"/CFLAGS \"%{rpmcflags}\"/" <local.h >local.h.tmp
sed -e "s,\"/usr/lib/ispell\",\"%{_libdir}/ispell\",g" \
	<local.h.tmp >local.h

# Make config.sh first
PATH=.:$PATH %{__make} config.sh

# Now save build-rooted version (with time-stamp) for install ...
cp -f config.sh config.sh.BUILD
sed -e "s,/usr/lib/ispell,%{_libdir}/ispell,g" < config.sh.BUILD | \
	sed -e "s,/usr/,$RPM_BUILD_ROOT%{_prefix}/,g" > config.sh.INSTALL

# and then make everything
PATH=.:$PATH TEMLIB="-lncurses" %{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_infodir},%{_libdir}/emacs/site-lisp}

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
%{_mandir}/man4/*
%dir %{_libdir}/ispell

%files en
%defattr(644,root,root,755)
%{_libdir}/ispell/*
