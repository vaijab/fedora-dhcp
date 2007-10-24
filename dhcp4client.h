/* dhcp4client.h
 *
 * Interface to the ISC dhcp IPv4 client libdhcp4client library.
 *
 * Copyright (C) 2006  Red Hat, Inc. All rights reserved.
 *
 * This copyrighted material is made available to anyone wishing to use,
 * modify, copy, or redistribute it subject to the terms and conditions of
 * the GNU General Public License v.2, or (at your option) any later version.
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY expressed or implied, including the implied warranties of
 * MERCHANTABILITY or FITNESS FOR A * PARTICULAR PURPOSE.  See the GNU General
 * Public License for more details.  You should have received a copy of the
 * GNU General Public License along with this program; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
 * source code or documentation are not subject to the GNU General Public
 * License and may only be used or replicated with the express permission of
 * Red Hat, Inc.
 *
 * Red Hat Author(s): Jason Vas Dias
 *                    David Cantrell
 */

/* include libdhcp_control.h or libdhcp.h for this */
extern struct libdhcp_control_s;

/* The ISC IPv4 DHCP client main() function */
extern int dhcpv4_client(struct libdhcp_control_s *dhc_ctl,
                         int argc, char **argv, char **envp);
