#!/usr/bin/python3

# <div class="line"><span class="key">Ctrl</span>+<span class="key">z</span>: <span class="function">Undo</span></div>
shortcuts = '''Window management
⊞+Tab:Show open windows
Alt+Tab:Switch windows
Ctrl+Tab:Switch tabs
Shift:Reverse switch
Alt+F4:Close window
Ctrl+F4:Close tab
⊞+←/↑/↓/→:Move window
#PC management
⊞+l:Lock your computer
⊞+d:Show desktop
⊞+p:Choose projector mode
#Browsing
Ctrl+f:Find
F5:Refresh
Ctrl+r:Refresh
F11:Fullscreen
Alt+←:Back
Alt+→:Forward
#Cursor movement
Home:Beginning of line
End:End of line
PgUp:Move one page up
PgDn:Move one page down
Ctrl+← or →:Move one word
Ctrl+↑ or ↓:Move one paragraph
Ctrl+Home or End:Move to ends of document
Shift:Select while moving cursor
Ctrl+backspace:Delete one word
#File
Ctrl+n:New
Ctrl+s:Save
Ctrl+o:Open
Ctrl+p:Print
#Editing
Ctrl+z:Undo
Ctrl+y:Redo
Ctrl+x:Cut
Ctrl+c:Copy
Ctrl+v:Paste
Ctrl+a:Select all
#Formatting
Ctrl+b:Bold
Ctrl+i:Italic
Ctrl+u:Underline
'''

output = '''<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>Keyboard shortcuts</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>

<div class="container">'''

for section in shortcuts.split('#'):
    lines = section.split('\n')

    output += '<div class="section">\n<div class="heading">'
    output += lines[0]
    lines = lines[1:-1]
    output += '</div>\n'

    for line in lines:
        halves = line.split(':')
        keys = halves[0].split('+')
        output += '<div class="line">'
        for key in keys:
            output += '<span class="key">'
            output += key
            output += '</span>'
            output += '<span class="plus">+</span>'
        output = output[0:-27]
        output += ':<span class="function"> '
        output += halves[1]
        output += '</span></div>\n'

    output += '</div>\n\n'

output += '''</div>
</body>
</html>
'''

print(output)

file = open('index.html', 'w')
file.write(output)
file.close()
