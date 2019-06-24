-----
install lirc 
sudo apt-get install lirc liblircclient-dev

lircd -v 
	lircd 0.9.4c

------
config

path 
/boot/config.txt
add in file

	dtoverlay=lirc-rpi,gpio_in_pin=18

-------
old version not use
path  
/etc/modules
add in file 
	lirc_dev
	lirc_rpi gpio_in_pin=18

