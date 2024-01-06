# Raspberry-pi-setup-headless
```some code```
This is the procedure to install Ubuntu 20.04 on a Raspberry Pi 4B. First, download the Raspberry Pi Imager. When you run the Raspberry Pi Imager, choose Ubuntu 20.04 as the operating system and write it onto an SD card. Don't forget to enable SSH and headless mode, and take note of the IP address, username, password, and the SSID and password for the wireless network you are connecting to. After plugging in the SD card and powering up the Raspberry Pi, wait for the green light to stop flashing. Then, start up your laptop and install the necessary packages. Once you find the name of your Raspberry Pi in the list, note the IP address and check if it matches the one you set during the installation process. SSH into the Raspberry Pi using the bash terminal. After entering the password, you should be successfully logged into the Raspberry Pi. If logging in for the first time, you may be asked to verify the authenticity of the IP address, to which you can respond affirmatively to add it to your trusted IP address list.

To update the summary and include the usage of the nmap package to get the IP addresses of connected devices to the network, you can add the following information:
To obtain the IP addresses of connected devices to the network, the nmap package can be used. By running a quick NMAP scan, network administrators can inventory network devices and monitor remote host status. For example, the command nmap ```sudo nmap -sn 192.168.2.0/24``` can be used to perform a ping scan on the whole subnet range and retrieve the IP addresses of the connected devices. This command will ping all the IP addresses to see if they respond and provide a list of the hostname and IP address for each device that responds to the ping.This addition provides an overview of how the nmap package can be used to scan the network and obtain the IP addresses of connected devices.

Refer to the pdf below for GPIO pin locations:
https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf

Some usefull commands

`export ROS_IP=192.168.2.12`
`export ROS_MASTER_URI=http://192.168.2.148:11311/`

`rostopic pub /testtopic std_msgs/String -r 2 -- "Hello"`

`rostopic echo /testtopic`

`ssh ra-pi@192.168.2.148`

`source /opt/ros/noetic/setup.bash`

`sudo ufw disable`

Environment Setup

`echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc`
`source ~/.bashrc`
