Summary: A DHCP (Dynamic Host Configuration Protocol) server and relay agent.
Name:    dhcp
Version: 3.0.2
Release: 6
Epoch:   10
License: distributable
Group: System Environment/Daemons
Source0: ftp://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.gz
Source1: dhcpd.conf.sample
Source2: dhcpd.init
Source3: dhcrelay.init
Patch: dhcp-3.0-alignment.patch
Patch100: dhcp-3.0-jbuild.patch
Patch102: dhcp-3.0.1rc13-dhcpctlman.patch
Patch103: dhcp-3.0pl1-miscfixes.patch
Patch106: dhcp-3.0pl1-minires.patch
Patch109: dhcpd-manpage.patch
Patch113: dhcp-3.0pl2-selinux.patch
Patch114: dhcp-3.0pl2-initialize.patch
Patch115: dhcp-3.0.1rc12-RHscript.patch
Patch116: dhcp-3.0.1rc12-staticroutes.patch
Patch117: dhcp-3.0.1rc12-pie.patch
Patch118: dhcp-3.0.1rc12-inherit-leases.patch
Patch119: dhcp-3.0.1rc13-noexpr.patch
Patch120: dhcp-3.0.1rc14-noconfig.patch
Patch121: dhcp-3.0.1-change_resolv_conf.patch
Patch122: dhcp-3.0.1-default_gateway.patch
Patch123: dhcp-3.0.1.preserve-sent-options.patch
Patch124: dhcp-3.0.1-mis_host.patch
Patch125: dhcp-3.0.1-new-host.patch
Patch126: dhcp-3.0.1-host_dereference.patch
Patch127: dhcp-3.0.1-restrict-unconfigured-IF.patch
Patch128: dhcp-3.0.1-check-empty-new-routers.patch
Patch129: dhcp-3.0.1-fix-ntp.patch
Patch130: dhcp-3.0.1-release-mode-ifup.patch
Patch131: dhcp-3.0.1-dhclient-script-big-fix.patch
Patch132: dhcp-3.0.2rc3-fix-hex.patch
Patch133: dhcp-3.0.2rc3-mem.patch
Patch134: dhcp-3.0.2rc3-dhclient_routes.patch
Patch135: dhcp-3.0.1-z-relro-now.patch
Patch136: dhcp-3.0.2rc3-dhclient-restorecon.patch
Patch137: dhcp-3.0.1-dhclient-config.patch
Patch138: dhcp-3.0.2-pid_file_excl.patch
Patch139: dhcp-3.0.2-dhclient-no-restorecon-or-route.patch
Patch140: dhcp-3.0.2-extended_option_environment.patch
URL: http://isc.org/products/DHCP/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/chkconfig
Requires: kernel >= 2.2.18
BuildRequires:  groff
#BuildRequires: compat-gcc >= 8-3.3.4.2   groff

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
Summary: Provides the dhclient ISC DHCP client daemon and dhclient-script .
Requires: initscripts >= 6.75
Group: System Environment/Base
Obsoletes: dhcpcd

%package devel
Summary: Development headers and libraries for interfacing to the DHCP server
Requires: dhcp = %{epoch}:%{version}
Group: Development/Libraries

%description -n dhclient
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

To use DHCP on your network, install a DHCP service (or relay agent),
and on clients run a DHCP client daemon.  The dhclient package 
provides the ISC DHCP client daemon.

%description devel
Libraries for interfacing with the ISC DHCP server.

%prep
%setup -q

%patch -p1 -b .alignment
%patch100 -p1 -b .jbuild
%patch102 -p1 -b .dhcpctlman
%patch103 -p1 -b .miscfixes
%patch106 -p1 -b .minires
%patch109 -p1 -b .dhcpdman
%patch113 -p1 -b .selinux
%patch114 -p1 -b .initialize
%patch115 -p1 -b .RHscript
%patch116 -p1 -b .staticroutes
%patch117 -p1 -b .pie
%patch118 -p1 -b .inherit-leases
%patch119 -p1 -b .noexp
%patch120 -p1 -b .noconfig
%patch121 -p1 -b .change_resolv_conf
%patch122 -p1 -b .default_gateway
# Patch123 is now upstream in dhcp-3.0.2
# %patch123 -p1 -b .preserve-sent-options
# Patch124 is now upstream in dhcp-3.0.2
# %patch124 -p1 -b .mis-host 
# Patch125 is now upstream in dhcp-3.0.2
# %patch125 -p1 -b .new-host
# Patch126 is now upstream in dhcp-3.0.2
# %patch126 -p1 -b .host-dereference
%patch127 -p1 -b .restrict-unconfigured-IF
%patch128 -p1 -b .check-empty-new-routers
%patch129 -p1 -b .fix-ntp
%patch130 -p1 -b .release-mode-ifup
%patch131 -p1 -b .dhclient-script-big-fix
%patch132 -p1 -b .fix-hex
%patch133 -p1 -b .mem
%patch134 -p1 -b .dhclient_routes
%patch135 -p1 -b .-z-relro-now
%patch136 -p1 -b .dhclient-restorecon
%patch137 -p1 -b .dhclient-dhconfig
%patch138 -p1 -b .pid_file_excl
%patch139 -p1 -b .dhclient-no-restorecon-or-route
%patch140 -p1 -b .extended_option_environment

