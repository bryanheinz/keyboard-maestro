tell application "Microsoft Outlook"
	set msgSelection to get selection
	set flagStatus to todo flag of msgSelection as string
	if flagStatus is "not completed" then
		# message is flagged, unflag
		set todo flag of msgSelection to not flagged
	else if flagStatus is "not flagged" then
		# message is not flagged, flag
		set todo flag of msgSelection to not completed
	end if
end tell
