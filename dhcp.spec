%{?!DHCLIENT_EXTENDED_OPTION_ENVIRONMENT:%define DHCLIENT_EXTENDED_OPTION_ENVIRONMENT 1}
%{?!NODEBUGINFO: %define NODEBUGINFO 0}
%{?!LIBDHCP4CLIENT: %define LIBDHCP4CLIENT 1}
Summary: A DHCP (Dynamic Host Configuration Protocol) server and relay agent.
Name:    dhcp
Version: 3.0.4
Release: 15
Epoch:   12
License: distributable
Group: System Environment/Daemons
Source0: ftp://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.gz
Source1: dhcpd.conf.sample
Source2: dhcpd.init
Source3: dhcrelay.init
Source4: dhcpd.conf
Source5: findptrsize.c
Source6: libdhcp4client.pc
Source7: dhcptables.pl
#
Patch: 	  dhcp-3.0-alignment.patch
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
Patch141: dhcp-3.0.2-dhclient-no_isc_blurb.patch
Patch142: dhcp-3.0.2-dhclient-script-restorecon.patch
Patch143: dhcp-3.0.2-dhclient-script-dhcdbd.patch
Patch144: dhcp-3.0.2-dhclient-script-fix-init-state-1.patch
Patch145: dhcp-3.0.2-dhclient-script-dbus-fix-interface.patch
Patch146: dhcp-3.0.2-dhclient_nodelay.patch
Patch147: dhcp-3.0.2-dhclient_decline_backoff.patch
Patch148: dhcp-3.0.2-uint8_binding_state.patch
Patch149: dhcp-3.0.2-dhclient_script_fast+arping.patch
Patch150: dhcp-3.0.3rc1-no-__u16.patch
Patch151: dhcp-3.0.3rc1-boot-file-server.patch
Patch152: dhcp-3.0.3-fast_dhclient.patch
Patch153: dhcp-3.0.3-dhclient-script-ypbind-hup-ok.patch
Patch154: dhcp-3.0.3-trailing_nul_options.patch
Patch155: dhcp-3.0.3-gcc4_warnings.patch
Patch156: dhcp-3.0.4-version.patch
Patch157: dhcp-3.0.3-dhclient-script-up-down-hooks.patch
Patch158: dhcp-3.0.3-bz167273.patch
Patch159: dhcp-3.0.3-failover_ports.patch
Patch160: dhcp-3.0.3-rt15293_bz160655.patch
Patch161: dhcp-3.0.3-static-routes.patch
Patch162: dhcp-3.0.3-dhclient_script_route_metrics.patch
Patch163: dhcp-3.0.3-dhclient-script-bz171312.patch
Patch164: dhcp-3.0.3-bz167028-ibm-unicast-bootp.patch
Patch165: dhcp-3.0.3-trailing_nul_options_2.patch
Patch166: dhcp-3.0.3-bz173619.patch
Patch167: dhcp-3.0.4-gcc4_warnings.patch
Patch168: dhcp-3.0.3-bz176270.patch
Patch169: dhcp-3.0.3-bz176615.patch
Patch170: dhcp-3.0.3-bz177845.patch
Patch171: dhcp-3.0.3-bz181482.patch
Patch172: dhcp-3.0.4-dhcient_ibmzSeries_broadcast.patch
Patch173: dhcp-3.0.4-dhclient_ibmzSeries_-I_option.patch
Patch174: dhcp-3.0.4-H_host-name_-F_fqdn_-T_timeout_options.patch
Patch175: dhcp-3.0.4-bz191470.patch
Patch176: dhcp-3.0.4-dhclient-R_option.patch
Patch177: dhcp-3.0.4-dhclient-script-METRIC.patch
Patch178: dhcp-3.0.4-dhclient-script-ntp-fudge-bz191461.patch

# patch to make the library subtree
Patch179: dhcp-3.0.4-lib-makefile.patch

# patches that _must_ go after the split
Patch180: dhcp-3.0.4-libdhcp4client.patch
Patch181: dhcp-3.0.4-timeouts.patch

URL: http://isc.org/products/DHCP/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/chkconfig
BuildRequires:  groff perl
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

%package -n 	libdhcp4client
Summary: The ISC DHCP IPv4 client in a library for invocation from other programs
Group:   Development/Libraries

%description -n libdhcp4client
The Internet Software Consortium (ISC) Dynamic Host Configuration Protocol (DHCP)
Internet Protocol version 4 (IPv4) client software in a library suitable for
linkage with and invocation by other programs.

