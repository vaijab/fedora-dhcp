/* dhcp4client.h
 *
 *  Interface to the ISC dhcp IPv4 client libdhcp4client library.
 *
 *
 *  Copyright(C) Jason Vas Dias <jvdias@redhat.com> Red Hat Inc. May 2006
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation at 
 *           http://www.fsf.org/licensing/licenses/gpl.txt
 *  and included in this software distribution as the "LICENSE" file.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 */

/* include libdhcp_control.h or libdhcp.h for this */
struct libdhcp_control_s;

/* The ISC IPv4 DHCP client main() function */
extern int dhcpv4_client(struct libdhcp_control_s *dhc_ctl,
                         int argc, char **argv, char **envp);
