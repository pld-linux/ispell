#ifndef LOCAL_H_INCLUDED
#define LOCAL_H_INCLUDED

/*
 * WARNING WARNING WARNING
 *
 * This file is *NOT* a normal C header file!  Although it uses C
 * syntax and is included in C programs, it is also processed by shell
 * scripts that are very stupid about format.
 *
 * Do not try to use #if constructs to configure this file for more
 * than one configuration.  Do not place whitespace after the "#" in
 * "#define".  Do not attempt to disable lines by commenting them out.
 * Do not use backslashes to reduce the length of long lines.
 * None of these things will work the way you expect them to.
 *
 * WARNING WARNING WARNING
 */

#define CC "cc"
#define CFLAGS "-O"
#define LDFLAGS "-s"
#define YACC "bison -y"

#define MINIMENU	/* Display a mini-menu at the bottom of the screen */
#define USG		/* Define on System V or if term.c won't compile */
#define GENERATE_LIBRARY_PROTOS
#define	EGREPCMD "grep -Ei"
#define	HAS_RENAME

/*
 * Important directory paths.  If you change MAN45DIR "/usr/share/man/man5"
 * something else, you probably also want to set MAN45SECT and
 * MAN45EXT (but not if you keep the man pages in section 5 and just
 * store them in a different place).
 */
#define BINDIR "/usr/bin"
#define LIBDIR "/usr/lib/ispell"
#define MAN1DIR "/usr/share/man/man1"
#define MAN45DIR "/usr/share/man/man5"
#define	MAN45SECT "5"
#define	MAN45EXT ".5"


/*
 * Place any locally-required #include statements here
 */

#endif /* LOCAL_H_INCLUDED */
