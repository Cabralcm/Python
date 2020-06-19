# Python
Programming in Python


# Configure Editor

Switch focus to Active Editor/File: `workbench.action.focusActiveEditorGroup`

Hot key: `Ctrl + K`

Switch focus to Terminal: `workbench.action.terminal.focus`

Hot key: `Ctrl + J`

# Re-map Keyboard Bindings

Goal: Change `CAPS-LOCK` to `ESC`

[Windows 10 Remap Video](https://www.youtube.com/watch?v=PlPoG7MAt_g)
[Guide](https://vim.fandom.com/wiki/Map_caps_lock_to_escape_in_Windows)

|Key| Hex Value|
|---|---|
|ESC| 01|
|Caps Lock | 3A|

1) Start > Run > `regedit`
2) Go to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout`
3) Singular `Keyboard Layout` without the **s**!
4) In the white area, right click, create new `binary file`. 
5) Name the file `Scancode Map`
6) Pad the first row with all zeros. That is: 00 00 00 00 00 00 00 00
7) Second row: 02 00 00 00 01 00 3A 00 (the 02 means 1 key to remap, 03 would be mean 2 keys to remap, always k = 1 + num_remappings)
8) Last row: 00 00 00 00

In summary:
Row 1: 00 00 00 00 00 00 00 00
Row 2: 02 00 00 00 01 00 3A 00
Row 3: 00 00 00 00

9) Save the file
10) **Reboot computer for changes to take effect**

11) If you wish to remove the mapping. Go back to the `Scancode Map` in `regedit`, and delete the `Scancode Map`. **Reboot computer again for changes to take effect**.







