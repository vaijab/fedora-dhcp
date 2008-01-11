#!/bin/bash
#
# Fetch latest version of LDAP patch.  The patch is downloaded and split in
# the ldap/ subdirectory.  It is up to the packager to merge the updates with
# the RPM.
#
# Upstream: http://home.ntelos.net/~masneyb/
#
# David Cantrell <dcantrell@redhat.com>
#

CWD=$(pwd)

rm -f masneyb.html-$$
wget -O masneyb.html-$$ http://home.ntelos.net/~masneyb
p="$(grep "ldap-patch" masneyb.html-$$ | cut -d '>' -f 3 | cut -d '<' -f 1)"
rm -f masneyb.html-$$

rm -rf ldap/
mkdir -p ldap/
cd ldap/
wget -N http://home.ntelos.net/~masneyb/$p
splitdiff -a -d $p
rm -f $p

rm -f *_debian_*