%package -n 	libdhcp4client-devel
Summary: Header files for development with the ISC DHCP IPv4 client library
Group:   Development/Libraries

%description -n libdhcp4client-devel
Header files for development with the Internet Software Consortium (ISC) 
Dynamic Host Configuration Protocol (DHCP) Internet Protocol version 4 (IPv4) 
client library .

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
# patches now upstream:
# %patch123 -p1 -b .preserve-sent-options
# %patch124 -p1 -b .mis-host 
# %patch125 -p1 -b .new-host
# %patch126 -p1 -b .host-dereference
# %patch127 -p1 -b .restrict-unconfigured-IF
%patch128 -p1 -b .check-empty-new-routers
%patch129 -p1 -b .fix-ntp
%patch130 -p1 -b .release-mode-ifup
%patch131 -p1 -b .dhclient-script-big-fix
# patches now upstream:
# %patch132 -p1 -b .fix-hex
# %patch133 -p1 -b .mem
%patch134 -p1 -b .dhclient_routes
%patch135 -p1 -b .-z-relro-now
%patch136 -p1 -b .dhclient-restorecon
%patch137 -p1 -b .dhclient-dhconfig
%patch138 -p1 -b .pid_file_excl
%patch139 -p1 -b .dhclient-no-restorecon-or-route
%if %{DHCLIENT_EXTENDED_OPTION_ENVIRONMENT}
%patch140 -p1 -b .extended_option_environment
%endif
%patch141 -p1 -b .no_isc_blurb
%patch142 -p1 -b .restore_restorecon
%patch143 -p1 -b .dhclient-script-dhcdbd
%patch144 -p1 -b .dhclient-script-fix-init-state-1
%patch145 -p1 -b .dhclient-script-dbus-fix-interface
%patch146 -p1 -b .dhclient_no_delay
%patch147 -p1 -b .dhclient_decline_backoff
# patch now upstream:
# %patch148 -p1 -b .uint8_binding_state
%patch149 -p1 -b .dhclient_script_fast+arping
# %patch150 -p1 -b .no-__u16
# ^- patch now upstream
# %patch151 -p1 -b .boot-file-server
# ^- RFC2131 compliance: force users to specify either the
# next-server or server-name options for the tftp-boot-server.
%patch152 -p1 -b .fast_dhclient
%patch153 -p1 -b .ypbind_hup_ok
#%patch154 -p1 -b .trailing_nul_options
# ! %patch155 -p1 -b .gcc4_warnings
%patch156 -p1 -b .version
%patch157 -p1 -b .dhclient-script-up-down-hooks
%patch158 -p1 -b .bz167273
%patch159 -p1 -b .failover_ports
#%patch160 -p1 -b .rt15293_bz160655
#^- patch now upstream 
%patch161 -p1 -b .static-routes
%patch162 -p1 -b .dhclient_script_route_metrics
%patch163 -p1 -b .bz171312
%patch164 -p1 -b .bz167028
#%patch165 -p1 -b .trailing_nul_options_2
#^- patch now upstream
%patch166 -p1 -b .bz173619
%patch167 -p1 -b .gcc4_warnings
%patch168 -p1 -b .bz176270
# %patch169 -p1 -b .bz176615
# ^- patch now upstream
%patch170 -p1 -b .bz177845
%patch171 -p1 -b .bz181482
%patch172 -p1 -b .dhclient_ibmzSeries_broadcast
%patch173 -p1 -b .dhclient_ibmzSeries_-I_option
%patch174 -p1 -b .dhclient_-H_host-name_-F_fqdn_-T_timeout_options
%patch175 -p1 -b .bz191470
%patch176 -p1 -b .dhclient-R_option
%patch177 -p1 -b .dhclient-script-METRIC
%patch178 -p1 -b .dhclient-script-ntp-fudge-bz191461
%patch179 -p1 -b .lib-makefile

cp %SOURCE1 .
cat <<EOF >site.conf
VARDB=%{_localstatedir}/lib/dhcpd
ADMMANDIR=%{_mandir}/man8
FFMANDIR=%{_mandir}/man5
LIBMANDIR=%{_mandir}/man3
USRMANDIR=%{_mandir}/man1
LIBDIR=%{_libdir}
INCDIR=%{_includedir}
EOF
cat <<EOF >>includes/site.h
#define _PATH_DHCPD_DB          "%{_localstatedir}/lib/dhcpd/dhcpd.leases"
#define _PATH_DHCLIENT_DB       "%{_localstatedir}/lib/dhclient/dhclient.leases"
EOF

