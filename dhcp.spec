# vendor string (e.g., Fedora, EL)
%define vvendor Fedora

Summary:  DHCP (Dynamic Host Configuration Protocol) server and relay agent
Name:     dhcp
Version:  4.0.0
Release:  24%{?dist}
# NEVER CHANGE THE EPOCH on this package.  The previous maintainer (prior to
# dcantrell maintaining the package) made incorrect use of the epoch and
# that's why it is at 12 now.  It should have never been used, but it was.
# So we are stuck with it.
Epoch:    12
License:  ISC
Group:    System Environment/Daemons
URL:      http://isc.org/products/DHCP/
Source0:  ftp://ftp.isc.org/isc/%{name}/%{name}-%{version}.tar.gz
Source1:  dhcpd.init
Source2:  dhcrelay.init
Source3:  libdhcp4client.pc
Source5:  README.ldap
Source6:  draft-ietf-dhc-ldap-schema-01.txt
Source7:  dhcpd-conf-to-ldap
Source8:  dhclient-script
Source9:  dhcp4client.h
Source10: libdhcp_control.h
Source11: dhcp.schema
Source12: get-ldap-patch.sh

Patch0:   %{name}-4.0.0-errwarn-message.patch
Patch1:   %{name}-4.0.0-ldap-configuration.patch
Patch2:   %{name}-4.0.0-memory.patch
Patch3:   %{name}-4.0.0-options.patch
Patch4:   %{name}-4.0.0-release-by-ifup.patch
Patch5:   %{name}-4.0.0-dhclient-decline-backoff.patch
Patch6:   %{name}-4.0.0-enable-timeout-functions.patch
Patch7:   %{name}-4.0.0-unicast-bootp.patch
Patch8:   %{name}-4.0.0-fast-timeout.patch
Patch9:   %{name}-4.0.0-failover-ports.patch
Patch10:  %{name}-4.0.0-dhclient-usage.patch
Patch11:  %{name}-4.0.0-default-requested-options.patch
Patch12:  %{name}-4.0.0-xen-checksum.patch
Patch13:  %{name}-4.0.0-dhclient-anycast.patch
Patch14:  %{name}-4.0.0-manpages.patch
Patch15:  %{name}-4.0.0-paths.patch
Patch16:  %{name}-4.0.0-NetworkManager-crash.patch
Patch17:  %{name}-4.0.0-FD_CLOEXEC.patch
Patch18:  %{name}-4.0.0-libdhcp4client.patch
Patch19:  %{name}-4.0.0-inherit-leases.patch
Patch20:  %{name}-4.0.0-garbage-chars.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: groff
BuildRequires: libtool
BuildRequires: openldap-devel

Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts

%description
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.  The dhcp package includes the
ISC DHCP service and relay agent.

To use DHCP on your network, install a DHCP service (or relay agent),
and on clients run a DHCP client daemon.  The dhcp package provides
the ISC DHCP service and relay agent.

%package -n dhclient
Summary: Provides the dhclient ISC DHCP client daemon and dhclient-script
Group: System Environment/Base
Requires: initscripts >= 6.75
Obsoletes: dhcpcd <= 1.3.22pl1-7
Provides: dhcpcd = 1.3.22pl1-8

%description -n dhclient
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

To use DHCP on your network, install a DHCP service (or relay agent),
and on clients run a DHCP client daemon.  The dhclient package
provides the ISC DHCP client daemon.

%package devel
Summary: Development headers and libraries for interfacing to the DHCP server
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and API documentation for using the ISC DHCP libraries.  The
libdhcpctl and libomapi static libraries are also included in this package.

%package -n libdhcp4client
Summary: ISC DHCP IPv4 client in a library for invocation from other programs
Group: Development/Libraries

%description -n libdhcp4client
The Internet Software Consortium (ISC) Dynamic Host Configuration Protocol
(DHCP) Internet Protocol version 4 (IPv4) client software in a library
suitable for linkage with and invocation by other programs.

%package -n libdhcp4client-devel
Summary: Header files for development with the ISC DHCP IPv4 client library
Group: Development/Libraries
Requires: dhcp-devel = %{epoch}:%{version}-%{release}
Requires: libdhcp4client = %{epoch}:%{version}-%{release}
Requires: openldap-devel
Requires: pkgconfig

%description -n libdhcp4client-devel
Header files for development with the Internet Software Consortium (ISC)
Dynamic Host Configuration Protocol (DHCP) Internet Protocol version 4 (IPv4)
client library.

%prep
%setup -q

# Replace the standard ISC warning message about requesting help with an
# explanation that this is a patched build of ISC DHCP and bugs should be
# reported through bugzilla.redhat.com
%patch0 -p1

# Add support for dhcpd.conf data in LDAP
# NOTE: Use get-ldap-patch.sh to pull down latest LDAP patch and then modify
# it for this package.
%patch1 -p1

# Fix memory alignment and initialization problems in common/packet.c
# Fix buffer overflow in minires library
# Init struct sock_prog in common/lpf.c to NULL
%patch2 -p1

# Add more dhclient options (-I, -B, -H, -F, -T, -V, and -R)
%patch3 -p1

# Handle releasing interfaces requested by /sbin/ifup
# pid file is assumed to be /var/run/dhclient-$interface.pid
%patch4 -p1

# If we receive a DHCP offer in dhclient and it's DECLINEd in dhclient-script,
# backoff for an amount of time before trying again
%patch5 -p1

# Enable cancel_all_timeouts() and relinquish_timeouts() regardless of
# the DEBUG_MEMORY_LEAKAGE_ON_EXIT macro
%patch6 -p1

# Support unicast BOOTP for IBM pSeries systems (and maybe others)
%patch7 -p1

# Fast timeout for dhclient
%patch8 -p1

# Use the following IANA-registered failover ports:
# dhcp-failover 647/tcp
# dhcp-failover 647/udp
# dhcp-failover 847/tcp
# dhcp-failover 847/udp
%patch9 -p1

# Update the usage screen for dhclient(8) indicating new options
# Use printf() rather than log_info() to display the information
# Also, return EXIT_FAILURE when the usage() screen is displayed (stop parsing)
%patch10 -p1

# Add NIS domain, NIS servers, and NTP servers to the list of default
# requested DHCP options
%patch11 -p1

# Handle Xen partial UDP checksums
%patch12 -p1

# Add anycast support to dhclient (for OLPC)
%patch13 -p1

# Patch man page contents
%patch14 -p1

# Change paths to conform to our standards
%patch15 -p1

# Avoid crash when dhclient is run with NetworkManager
%patch16 -p1

# Make sure all open file descriptors are closed-on-exec for SELinux (#446632)
%patch17 -p1

# Add the libdhcp4client target (library version of dhclient)
%patch18 -p1

# If we have an active lease, do not down the interface (#453982)
%patch19 -p1

# Fix 'garbage in format string' error (#450052)
%patch20 -p1

