#!/bin/zsh

baseDir=$(dirname "$0")
kmDir="/usr/local/keyboard-maestro"
theUser=$(/usr/bin/stat -f "%Su" /dev/console)

if [[ ! -d $kmDir ]]; then
    sudo ln -s "$baseDir" "$kmDir"
    echo "Created Keyboard Maestro symlink from $baseDir to $kmDir."
fi