cp -fp %SOURCE5 .
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Dlint -Werror -Wno-unused"
%{__cc} -I. -o findptrsize findptrsize.c
[ "`./findptrsize`" -ge 8 ] && RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DPTRSIZE_64BIT"
%ifarch s390 s390x
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIE"
%else
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fpie"
%endif
%if %{DHCLIENT_EXTENDED_OPTION_ENVIRONMENT}
    RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DEXTENDED_NEW_OPTION_INFO"
%endif
#RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's/\ \-mtune\=[^\=\ ]*//'`
%if %{NODEBUGINFO}
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -g3 -gdwarf-2"
%endif
CC="%{__cc}" ./configure --copts "$RPM_OPT_FLAGS"
# -DDEBUG_PACKET -DDEBUG_EXPRESSIONS"
# -DDEBUG_MEMORY_LEAKAGE -DDEBUG_MALLOC_POOL -DDEBUG_REFCNT_DMALLOC_FREE -DDEBUG_RC_HISTORY -DDEBUG_MALLOC_POOL_EXHAUSTIVELY -DDEBUG_MEMORY_LEAKAGE_ON_EXIT -DRC_MALLOC=3"
#make %{?_smp_mflags} CC="gcc33"

%if %{LIBDHCP4CLIENT}
sed 's/@DHCP_VERSION@/'%{version}'/' < %SOURCE5 >libdhcp4client.pc
make -f libdhcp4client.Makefile CC="%{__cc}" libdhcp4client/.
%patch180 -p1 -b .lib
%patch181 -p1 -b .timeouts
# can't handle make -j yet!
%endif

%build
make %{?_smp_mflags} CC="%{__cc}"
%if %{LIBDHCP4CLIENT}
sed 's/@DHCP_VERSION@/'%{version}'/' < %SOURCE5 >libdhcp4client.pc
make -f libdhcp4client.Makefile CC="%{__cc}"
# can't handle make -j yet!
%endif

%if %{NODEBUGINFO}
%define debug_package %{nil}
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/sysconfig

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 0755 %SOURCE2 %{buildroot}/etc/rc.d/init.d/dhcpd