# Copy in documentation and example scripts for LDAP patch to dhcpd
%{__install} -p -m 0644 %{SOURCE5} .
%{__install} -p -m 0644 %{SOURCE6} doc/
%{__install} -p -m 0755 %{SOURCE7} contrib/

# Copy in the Fedora/RHEL dhclient script
%{__install} -p -m 0755 %{SOURCE8} client/scripts/linux

# Copy in the libdhcp4client headers and Makefile.dist
%{__install} -p -m 0644 %{SOURCE9} includes/

# Copy in libdhcp_control.h to the isc-dhcp includes directory
%{__install} -p -m 0644 %{SOURCE10} includes/isc-dhcp/

# Ensure we don't pick up Perl as a dependency from the scripts and modules
# in the contrib directory (we copy this to /usr/share/doc in the final
# package).
%{__cp} -pR contrib __fedora_contrib
pushd __fedora_contrib
%{__chmod} -x 3.0b1-lease-convert dhclient-tz-exithook.sh dhcpd-conf-to-ldap
%{__chmod} -x sethostname.sh solaris.init
%{__mv} ms2isc/Registry.pm ms2isc/Registry.perlmodule
%{__rm} -f dhcp.spec

# We want UNIX-style line endings
%{__sed} -i -e 's/\r//' ms2isc/readme.txt
%{__sed} -i -e 's/\r//' ms2isc/Registry.perlmodule
%{__sed} -i -e 's/\r//' ms2isc/ms2isc.pl
popd

# Filter false positive perl requires (all of them)
%{__cat} << EOF > %{name}-req
#!/bin/sh
%{__perl_requires} \
| %{__grep} -v 'perl('
EOF
%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
%{__chmod} +x %{__perl_requires}

# Replace @PRODUCTNAME@
%{__sed} -i -e 's|@PRODUCTNAME@|%{vvendor}|g' common/dhcp-options.5
%{__sed} -i -e 's|@PRODUCTNAME@|%{vvendor}|g' configure.ac

# Update paths in all man pages
for page in client/dhclient.conf.5 client/dhclient.leases.5 \
            client/dhclient-script.8 client/dhclient.8 ; do
    %{__sed} -i -e 's|CLIENTBINDIR|/sbin|g' \
                -e 's|RUNDIR|%{_localstatedir}/run|g' \
                -e 's|DBDIR|%{_localstatedir}/db/dhclient|g' \
                -e 's|ETCDIR|%{_sysconfdir}|g' $page
done

for page in server/dhcpd.conf.5 server/dhcpd.leases.5 server/dhcpd.8 ; do
    %{__sed} -i -e 's|CLIENTBINDIR|/sbin|g' \
                -e 's|RUNDIR|%{_localstatedir}/run|g' \
                -e 's|DBDIR|%{_localstatedir}/db/dhcpd|g' \
                -e 's|ETCDIR|%{_sysconfdir}|g' $page
done

aclocal
libtoolize --copy --force
autoconf
autoheader
automake --foreign --add-missing --copy

%build
CFLAGS="%{optflags} -fPIC" \
%configure \
    --disable-dhcpv6 \
    --with-srv-lease-file=%{_localstatedir}/lib/dhcpd/dhcpd.leases \
    --with-cli-lease-file=%{_localstatedir}/lib/dhclient/dhclient.leases \
    --with-srv-pid-file=%{_localstatedir}/run/dhcpd.pid \
    --with-cli-pid-file=%{_localstatedir}/run/dhclient.pid \
    --with-relay-pid-file=%{_localstatedir}/run/dhcrelay.pid
%{__make} %{?_smp_mflags}

%{__sed} 's/@DHCP_VERSION@/%{version}/' < %{SOURCE3} > libdhcp4client.pc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# Remove files we don't want
%{__rm} -rf %{buildroot}%{_libdir}/libdhcp4client.a
%{__rm} -rf %{buildroot}%{_libdir}/libdhcp4client.la
%{__rm} %{buildroot}%{_sysconfdir}/dhclient.conf

# Install correct dhclient-script
%{__mkdir} -p %{buildroot}/sbin
%{__mv} %{buildroot}%{_sbindir}/dhclient %{buildroot}/sbin/dhclient
%{__install} -p -m 0755 client/scripts/linux %{buildroot}/sbin/dhclient-script

# Install pkg-config file
%{__install} -p -m 0644 %{SOURCE10} %{buildroot}%{_includedir}/isc-dhcp/
%{__install} -p -m 0644 -D libdhcp4client.pc %{buildroot}%{_libdir}/pkgconfig/libdhcp4client.pc

# Install headers for libdhcp4client-devel
%{__mkdir} -p %{buildroot}%{_includedir}/dhcp4client/minires
%{__install} -p -m 0644 %{SOURCE9} %{buildroot}%{_includedir}/dhcp4client
for hdr in cdefs.h ctrace.h dhcp.h dhcp6.h dhcpd.h dhctoken.h failover.h \
           heap.h inet.h minires/minires.h minires/res_update.h \
           minires/resolv.h osdep.h site.h statement.h tree.h ; do
    %{__install} -p -m 0644 includes/${hdr} %{buildroot}%{_includedir}/dhcp4client/${hdr}
done

# Install init scripts
%{__mkdir} -p %{buildroot}%{_initrddir}
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/dhcpd
%{__install} -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/dhcrelay

# Start empty lease databases
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/dhcpd/
touch %{buildroot}%{_localstatedir}/lib/dhcpd/dhcpd.leases
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/dhclient/

# Create default sysconfig files for dhcpd and dhcrelay
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig

%{__cat} << EOF > %{buildroot}%{_sysconfdir}/sysconfig/dhcrelay
# Command line options here
INTERFACES=""
DHCPSERVERS=""
EOF

%{__cat} <<EOF > %{buildroot}%{_sysconfdir}/sysconfig/dhcpd
# Command line options here
DHCPDARGS=
EOF

# Copy sample conf files into position (called by doc macro)
%{__cp} -p client/dhclient.conf dhclient.conf.sample
%{__cp} -p server/dhcpd.conf dhcpd.conf.sample

# Install default (empty) dhcpd.conf:
%{__cat} << EOF > %{buildroot}%{_sysconfdir}/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp*/dhcpd.conf.sample
#   see 'man 5 dhcpd.conf'
#
EOF

# Install dhcp.schema for LDAP configuration
%{__mkdir} -p %{buildroot}%{_sysconfdir}/openldap/schema
%{__install} -p -m 0644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/openldap/schema

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add dhcpd
/sbin/chkconfig --add dhcrelay || :

%preun
if [ $1 = 0 ]; then
    /sbin/service dhcpd status >/dev/null 2>&1
    if [ $? = 3 ]; then
        /sbin/service dhcpd stop >/dev/null 2>&1
    fi

    /sbin/service dhcrelay status >/dev/null 2>&1
    if [ $? = 3 ]; then
        /sbin/service dhcrelay stop >/dev/null 2>&1
    fi

    /sbin/chkconfig --del dhcpd
    /sbin/chkconfig --del dhcrelay || :
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service dhcpd condrestart >/dev/null 2>&1
    /sbin/service dhcrelay condrestart >/dev/null 2>&1 || :
