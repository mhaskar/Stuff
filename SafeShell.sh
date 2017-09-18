#!/bin/sh

hn=$(hostname)
while true
do
read -r -p "SafeShell@$hn>> " command
$command
done
