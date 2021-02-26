# Author: Ben Kallus
# Reads input from stdin, prints it back case-swapped.

while 1:print("".join(chr(ord(c)+(("@"<c<"[")-("`"<c<"{"))*32)for c in input()))