fi

%post -n libdhcp4client -p /sbin/ldconfig

%postun -n libdhcp4client -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README README.ldap RELNOTES dhcpd.conf.sample
%doc doc/IANA-arp-parameters doc/api+protocol doc/*.txt __fedora_contrib/*
%dir %{_localstatedir}/lib/dhcpd
%verify(not size md5 mtime) %config(noreplace) %{_localstatedir}/lib/dhcpd/dhcpd.leases
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd
%config(noreplace) %{_sysconfdir}/sysconfig/dhcrelay
%config(noreplace) %{_sysconfdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/openldap/schema/dhcp.schema
%{_initrddir}/dhcpd
%{_initrddir}/dhcrelay
%{_bindir}/omshell
%{_sbindir}/dhcpd
%{_sbindir}/dhcrelay
%attr(0644,root,root) %{_mandir}/man1/omshell.1.gz
%attr(0644,root,root) %{_mandir}/man5/dhcpd.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhcpd.leases.5.gz
%attr(0644,root,root) %{_mandir}/man8/dhcpd.8.gz
%attr(0644,root,root) %{_mandir}/man8/dhcrelay.8.gz
%attr(0644,root,root) %{_mandir}/man5/dhcp-options.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhcp-eval.5.gz

%files -n dhclient
%defattr(-,root,root,-)
%doc dhclient.conf.sample
%dir %{_localstatedir}/lib/dhclient
/sbin/dhclient
/sbin/dhclient-script
%attr(0644,root,root) %{_mandir}/man5/dhclient.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhclient.leases.5.gz
%attr(0644,root,root) %{_mandir}/man8/dhclient.8.gz
%attr(0644,root,root) %{_mandir}/man8/dhclient-script.8.gz
%attr(0644,root,root) %{_mandir}/man5/dhcp-options.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhcp-eval.5.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/dhcpctl
%{_includedir}/isc-dhcp
%{_includedir}/omapip
%{_libdir}/libdhcpctl.a
%{_libdir}/libomapi.a
%{_libdir}/libdst.a
%attr(0644,root,root) %{_mandir}/man3/dhcpctl.3.gz
%attr(0644,root,root) %{_mandir}/man3/omapi.3.gz

%files -n libdhcp4client
%defattr(0755,root,root,0755)
%{_libdir}/libdhcp4client-*.*.so.*

%files -n libdhcp4client-devel
%defattr(0644,root,root,0755)
%{_includedir}/dhcp4client
%{_libdir}/pkgconfig/libdhcp4client.pc
%{_libdir}/libdhcp4client.so

%changelog
* Mon Sep 29 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-24
- 'server' -> 'service' in dhclient-script (#462343)
- Fix dhcpd so it can find configuration data via LDAP (#452985)

* Fri Aug 29 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-23
- Prevent $metric from being set to '' (#460640)
- Remove unnecessary warning messages
- Do not source config file (ifcfg-DEVICE) unless it exists

* Sun Aug 24 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-22
- Add missing '[' to dhclient-script (#459860)
- Correct test statement in add_default_gateway() in dhclient-script (#459860)

* Sat Aug 23 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-21
- Fix syntax error in dhclient-script (#459860)

* Fri Aug 22 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-20
- Rewrite of /sbin/dhclient-script (make the script a little more readable,
  discontinue use of ifconfig in favor of ip, store backup copies of orig
  files in /var rather than in /etc)

* Wed Aug 06 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-19
- Remove 'c' from the domain-search format string in common/tables.c
- Prevent \032 from appearing in resolv.conf search line (#450042)
- Restore SELinux context on saved /etc files (#451560)

* Sun Aug 03 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 12:4.0.0-18
- filter out false positive perl requires

* Fri Aug 01 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-17
- Carry over RES_OPTIONS from ifcfg-ethX files to /etc/resolv.conf (#202923)
- Clean up Requires tags for devel packages
- Allow SEARCH variable in ifcfg files to override search path (#454152)
- Do not down interface if there is an active lease (#453982)
- Clean up how dhclient-script restarts ypbind
- Set close-on-exec on dhclient.leases for SELinux (#446632)

* Sat Jun 21 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-16
- Remove instaces of \032 in domain search option (#450042)
- Make 'service dhcpd configtest' display text indicating the status

* Fri May 16 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-15
- Set close-on-exec on dhclient.leases for SELinux (#446632)

* Tue Apr 01 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-14
- Avoid dhclient crash when run via NetworkManager (#439796)

* Tue Mar 25 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-13
- Update dhclient-script to handle domain-search correctly (#437840)

* Tue Mar 25 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-12
- Remove Requires on openldap-server (#432180)
- Replace CLIENTBINDIR, ETCDIR, DBDIR, and RUNDIR in the man pages with the
  correct paths

* Wed Feb 13 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-11
- Add missing newline to usage() screen in dhclient

* Thu Feb 07 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-10
- Save conf files adding '.predhclient.$interface' to the name (#306381)
- Only restore conf files on EXPIRE/FAIL/RELEASE/STOP if there are no other
  dhclient processes running (#306381)

* Wed Feb 06 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-9
- Match LDAP server option values in stables.c and dhcpd.h (#431003)
- Fix invalid sprintf() statement in server/ldap.c (#431003)

* Wed Feb 06 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-8
- Remove invalid fclose() patch

* Tue Feb 05 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-7
- Don't leak /var/lib/dhclient/dhclient.leases file descriptors (#429890)

* Tue Jan 22 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-6
- read_function() comes from the LDAP patch, so fix it there
- Init new struct universe structs in libdhcp4client so we don't crash on
  multiple DHCP attempts (#428203)

* Thu Jan 17 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-5
- Patch read_function() to handle size_t from read() correctly (#429207)

* Wed Jan 16 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-4
- Fix dhclient.lease file parsing problems (#428785)
- Disable IPv6 support for now as we already ship dhcpv6 (#428987)

* Tue Jan 15 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-3
- Fix segfault in next_iface4() and next_iface6() (#428870)

* Mon Jan 14 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-2
- -fvisibility fails me again

* Mon Jan 14 2008 David Cantrell <dcantrell@redhat.com> - 12:4.0.0-1
- Upgrade to ISC dhcp-4.0.0 (#426634)
     - first ISC release to incorporate DHCPv6 protocol support
     - source tree now uses GNU autoconf/automake
- Removed the libdhcp4client-static package

* Tue Dec 04 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-12
- Requires line fixes

* Tue Dec 04 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-11
- Postinstall script fixes

* Mon Nov 19 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-10
- Remove dhcdbd check from dhcpd init script

* Thu Nov 15 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-9
- Fix chkconfig lines in dhcpd and dhcrelay init scripts (#384431)
- Improve preun scriptlet

* Mon Nov 12 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-8
- Put dhcp.schema in /etc/openldap/schema (#330471)
- Remove manpages patch and keep modified man pages as Source files
- Improve dhclient.8 man page to list options in a style consistent
  with most other man pages on the planet
- Upgrade to latest dhcp LDAP patch, which brings in a new dhcpd-conf-to-ldap
  script, updated schema file, and other bug fixes including SSL support for
  LDAP authentication (#375711)
- Do not run dhcpd and dhcrelay services by default (#362321)

* Fri Oct 26 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-7
- libdhcp4client-devel requires openldap-devel

* Thu Oct 25 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-6
- Rename Makefile.dist to Makefile.libdhcp4client
- Spec file cleanups
- Include stdarg.h in libdhcp_control.h

* Thu Oct 25 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-5
- Remove chkconfig usage for ypbind in dhclient-script (#351211)
- Combine dhcp-static and dhcp-devel packages since there are no shared
  libraries offered
- Remove Requires: openldap-devel on dhcp-devel and libdhcp4client-devel
- Make libdhcp4client-devel require dhcp-devel (for libdhcp_control.h)
- Do not make dhcp-devel require the dhcp package, those are independent

* Wed Oct 24 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-4
- Install libdhcp_control.h to /usr/include/isc-dhcp/libdhcp_control.h
- Update libdhcp4client patch to use new libdhcp_control.h location
- Remove __fedora_contrib/ subdirectory in /usr/share/doc/dhcp-3.1.0,
  install those docs to /usr/share/doc/dhcp-3.1.0

* Wed Oct 24 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-3
- Remove ISC.Cflags variable from libdhcp4client.pc

* Wed Oct 24 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-2
- Fix 'restart' mode in init script (#349341)

* Tue Oct 23 2007 David Cantrell <dcantrell@redhat.com> - 12:3.1.0-1
- Upgrade to ISC dhcp-3.1.0
- Remove unnecessary /usr/include/dhcp4client/isc_dhcp headers
- Make sure restorecon is run on /var/lib/dhcpd/dhcpd.leases (#251688)
- Install dhcp.schema to /etc/openldap/dhcp.schema (#330471)

* Mon Oct 08 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-8
- Init script fixes (#320761)
- Removed linux.dbus-example script since we aren't using dhcdbd now
- Remove dhcdbd leftovers from dhclient-script (#306381)

* Wed Sep 26 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-7
- In dhcp.conf.5, explain that if no next-server statement applies to the
  requesting client, the address 0.0.0.0 is used (#184484).

* Wed Sep 26 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-6
- Init script fixes for dhcpd and dhcrelay (#278601)

* Mon Sep 10 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-5
- Fix typos in ldap.c and correct LDAP macros (#283391)

* Tue Sep 04 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-4
- Do not override manually configured NTP servers in /etc/ntp.conf (#274761)

* Wed Aug 15 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-3
- Remove the -x switch enabling extended new option info.  If given to
  dhclient now, it's ignored.

* Wed Jul 18 2007 Florian La Roche <laroche@redhat.com> - 12:3.0.6-2
- use a new macro name vendor -> vvendor to not overwrite the
  RPMTAG_VENDOR setting

* Tue Jul 10 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.6-1
- Upgrade to ISC dhcp-3.0.6
- Remove the -TERM option from killproc command (#245317)

* Wed Jun 20 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-37
- For init script functions, echo new line after OK or FAIL msg (#244956)

* Fri Jun 15 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-36
- BOOTP_BROADCAST_ALWAYS is not the same as ATSFP, fixed
- Added anycast mac support to dhclient for OLPC

* Tue May 22 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-35
- Disable -fvisibility=hidden for now as it breaks dhcpv4_client() from
  the shared library (#240804)

* Thu Apr 26 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-34
- Init script fixes (#237985, #237983)
- Reference correct scripts in dhclient-script.8 man page (#238036)

* Fri Apr 20 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-33
- Rename -devel-static packages to -static (#225691)

* Tue Apr 17 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-32
- Added missing newline on usage() screen in dhclient

* Thu Apr 12 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-31
- Spec file cleanups (#225691)
- Put libdhcpctl.a and libomapi.a in dhcp-devel-static package
- Put libdhcp4client.a in libdhcp4client-devel-static package

* Wed Apr 11 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-30
- Enable Xen patch again, kernel bits present (#231444)

* Tue Apr 10 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-29
- Spec file cleanups (#225691)

* Mon Apr 09 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-28
- Remove Xen patch (#235649, from RHEL-5, doesn't work correctly for Fedora)

* Sun Apr 01 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-27
- Ensure that Perl and Perl modules are not added as dependencies (#234688)
- Reorganize patches by feature/bug per packaging guidelines (#225691)
- Move the following files from patches to source files:
     linux.dbus-example, linux, Makefile.dist, dhcp4client.h, libdhcp_control.h
- Compile with -fno-strict-aliasing as ISC coding standards generally don't
  agree well with gcc 4.x.x

* Wed Mar 21 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-26
- Fix formatting problems in dhclient man page (#233076).

* Mon Mar 05 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-25
- Man pages need 0644 permissions (#222572)

* Thu Mar 01 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-24
- Include contrib/ subdirectory in /usr/share/doc (#230476)
- Added back Requires for perl since dhcpd-conf-to-ldap needs it (#225691)
- Put copies of dhcp-options and dhcp-eval man pages in the dhcp and
  dhclient packages rather than having the elaborate symlink collection
- Explicitly name man pages in the %%files listings
- Use the %%{_sysconfdir} and %%{_initrddir} macros (#225691)
- Use macros for commands in %%build and %%install
- Split README.ldap, draft-ietf-dhc-ldap-schema-01.txt, and
  dhcpd-conf-to-ldap.pl out of the LDAP patch
- Split linux.dbus-example script out of the extended new option info patch
- Remove unnecessary changes from the Makefile patch

* Wed Feb 28 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-23
- Update Xen partial checksums patch
- Remove perl Requires (#225691)
- Make dhcp-devel depend on dhcp = e:v-r (#225691)
- libdhcp4client-devel Requires pkgconfig (#225691)
- Do not add to RPM_OPT_FLAGS, use COPTS variable instead (#225691)
- Use %%{buildroot} macro instead of RPM_BUILD_ROOT variable (#225691)
- Preserve timestamps on all installed data files (#225691)
- Remove dhcp-options.5.gz and dhcp-eval.5.gz symlinking in post (#225691)
- Use %%defattr(-,root,root,-) (#225691)
- Do not flag init scripts as %%config in %%files section (#225691)

* Tue Feb 27 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-22
- Change license field to say ISC

* Sat Feb 17 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-21
- Obsoletes dhcpcd <= 1.3.22 (#225691)

* Fri Feb 16 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-20
- Review cleanups (#225691)

* Fri Feb 09 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-19
- Require openldap-devel on dhcp-devel and libdhcp4client-devel packages

* Thu Feb 08 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-18
- Fix libdhcp4client visibility _again_ (#198496)

* Thu Feb 08 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-17
- Remove period from summary line (package review)
- Use preferred BuildRoot (package review)

* Sun Feb 04 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-16
- Disable xen-checksums patch for now as it breaks dhclient (#227266)
- Updated fix-warnings patch

* Sun Feb 04 2007 David Woodhouse <dwmw2@redhat.com> - 12:3.0.5-15
- Fix broken file reading due to LDAP patch

* Fri Feb 02 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-14
- Only export the symbols we want in libdhcp4client (#198496)

* Wed Jan 31 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-13
- Add support for dhcpd(8) to read dhcpd.conf from an LDAP server (#224352)
- Remove invalid ja_JP.eucJP man pages from /usr/share/doc

* Wed Jan 31 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-12
- Rebuild

* Tue Jan 30 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-11
- Remove FORTIFY_SOURCE=0 leftovers from testing last week (whoops)

* Tue Jan 30 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-10
- Fix Xen networking problems with partial checksums (#221964)

* Mon Jan 29 2007 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-9
- Remove dhcptables.pl from the source package
- Mark libres.a symbols hidden (#198496)
- Set DT_SONAME on libdhcp4client to libdhcp4client-VERSION.so.0
- Make function definition for dst_hmac_md5_init() match the prototype

* Wed Nov 29 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-8
- Roll md5 patch in to libdhcp4client patch since it's related
- Do not overwrite /etc/ntp/step-tickers (#217663)
- Resolves: rhbz#217663

* Wed Nov 22 2006 Peter Jones <pjones@redhat.com> - 12:3.0.5-7
- Build the MD5 functions we link against.

* Thu Nov 16 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-6
- Set permission of libdhcp4client.so.1 to 0755 (#215910)

* Tue Nov 14 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-5
- Do not link res_query.o in to libdhcp4client (#215501)

* Mon Nov 13 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-4
- Enable relinquish_timeouts() and cancel_all_timeouts() even when
  DEBUG_MEMORY_LEAKAGE_ON_EXIT is not defined
- Add prototypes for b64_pton() and b64_ntop in dst/
- Move variable declarations and labels around in the fix-warnings patch
- Expand the list of objects needed for libdhcp4client (#215328)
- Use libres.a in libdhcp4client since it gives correct minires objects
- Remove the dhcp options table in C, Perl, Python, and text format (these
  were reference files added to /usr/share/doc)

* Mon Nov 13 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-3
- Remove struct universe *universe from envadd_state in the client patch
- Add struct universe *universe to envadd_state in the enoi patch
- Add example dbusified dhclient-script in the enoi patch

* Fri Nov 10 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-2
- Change the way libdhcp4client is compiled (patch main source, create new
  Makefile rather than copy and patch code after main patches)
- Fix up problems generating compiler warnings
- Use 'gcc' for making dependencies
- Pass -fPIC instead of -fpie/-fPIE in compiler flags
- Combine the extended new option info changes in to one patch file (makes
  it easier for outside projects that want to use dhcdbd and NetworkManager)

* Tue Nov 07 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.5-1
- Upgrade to ISC dhcp-3.0.5

* Fri Oct 27 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-24
- Put typedef for dhcp_state_e before it's used in libdhcp_control.h (#212612)
- Remove dhcpctl.3 from minires/Makefile.dist because it's in dhcpctl
- Remove findptrsize.c and just set compiler flag for ppc64 and s390x

* Sat Oct 14 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-23
- Remove NODEBUGINFO junk from the spec file as well as old/unused code
- Rolled all 68 patches in to one patch since more than half of them get
  overridden by later patches anyway.

* Fri Oct 13 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-22
- Send usage() screen in dhclient to stdout rather than the syslog (#210524)

* Mon Sep 11 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-21
- Rebuild (#205505)

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 12:3.0.4-20
- rebuilt with latest binutils to pick up 64K -z commonpagesize on ppc*
  (#203001)

* Thu Aug 17 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-19
- Fix mkdir problem in libdhcp4client.Makefile

* Thu Aug 17 2006 David Cantrell <dcantrell@redhat.com> - 12:3.0.4-18
- Fix dhclient on s390x platform (#202911)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 12:3.0.4-17.1
- rebuild

* Wed Jun 28 2006 Peter Jones <pjones@redhat.com> - 12:3.0.4-17
- export timeout cancellation functions in libdhcp4client

* Wed Jun 28 2006 Florian La Roche <laroche@redhat.com> - 12:3.0.4-16
- add proper coreutils requires for the scripts

* Thu Jun 22 2006 Peter Jones <pjones@redhat.com> - 12:3.0.4-15
- Make timeout dispatch code not recurse while traversing a linked
  list, so it doesn't try to free an entries that have been removed.
  (bz #195723)
- Don't patch in a makefile, do it in the spec.

* Thu Jun 08 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-14
- fix bug 191461: preserve ntp.conf local clock fudge statements
- fix bug 193047: both dhcp and dhclient need to ship common
                  man-pages: dhcp-options(5) dhcp-eval(5)

* Tue May 30 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-12
- Make -R option take effect in per-interface client configs

* Fri May 26 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-10
- fix bug 193047: allow $METRIC to be specified for dhclient routes
- add a '-R <request option list>' dhclient argument

* Fri May 26 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-8.1
- fix a libdhcp4client memory leak (1 strdup) and 
  fill in client->packet.siaddr before bind_lease() for pump
  nextServer option.

* Fri May 19 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-8
- Make libdhcp4client a versioned .so (BZ 192146)

* Wed May 17 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-4
- Enable libdhcp4client build

* Tue May 16 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-2
- Fix bug 191470: prevent dhcpd writing 8 byte dhcp-lease-time 
                  option in packets on 64-bit platforms

* Sun May 14 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-2
- Add the libdhcp4client library package for use by the new libdhcp 
  package, which enables dhclient to be invoked by programs in a 
  single process from the library. The normal dhclient code is
  unmodified by this.

* Mon May 08 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-2
- Add new dhclient command line argument:
  -V <vendor-class-identifier>

* Sat May 06 2006 Jason Vas Dias <jvdias@redhat.com> - 12:3.0.4-1
- Upgrade to upstream version 3.0.4, released Friday 2006-05-05 .
- Add new dhclient command line arguments:
  -H <host-name> : parse as dhclient.conf 'send host-name "<host-name>";'
  -F <fqdn>      : parse as dhclient.conf 'send fqdn.fqdn "<fqdn>";'
  -T <timeout>   : parse as dhclient.conf 'timeout <timeout>;'

* Thu Mar 02 2006 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-26
- fix bug 181908: enable dhclient to operate on IBM zSeries z/OS linux guests:
  o add -I <dhcp-client-identifier> dhclient command line option
  o add -B "always broadcast" dhclient command line option
  o add 'bootp-broadcast-always;' dhclient.conf statement

* Mon Feb 20 2006 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-24
- Apply upstream fix for bug 176615 / ISC RT#15811

* Tue Feb 14 2006 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-22
- fix bug 181482: resolv.conf not updated on RENEW :
  since dhcp-3.0.1rc12-RHScript.patch: "$new_domain_servers" should have
  been "$new_domain_name_servers" :-(

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 11:3.0.3-21.1.1
- bump again for double-long bug on ppc(64)

* Mon Feb 06 2006 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-21.1
- Rebuild for new gcc, glibc and glibc-kernheaders

* Sun Jan 22 2006 Dan Williams <dcbw@redhat.com> - 11:3.0.3-21
- Fix dhclient-script to use /bin/dbus-send now that all dbus related
  binaries are in /bin rather than /usr/bin

* Mon Jan 16 2006 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-20
- fix bug 177845: allow client ip-address as default router 
- fix bug 176615: fix DDNS update when Windows-NT client sends 
                  host-name with trailing nul

* Tue Dec 20 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-18
- fix bug 176270: allow routers with an octet of 255 in their IP address

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec 05 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-16
- fix gcc 4.1 compile warnings (-Werror)

* Fri Nov 19 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-12
- fix bug 173619: dhclient-script should reconfig on RENEW if 
                  subnet-mask, broadcast-address, mtu, routers, etc.
                  have changed
- apply upstream improvements to trailing nul options fix of bug 160655

* Tue Nov 15 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-11
- Rebuild for FC-5
- fix bug 167028 - test IBM's unicast bootp patch (from xma@us.ibm.com)
- fix bug 171312 - silence chkconfig error message if ypbind not installed
- fix dhcpd.init when -cf arg given to dhcpd
- make dhcpd init touch /var/lib/dhcpd/dhcpd.leases, not /var/lib/dhcp/dhcpd.leases

* Tue Oct 18 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-10
- Allow dhclient route metrics to be specified with DHCP options:
  The dhcp-options(5) man-page states:
  'option routers ... Routers should be listed in order of preference' 
  and
  'option static-routes ... are listed in descending order of priority' .
  No preference / priority could be set with previous dhclient-script .
  Now, dhclient-script provides: 
  Default Gateway (option 'routers') metrics:
    Instead of allowing only one default gateway, if more than one router 
    is specified in the routers option, routers following the first router
    will have a 'metric' of their position in the list (1,...N>1).
  Option static-routes metrics:
    If a target appears in the list more than once, routes for duplicate
    targets will have successively greater metrics, starting at 1.

* Mon Oct 17 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-8
- further fix for bug 160655 / ISC bug 15293 - upstream patch:
  do NOT always strip trailing nulls in the dhcpd server
- handle static-routes option properly in dhclient-script :
  trailing 0 octets in the 'target' IP specify the class -
  ie '172.16.0.0 w.x.y.z' specifies '172.16/16 via w.x.y.z'.

* Fri Sep 23 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-7
- fix bug 169164: separate /var/lib/{dhcpd,dhclient} directories
- fix bug 167292: update failover port info in dhcpd.conf.5; give
                  failover ports default values in server/confpars.c
 
* Mon Sep 12 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-6
- fix bug 167273: time-offset should not set timezone by default
                  tzdata's Etc/* files are named with reverse sign
                  for hours west - ie. 'GMT+5' is GMT offset -18000seconds.

* Mon Aug 29 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-4
- fix bug 166926: make dhclient-script handle interface-mtu option
  make dhclient-script support /etc/dhclient{,-$IF}-{up,down}-hooks scripts
  to allow easy customization to support other non-default DHCP options -
  documented in 'man 8 dhclient-script' .
- handle the 'time-offset' DHCP option, requested by default.

* Tue Aug 23 2005 Jason Vas Dias <jvdias@redhat.com> - 11:3.0.3-3
- fix bug 160655: strip trailing '\0' bytes from text options before append
- fix gcc4 compiler warnings ; now compiles with -Werror
- add RPM_OPT_FLAGS to link as suggested in gcc man-page on '-pie' option
- change ISC version string to 'V3.0.3-RedHat' at request of ISC

* Tue Aug  9 2005 Jeremy Katz <katzj@redhat.com> - 11:3.0.3-2
- don't explicitly require 2.2 era kernel, it's fairly overkill at this point

* Fri Jul 29 2005 Jason Vas Dias <jvdias@redhat.com> 11:3.0.3-1
- Upgrade to upstream version 3.0.3 
- Don't apply the 'default boot file server' patch: legacy
  dhcp behaviour broke RFC 2131, which requires that the siaddr
  field only be non-zero if the next-server or tftp-server-name
  options are specified.
- Try removing the 1-5 second wait on dhclient startup altogether.
- fix bug 163367: supply default configuration file for dhcpd
 
* Thu Jul 14 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.3rc1-1
- Upgrade to upstream version 3.0.3rc1
- fix bug 163203: silence ISC blurb on configtest 
- fix default 'boot file server' value (packet->siaddr):
  In dhcp-3.0.2(-), this was defaulted to the server address;
  now it defaults to 0.0.0.0 (a rather silly default!) and
  must be specified with the 'next-server' option (not the tftp-boot-server
  option ?!?) which causes PXE boot clients to fail to load anything after
  the boot file.

* Fri Jul 08 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-14.FC5
- Allow package to compile with glibc-headers-2.3.5-11 (tr.c's use of __u16)

* Fri May 10 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-14
- Fix bug 159929: prevent dhclient flooding network on repeated DHCPDECLINE
- dhclient fast startup:
   remove dhclient's  random 1-5 second delay on startup if only
   configuring one interface
   remove dhclient_script's "sleep 1" on PREINIT
- fix new gcc-4.0.0-11 compiler warnings for binding_state_t

* Tue May 03 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-12
- Rebuild for new glibc
- Fix dhcdbd set for multiple interfaces

* Wed Apr 27 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-11
- as pointed out by Peter Jones, dhclient-script spews
- 'chkconfig: Usage' if run in init state 1 (runlevel returns "unknown".)
- this is now corrected.

* Mon Apr 25 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-10
- dhclient-script dhcdbd extensions. 
- Tested to have no effect unless dhcdbd invokes dhclient.

* Thu Apr 21 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-9
- bugs 153244 & 155143 are now fixed with SELinux policy; 
  autotrans now works for dhcpc_t, so restorecons are not required,
  and dhclient runs OK under dhcpc_t with SELinux enforcing.
- fix bug 155506: 'predhclien' typo (emacs!).

* Mon Apr 18 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-8
- Fix bugs 153244 & 155143: 
      o restore dhclient-script 'restorecon's
      o give dhclient and dhclient-script an exec context of
        'system_u:object_r:sbin_t' that allows them to run
        domainname / hostname and to update configuration files
        in dhclient post script.
- Prevent dhclient emitting verbose ISC 'blurb' on error exit in -q mode

* Mon Apr 04 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-7
- Add '-x' "extended option environment" dhclient argument:
-  When -x option given to dhclient:
-    dhclient enables arbitrary option processing by writing information
-    about user or vendor defined option space options to environment.
-
- fix bug 153244: dhclient should not use restorecon
- fix bug 151023: dhclient no 'headers & libraries' 
- fix bug 149780: add 'DHCLIENT_IGNORE_GATEWAY' variable
- remove all usage of /sbin/route from dhclient-script

* Thu Mar 24 2005 Florian La Roche <laroche@redhat.com>
- add "exit 0" to post script

* Mon Mar 07 2005 Jason Vas Dias <jvdias@redhat.com> 10.3.0.2-3
- rebuild for gcc4/glibc-2.3.4-14; fix bad memset

* Thu Feb 24 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-2
- Fix bug 143640: do not allow more than one dhclient to configure an interface

* Mon Feb 21 2005 Jason Vas Dias <jvdias@redhat.com> 10:3.0.2-1
- Upgrade to ISC 3.0.2 Final Release (documentation change only).

* Tue Feb 14 2005 Jason Vas Dias <jvdias@redhat.com> 8:3.0.2rc3-8
- Add better execshield security link options
- fix dhcpd.init when no /etc/dhcpd.conf exists and -cf in DHCPDARGS

* Mon Feb 14 2005 Jason Vas Dias <jvdias@redhat.com> 8:3.0.2rc3-4
- make dhclient-script TIMEOUT mode do exactly the same configuration
- as BOUND / RENEW / REBIND / REBOOT if router ping succeeds

* Mon Feb 14 2005 Jason Vas Dias <jvdias@redhat.com> 3.0.2rc3-4
- fix bug 147926: dhclient-script should do restorecon for modified conf files
- optimize execshield protection

* Thu Feb 10 2005 Jason Vas Dias <jvdias@redhat.com> 8.3.0.4rc3-3
- fix bug 147375: dhcpd heap corruption on 32-bit 'subnet' masks
- fix bug 147502: dhclient should honor GATEWAYDEV and GATEWAY settings
- fix bug 146600: dhclient's timeout mode ping should use -I
- fix bug 146524: dhcpd.init should discard dhcpd's initial output message
- fix bug 147739: dhcpd.init configtest should honor -cf in DHCPDARGS

* Mon Jan 24 2005 Jason Vas Dias <jvdias@redhat.com> 8:3.0.2rc3-2
- fix bug 145997: allow hex 32-bit integers in user specified options

* Thu Jan 06 2005 Jason Vas Dias <jvdias@redhat.com> 8:3.0.2rc3-1
- still need an epoch to get past nvre test

* Thu Jan 06 2005 Jason Vas Dias <jvdias@redhat.com> 3.0.2rc3-1
- fix bug 144417: much improved dhclient-script

* Thu Jan 06 2005 Jason Vas Dias <jvdias@redhat.com> 3.0.2rc3-1
- Upgrade to latest release from ISC, which includes most of our
- recent patches anyway.

* Thu Jan 06 2005 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-17
- fix bug 144250: gcc-3.4.3-11 is broken :
- log_error ("Lease with bogus binding state: %%d size: %%d",
-   comp -> binding_state,
-   sizeof(comp->binding_state));
- prints:    'Lease with bogus binding state: 257 1'    !
- compiling with gcc33 (compat-gcc-8-3.3.4.2 fixes for now).

* Mon Jan 03 2005 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-16
- fix bug 143704: dhclient -r does not work if lease held by
- dhclient run from ifup . dhclient will now look for the pid
- files created by ifup.

* Wed Nov 17 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-14
- NTP: fix bug 139715: merge in new ntp servers only rather than replace
- all the ntp configuration files; restart ntpd if configuration changed.

* Tue Nov 16 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-12
- fix bug 138181 & bug 139468: do not attempt to listen/send on
-     unconfigured  loopback, point-to-point or non-broadcast
-     interfaces (don't generate annoying log messages)
- fix bug 138869: dhclient-script: check if '$new_routers' is
-     empty before doing 'set $new_routers;...;ping ... $1'

* Wed Oct 06 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-11
- dhcp-3.0.2b1 came out today. A diff of the 'ack_lease' function
- Dave Hankins and I patched exposed a missing '!' on an if clause
- that got dropped with the 'new-host' patch. Replacing the '!'.
- Also found one missing host_dereference.

* Wed Oct 06 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-10
- clean-up last patch: new-host.patch adds host_reference(host)
- without host_dereference(host) before returns in ack_lease
- (dhcp-3.0.1-host_dereference.patch)
 
* Mon Sep 27 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-9
- Fix bug 133522:
- PXE Boot clients with static leases not given 'file' option
- 104 by server - PXE booting was disabled for 'fixed-address'
- clients.

* Fri Sep 10 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-8
- Fix bug 131212:
- If "deny booting" is defined for some group of hosts,
- then after one of those hosts is denied booting, all
- hosts are denied booting, because of a pointer not being
- cleared in the lease record. 
- An upstream patch was obtained which will be in dhcp-3.0.2.

* Mon Aug 16 2004 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-7
- Forward DNS update by client was disabled by a bug that I
- found in code where 'client->sent_options' was being
- freed too early.
- Re-enabled it after contacting upstream maintainer
- who confirmed that this was a bug (bug #130069) -
- submitted patch dhcp-3.0.1.preserve-sent-options.patch.
- Upstream maintainer informs me this patch will be in dhcp-3.0.2 .

* Tue Aug 3  2004 Jason Vas Dias <jvdias@redhat.com> 6:3.0.1-6
- Allow 2.0 kernels to obtain default gateway via dhcp

* Mon Aug 2  2004 Jason Vas Dias <jvdias@redhat.com> 5:3.0.1-5
- Invoke 'change_resolv_conf' function to change resolv.conf

* Fri Jul 16 2004 Jason Vas Dias <jvdias@redhat.com> 3:3.0.1
- Upgraded to new ISC 3.0.1 version

* Thu Jun 24 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc14-5
- Allow dhclient-script to continue without a config file.
- It will use default values.

* Wed Jun 23 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc14-4
- fix inherit-leases patch

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc14-2
- Turn on inherit-leases patch

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc14-1
- User kernelversion instead of uname-r
- Update to latest package from ISC
- Remove inherit-leases patch for now.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc13-1
- Update to latest package from ISC

* Thu Jun 10 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc12-9
- add route back in after route up call

* Wed Jun 9 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc12-8
- add alex's dhcp-3.0.1rc12-inherit-leases.patch patch

* Tue Jun  8 2004 Bill Nottingham <notting@redhat.com> 1:3.0.1rc12-7
- set device on default gateway route

* Mon May 17 2004 Thomas Woerner <twoerner@redhat.com> 1:3.0.1rc12-6
- compiling dhcpd PIE

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc12-5
- Add static routes patch to dhclient-script

* Wed Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc12-4
- Fix init to check config during restart

* Wed Mar 24 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0.1rc12-3
- Fix init script to create leases file if missing

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 21 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.20
- Fix initialization of memory to prevent compiler error

* Mon Jan 5 2004 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.19
- Close leaseFile before exec, to fix selinux error message

* Mon Dec 29 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.18
- Add BuildRequires groff
- Replace resolv.conf if renew and data changes

* Sun Nov 30 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.17
- Add obsoletes dhcpcd

* Wed Oct 8 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.16
- Fix location of ntp driftfile

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.15
- Bump Release

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.14
- Add div0 patch

* Wed Aug 20 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.13
- Add SEARCH to client script

* Wed Aug 20 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.12
- Bump Release

* Wed Aug 20 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.11
- Add configtest

* Fri Aug 1 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.10
- increment for base

* Fri Aug 1 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.9
- Don't update resolv.conf on renewals

* Tue Jul  29 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.8
- increment for base

* Tue Jul  29 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.7
- Fix name of driftfile

* Tue Jul  29 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.6
- increment for base

* Tue Jul  29 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.5
- Change dhcrelay script to check DHCPSERVERS

* Mon Jul  7 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.4
- increment for base

* Mon Jul  7 2003 Dan Walsh <dwalsh@redhat.com> 1:3.0pl2-6.3
- Fix dhclient-script to support PEERNTP and PEERNIS flags.
- patch submitted by aoliva@redhat.com

* Sun Jun  8 2003 Tim Powers <timp@redhat.com> 1:3.0pl2-6.1
- add epoch to dhcp-devel versioned requires on dhcp
- build for RHEL

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 27 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl2-5
- Fix memory leak in parser.

* Mon May 19 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl2-4
- Change Rev for RHEL

* Mon May 19 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl2-3
- Change example to not give out 255 address.

* Tue Apr 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl2-2
- Change Rev for RHEL

* Mon Apr 28 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl2-1
- upgrade to 3.0pl2

* Wed Mar 26 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-26
- add usage for dhcprelay -c
- add man page for dhcprelay -c

* Fri Mar 7 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-25
- Fix man dhcpd.conf man page

* Tue Mar 4 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-24
- Fix man dhcpctl.3 page

* Mon Feb 3 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-23
- fix script to handle ntp.conf correctly

* Thu Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-22
- Increment release to add to 8.1

* Wed Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-21
- Implement max hops patch

* Wed Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-20
- It has now been decided to just have options within dhclient kit

* Sun Jan 26 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add defattr() to have files not owned by root

* Fri Jan 24 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-17
- require kernel version

* Fri Jan 24 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-16
- move dhcp-options to separate package

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 9 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-15
- eliminate dhcp-options from dhclient in order to get errata out

* Wed Jan 8 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-14
- VU#284857 - ISC DHCPD minires library contains multiple buffer overflows

* Mon Jan 6 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-13
- Fix when ntp is not installed.

* Mon Jan 6 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-12
- Fix #73079 (dhcpctl man page)

* Thu Nov 14 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-11
- Use generic PTRSIZE_64BIT detection instead of ifarch.

* Thu Nov 14 2002 Preston Brown <pbrown@redhat.com> 3.0pl1-10
- fix parsing of command line args in dhclient.  It was missing a few.

* Mon Oct 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- work on 64bit archs

* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-9
- Fix #72795

* Mon Aug 26 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-8
- More #68650 (modify requested options)
- Fix #71453 (dhcpctl man page) and #71474 (include libdst.a) and
  #72622 (hostname setting)

* Thu Aug 15 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-7
- More #68650 (modify existing patch to also set NIS domain)

* Tue Aug 13 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-6
- Patch102 (dhcp-3.0pl1-dhcpctlman-69731.patch) to fix #69731

* Tue Aug 13 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-5
- Patch101 (dhcp-3.0pl1-dhhostname-68650.patch) to fix #68650

* Fri Jul 12 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-4
- Fix unaligned accesses when decoding a UDP packet

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-3
- No apparent reason for the dhclient -> dhcp dep mentioned in #68001,
  so removed it

* Wed Jun 27 2002 David Sainty <saint@redhat.com> 3.0pl1-2
- Move dhclient.conf.sample from dhcp to dhclient

* Mon Jun 25 2002 David Sainty <saint@redhat.com> 3.0pl1-1
- Change to dhclient, dhcp, dhcp-devel packaging
- Move to 3.0pl1, do not strip binaries
- Drop in sysconfig-enabled dhclient-script

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jan 26 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- prereq chkconfig

* Tue Jan 22 2002 Elliot Lee <sopwith@redhat.com> 3.0-5
- Split headers/libs into a devel subpackage (#58656)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 28 2001 Elliot Lee <sopwith@redhat.com> 3.0-3
- Fix the #52856 nit.
- Include dhcrelay scripts from #49186

* Thu Dec 20 2001 Elliot Lee <sopwith@redhat.com> 3.0-2
- Update to 3.0, include devel files installed by it (as part of the main
  package).

* Sun Aug 26 2001 Elliot Lee <sopwith@redhat.com> 2.0pl5-8
- Fix #26446

* Mon Aug 20 2001 Elliot Lee <sopwith@redhat.com>
- Fix #5405 for real - it is dhcpd.leases not dhcp.leases.

* Mon Jul 16 2001 Elliot Lee <sopwith@redhat.com>
- /etc/sysconfig/dhcpd
- Include dhcp.leases file (#5405)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Feb 14 2001 Tim Waugh <twaugh@redhat.com>
- Fix initscript typo (bug #27624).

* Wed Feb  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Improve spec file i18n

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script (#26084)

* Sun Sep 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.0pl5
- redo buildroot patch

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Preston Brown <pbrown@redhat.com>
- check for existence of /var/lib/dhcpd.leases in initscript before starting

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- /etc/rc.d/init.d -> /etc/init.d
- fix /var/state/dhcp -> /var/lib/dhcp

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- condrestart for initscript, graceful upgrades.

* Thu Feb 03 2000 Erik Troan <ewt@redhat.com>
- gzipped man pages
- marked /etc/rc.d/init.d/dhcp as a config file

* Mon Jan 24 2000 Jakub Jelinek <jakub@redhat.com>
- fix booting of JavaStations
  (reported by Pete Zaitcev <zaitcev@metabyte.com>).
- fix SIGBUS crashes on SPARC (apparently gcc is too clever).

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %%preun, not %%postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0b1pl28.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- copy the source file in prep, not move

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added a sample dhcpd.conf file
- we don't need to dump rfc's in /usr/doc

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- modify dhcpd.init to exit if /etc/dhcpd.conf is not present

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- Upgraded to 2.0b1pl6 (patch1 no longer needed).

* Thu Jun 11 1998 Erik Troan <ewt@redhat.com>
- applied patch from Chris Evans which makes the server a bit more paranoid
  about dhcp requests coming in from the wire

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- updated to dhcp 2.0b1pl1
- got proper man pages in the package

* Tue Mar 31 1998 Erik Troan <ewt@redhat.com>
- updated to build in a buildroot properly
- don't package up the client, as it doens't work very well <sigh>

* Tue Mar 17 1998 Bryan C. Andregg <bandregg@redhat.com>
- Build rooted and corrected file listing.

* Mon Mar 16 1998 Mike Wangsmo <wanger@redhat.com>
- removed the actual inet.d links (chkconfig takes care of this for us)
  and made the %%postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.
