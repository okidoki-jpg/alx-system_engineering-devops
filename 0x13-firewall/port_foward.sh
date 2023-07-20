#!/usr/bin/env bash

sudo echo 1 > /proc/sys/net/ipv4/ip_forward

sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80

mkdir -p /etc/iptables/
touch /etc/iptables/rules.v4
touch /etc/iptables/rules.v6
sudo iptables-save > /etc/iptables/rules.v4
sudo iptables-save > /etc/iptables/rules.v6

