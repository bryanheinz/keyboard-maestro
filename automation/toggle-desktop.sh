#!/bin/bash

dtopState=$(defaults read com.apple.finder CreateDesktop)

if [[ "$dtopState" == "true" ]]; then
    defaults write com.apple.finder CreateDesktop false && killall Finder
else
    defaults write com.apple.finder CreateDesktop true && killall Finder
fi
