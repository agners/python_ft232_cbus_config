#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python script to program FTDI EEPROM.

Small program which sets CBUS2/3 function to IOMODE. If you have multiple
FTDI chips connected, use the serial number (typically found in the symlink
located in /dev/serial/by-id:
    ./ft232_cbus_config.py A10XXXXX

Uses libftdi1 Python bindings, e.g. provided by python-ftdi1 on Debian"""

import ftdi1 as ftdi
import subprocess
import sys
import time

def set_eeprom_value(ftdic, function, mode):
    ret = ftdi.set_eeprom_value(ftdic, function, mode);
    if ret < 0:
        print("ftdi.set_eeprom_value(): %d" % ret, file=sys.stderr)
        sys.exit(1)


def main():
    """Main program"""
    restart = True
    ftdic = ftdi.new()
    serial = None

    if len(sys.argv) > 1:                                                                                                                   
        serial = sys.argv[1]

    ret = ftdi.usb_open_desc(ftdic, 0x0403, 0x6001, None, None)
    if ret < 0:
        print("ftdi.usb_open(): %d" % ret, file=sys.stderr)
        sys.exit(1)

    ret = ftdi.read_eeprom(ftdic)
    if ret < 0:
        print("ftdi.read_eeprom(): %d" % ret, file=sys.stderr)
        sys.exit(1)

    ret = ftdi.eeprom_decode(ftdic, True)
    if ret < 0:
        print("ftdi.eeprom_decode(): %d" % ret, file=sys.stderr)
        sys.exit(1)
    print()

    set_eeprom_value(ftdic, ftdi.CBUS_FUNCTION_0, ftdi.CBUS_TXLED)
    set_eeprom_value(ftdic, ftdi.CBUS_FUNCTION_1, ftdi.CBUS_RXLED)
    set_eeprom_value(ftdic, ftdi.CBUS_FUNCTION_2, ftdi.CBUS_IOMODE)
    set_eeprom_value(ftdic, ftdi.CBUS_FUNCTION_3, ftdi.CBUS_IOMODE)

    ret = ftdi.eeprom_build(ftdic);
    if ret < 0:
        print("ftdi.eeprom_build(): %d" % ret, file=sys.stderr)
        sys.exit(1)

    print("New EEPROM settings:")
    ret = ftdi.eeprom_decode(ftdic, True)
    if ret < 0:
        print("ftdi.eeprom_decode(): %d" % ret, file=sys.stderr)
        sys.exit(1)

    ret = ftdi.write_eeprom(ftdic);
    if ret < 0:
        print("ftdi.write_eeprom(): %d" % ret, file=sys.stderr)
        sys.exit(1)

    ftdi.free(ftdic)

main()


