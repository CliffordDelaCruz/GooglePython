#!/bin/bash

if grep "127.0.0.1" /etc/localhosts; then
	echo "Everything is ok."
else
	echo "ERROR! 127.0.0.1 is not in etc/localhost"
fi
