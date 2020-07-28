#!/usr/bin/env python

port1 = {21: "FTP", 22: "SSH", 23: "telnet", 80: "http"}
print({port1[i]: i for i in port1})
