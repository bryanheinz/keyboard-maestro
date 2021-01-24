# Text Manipulation
These are my Keyboard Maestro text manipulation scripts.

## Setup
This is my setup to run these text manipulation macros
- New named clipboard "Text Manipulation"
- New macro with these actions:
- Action - Copy to Named Clipboard "Text Manipulation"
- Action - Execute Shell Script *file* with input from **Named Clipboard** "Text Manipulation" and *save results to variable* "output_text"
- Action - Insert Text by Pasting *variable* `%Variable%output_text%`

I've found this the be efficient with minimal impact to my [LaunchBar](https://www.obdev.at/products/launchbar/index.html) clipboard history.

I created a macro called `_template` and assigned it my `_template.py` script to dupe and easily create new text manipulation macros.
