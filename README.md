# Python ft232_cbus_config

Python script to configure FT232 CBUS pins. Requires python-ftdi1.

Inspired by: https://github.com/trabucayre/ft232_cbus_config

By default CBUS2 and CBUS3 are configured in IOMODE while CBUS0 and CBUS1 are
left at their default (TXLED/RXLED). Edit the script to change the default
settings.

If you need to control the GPIOs without detaching the kernel FTDI driver, see
the ftdi-cbus-ctrlep.py script:
https://gist.github.com/falstaff84/299639de3c5cfd97ba01db409c03b5b6