cp %SOURCE1 .
cat <<EOF >site.conf
VARDB=%{_localstatedir}/lib/dhcp
ADMMANDIR=%{_mandir}/man8
FFMANDIR=%{_mandir}/man5
LIBMANDIR=%{_mandir}/man3
USRMANDIR=%{_mandir}/man1
LIBDIR=%{_libdir}
INCDIR=%{_includedir}
EOF
cat <<EOF >>includes/site.h
#define _PATH_DHCPD_DB          "%{_localstatedir}/lib/dhcp/dhcpd.leases"
#define _PATH_DHCLIENT_DB       "%{_localstatedir}/lib/dhcp/dhclient.leases"
EOF

%build
cat <<EOF >findptrsize.c
#include <stdio.h>
int main(void) { printf("%%d\n", sizeof(void *)); return 0; }
EOF
cc -o findptrsize findptrsize.c
[ "`./findptrsize`" -ge 8 ] && RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DPTRSIZE_64BIT"
%ifarch s390 s390x
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIE"
%else
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fpie"
%endif
#RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's/\ \-mtune\=[^\=\ ]*//'`
./configure --copts "$RPM_OPT_FLAGS"
# -DDEBUG_PACKET -DDEBUG_EXPRESSIONS"
# -DDEBUG_MEMORY_LEAKAGE -DDEBUG_MALLOC_POOL -DDEBUG_REFCNT_DMALLOC_FREE -DDEBUG_RC_HISTORY -DDEBUG_MALLOC_POOL_EXHAUSTIVELY -DDEBUG_MEMORY_LEAKAGE_ON_EXIT -DRC_MALLOC=3"
#make %{?_smp_mflags} CC="gcc33"
make %{?_smp_mflags} CC="cc"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/sysconfig

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 0755 %SOURCE2 %{buildroot}/etc/rc.d/init.d/dhcpd

touch %{buildroot}%{_localstatedir}/lib/dhcp/dhcpd.leases

cat <<EOF > %{buildroot}/etc/sysconfig/dhcpd
# Command line options here
DHCPDARGS=
EOF

install -m0755 %SOURCE3 %{buildroot}/etc/rc.d/init.d/dhcrelay

cat <<EOF > %{buildroot}/etc/sysconfig/dhcrelay
# Command line options here
INTERFACES=""
DHCPSERVERS=""
EOF

# Copy sample dhclient.conf file into position
cp client/dhclient.conf dhclient.conf.sample
chmod 755 %{buildroot}/sbin/dhclient-script
touch debugfiles.list
:;

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add dhcpd
/sbin/chkconfig --add dhcrelay

%preun
if [ $1 = 0 ]; then	# execute this only if we are NOT doing an upgrade
    service dhcpd stop >/dev/null 2>&1
    service dhcrelay stop >/dev/null 2>&1
    /sbin/chkconfig --del dhcpd 
    /sbin/chkconfig --del dhcrelay
fi

%postun
if [ "$1" -ge "1" ]; then
    service dhcpd condrestart >/dev/null 2>&1
    service dhcrelay condrestart >/dev/null 2>&1
fi
exit 0

%files
%defattr(-,root,root)
%doc README RELNOTES dhcpd.conf.sample
%dir %{_localstatedir}/lib/dhcp
%verify(not size md5 mtime) %config(noreplace) %{_localstatedir}/lib/dhcp/dhcpd.leases
%config(noreplace) /etc/sysconfig/dhcpd
%config(noreplace) /etc/sysconfig/dhcrelay
%config /etc/rc.d/init.d/dhcpd
%config /etc/rc.d/init.d/dhcrelay
%{_bindir}/omshell
%{_sbindir}/dhcpd
%{_sbindir}/dhcrelay
%{_mandir}/man1/omshell.1*
%{_mandir}/man5/dhcp-eval.5*
%{_mandir}/man5/dhcpd.conf.5*
%{_mandir}/man5/dhcpd.leases.5*
%{_mandir}/man8/dhcpd.8*
%{_mandir}/man8/dhcrelay.8*

%files -n dhclient
%defattr(-,root,root)
%doc dhclient.conf.sample
%dir %{_localstatedir}/lib/dhcp
/sbin/dhclient
/sbin/dhclient-script
%{_mandir}/man5/dhclient.conf.5*
%{_mandir}/man5/dhclient.leases.5*
%{_mandir}/man8/dhclient.8*
%{_mandir}/man8/dhclient-script.8*
%{_mandir}/man5/dhcp-options.5*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*

%changelog
* Mon Apr 04 2005 Jason Vas Dias <jvdias@redhat.com>
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
- log_error ("Lease with bogus binding state: %d size: %d",
-			   comp -> binding_state,
-			   sizeof(comp->binding_state));
- prints:    'Lease with bogus binding state: 257 1'    !
- compiling with gcc33 (compat-gcc-8-3.3.4.2 fixes for now).

* Mon Jan 03 2005 Jason Vas Dias <jvdias@redhat.com> 7:3.0.1-16
- fix bug 143704: dhclient -r does not work if lease held by
- dhclient run from ifup . dhclient will now look for the pid
- files created by ifup .

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
- that got dropped with the 'new-host' patch. Replacing the '!' .
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
- An upstream patch was obtained which will be in dhcp-3.0.2 .

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
- Update to 3.0, include devel files installed by it (as part of the main package).

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
- chkconfig --del in %preun, not %postun

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
  and made the %postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.
