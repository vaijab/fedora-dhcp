# Makefile for source rpm: dhcp
# $Id$
NAME := dhcp
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
