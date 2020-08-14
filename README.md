# Python
Programming courses and projects in Python


# Configure VSCode

**Goal**: Switch between Editting file and Terminal via Hotkeys.

1) File > Preferences > Keyboard Shortcuts

2) Switch focus to Active Editor/File. Search for: `workbench.action.focusActiveEditorGroup`

3) Set Hot key: `Ctrl + K`

4) Switch focus to Terminal. Search for: `workbench.action.terminal.focus`

5) Hot key: `Ctrl + J`

# Re-map Keyboard Bindings

**Goal**: Change `CAPS-LOCK` to `ESC`

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
7) Second row: 02 00 00 00 01 00 3A 00 
> Note: the `02` means are remapping a single key. It is always 1 + the number of keys you want to remap (n = 1 + keys). `01` is the ESC character key, and `3A` is the CAPS LOCK. We start with the key we want to map TO, followed by the key we want to map FROM. Thus we are mapping `3A` to `01` (CAPS LOCK to ESC)!
8) Last row: 00 00 00 00

**In summary:**
Row 1: 00 00 00 00 00 00 00 00

Row 2: 02 00 00 00 01 00 3A 00

Row 3: 00 00 00 00

9) Save the file
10) **Reboot computer for changes to take effect**

11) If you wish to remove the mapping. Go back to the `Scancode Map` in `regedit`, and delete the `Scancode Map`. **Reboot computer again for changes to take effect**.







