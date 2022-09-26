# How to disable middle click within the Linux operating system

This is useful when your mouse pointing device has a scroll wheel that performs as a middle button.

In the terminal program, type and press enter:

```
xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"
```

This will disable the middle click until you log out.

-------------------

## To make a script for easy running on multiple occasions:

In the terminal, go to the Desktop:

```
cd ~/Desktop
```

_NOTE: Throughout this document, after each command (e.g. "xmodmap....10", above), press the {Enter} key._

Write the command into a file:

```
echo 'xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"' > disable-middle-click.sh
```

Make that file executable:

```
chmod +x disable-middle-click.sh
```

Now, you may run the file:

```
./disable-middle-click.sh
```

---------------

## To re-enable middle click:

```
xmodmap -e "pointer = 1 2 3 4 5 6 7 8 9 10"
```

When the computer is rebooted, most likely it will revert to a state in which the middle click function of the scroll wheel/middle button is enabled.