touch %{buildroot}%{_localstatedir}/lib/dhcpd/dhcpd.leases
mkdir -p  %{buildroot}%{_localstatedir}/lib/dhclient/
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
#
# Create per-package copies of dhcp-options and dhcp-eval common man-pages:
cp -fp ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcp-options.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcpd-options.5 
cp -fp ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcp-options.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/dhclient-options.5 
cp -fp ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcp-eval.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcpd-eval.5 
cp -fp ${RPM_BUILD_ROOT}%{_mandir}/man5/dhcp-eval.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/dhclient-eval.5 
#
# Why not ship the doc/ documentation ? Some of it is quite useful.
# Also generate DHCP options tables for C, perl, python:
#
/usr/bin/perl %SOURCE7 > doc/dhcp_options.h
/usr/bin/perl %SOURCE7 -pe > doc/dhcp_options.pl
/usr/bin/perl %SOURCE7 -py > doc/dhcp_options.py
/usr/bin/perl %SOURCE7 -d  > doc/dhcp_options.txt
#
# Fix bug 163367: install default (empty) dhcpd.conf:
cp -fp %SOURCE4 %{buildroot}/etc
#
%if %{LIBDHCP4CLIENT}
# libdhcp4client install
sed 's/@DHCP_VERSION@/'%{version}'/' < %SOURCE6 >libdhcp4client.pc
make -f libdhcp4client.Makefile install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
%endif
%if !%{NODEBUGINFO}
#
# Fix debuginfo files list - don't ship links to .c files in the buildroot :-)
work=work.`./configure --print-sysname`;
find $work -type l -a -name '*.c' | 
while read f; do 
   rm -f $f; 
   cp -fp ${f#$work/} $f; 
done
%else
/usr/lib/rpm/brp-compress
exit 0
%endif
:;

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add dhcpd
/sbin/chkconfig --add dhcrelay
if [ "$1" -ge 1 ]; then
   if [ ! -e %{_mandir}/man5/dhcp-options.5.gz ]; then
	/bin/ln -s %{_mandir}/man5/dhcpd-options.5.gz %{_mandir}/man5/dhcp-options.5.gz;
   fi;
   if [ ! -e %{_mandir}/man5/dhcp-eval.5.gz ]; then
	/bin/ln -s %{_mandir}/man5/dhcpd-eval.5.gz %{_mandir}/man5/dhcp-eval.5.gz;
   fi;
fi;

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
elif [ "$1" -eq 0 ]; then
    if [ -e %{_mandir}/man5/dhclient-options.5.gz  ]; then
	/bin/ln -sf %{_mandir}/man5/dhclient-options.5.gz %{_mandir}/man5/dhcp-options.5.gz;
    fi;
    if [ -e %{_mandir}/man5/dhclient-eval.5.gz  ]; then
	/bin/ln -sf %{_mandir}/man5/dhclient-eval.5.gz %{_mandir}/man5/dhcp-eval.5.gz;
    fi;
fi
exit 0

%post -n dhclient
if [ "$1" -ge 1 ]; then
   if [ ! -e %{_mandir}/man5/dhcp-options.5.gz ]; then
	/bin/ln -s %{_mandir}/man5/dhclient-options.5.gz %{_mandir}/man5/dhcp-options.5.gz;
   fi;
   if [ ! -e %{_mandir}/man5/dhcp-eval.5.gz ]; then
	/bin/ln -s %{_mandir}/man5/dhclient-eval.5.gz %{_mandir}/man5/dhcp-eval.5.gz;
   fi;   
fi
:;

%postun -n dhclient
if [ "$1" -eq 0 ]; then
    if [ -e %{_mandir}/man5/dhcpd-options.5.gz  ]; then
	/bin/ln -sf %{_mandir}/man5/dhcpd-options.5.gz %{_mandir}/man5/dhcp-options.5.gz;
    fi;
    if [ -e %{_mandir}/man5/dhcpd-eval.5.gz  ]; then
	/bin/ln -sf %{_mandir}/man5/dhcpd-eval.5.gz %{_mandir}/man5/dhcp-eval.5.gz;
    fi;
fi
:;   

%post -n libdhcp4client -p /sbin/ldconfig

%postun -n libdhcp4client -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README RELNOTES dhcpd.conf.sample doc/*
%dir %{_localstatedir}/lib/dhcpd
%verify(not size md5 mtime) %config(noreplace) %{_localstatedir}/lib/dhcpd/dhcpd.leases
%config(noreplace) /etc/sysconfig/dhcpd
%config(noreplace) /etc/sysconfig/dhcrelay
%config(noreplace) /etc/dhcpd.conf
%config /etc/rc.d/init.d/dhcpd
%config /etc/rc.d/init.d/dhcrelay
%{_bindir}/omshell
%{_sbindir}/dhcpd
%{_sbindir}/dhcrelay
%{_mandir}/man1/omshell.1*
%{_mandir}/man5/dhcpd.conf.5*
%{_mandir}/man5/dhcpd.leases.5*
%{_mandir}/man8/dhcpd.8*
%{_mandir}/man8/dhcrelay.8*
%{_mandir}/man5/dhcpd-options.5*
%{_mandir}/man5/dhcpd-eval.5*
%ghost %{_mandir}/man5/dhcp-options.5.gz
%ghost %{_mandir}/man5/dhcp-eval.5.gz

%files -n dhclient
%defattr(-,root,root)
%doc dhclient.conf.sample
%dir %{_localstatedir}/lib/dhclient
/sbin/dhclient
/sbin/dhclient-script
%{_mandir}/man5/dhclient.conf.5*
%{_mandir}/man5/dhclient.leases.5*
%{_mandir}/man8/dhclient.8*
%{_mandir}/man8/dhclient-script.8*
%{_mandir}/man5/dhclient-options.5*
%{_mandir}/man5/dhclient-eval.5*
%ghost %{_mandir}/man5/dhcp-options.5.gz
%ghost %{_mandir}/man5/dhcp-eval.5.gz

%files devel
%defattr(-,root,root)
%if %{LIBDHCP4CLIENT}
%exclude %{_libdir}/libdhcp4client*
%exclude %{_includedir}/dhcp4client
%endif
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*

%if %{LIBDHCP4CLIENT}
%files -n libdhcp4client
%defattr(-,root,root,-)
%{_libdir}/libdhcp4client.so.*

%files -n libdhcp4client-devel
%defattr(0644,root,root,0755)
%{_includedir}/dhcp4client*
%{_libdir}/pkgconfig/libdhcp4client.pc
%{_libdir}/libdhcp4client.a
%{_libdir}/libdhcp4client.so
%endif

%changelog
* Thu Jun 22 2006 Peter Jones <pjones@redhat.com> - 12:3.0.4-15
- Make timeout dispatch code not recurse while traversing a linked
  list, so it doesn't try to free an entries that have been removed.
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
  must be specified with the 'next-server' option ( not the tftp-boot-server option ?!?)
  which causes PXE boot clients to fail to load anything after the boot file.

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
