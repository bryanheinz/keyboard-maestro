#!/bin/zsh

theUser=$(/usr/bin/stat -f "%Su" /dev/console)

if [[ ! -f /Library/Developer/CommandLineTools/usr/bin/git ]]; then
    echo "git doesn't appear to be installed."
    echo "manually install from https://github.com/bryanheinz/keyboard-maestro"
    exit 1
fi

if [[ -d /usr/local/keyboard-maestro ]]; then
    cd /usr/local/keyboard-maestro
    git pull
else
    cd /usr/local/
    sudo git clone https://github.com/bryanheinz/keyboard-maestro
    sudo chown -R $theUser /usr/local/keyboard-maestro
fi
