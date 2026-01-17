# python autoreload

This script detects when you save changes in your script, and automatically runs it again.

Lots of time and attention gets wasted on switching between an editor and the terminal, manually running the script after making changes. Even if it's just a few keypresses, we do it so often that it might as well be automated. 

## how to use it

just replace `python3` with `python3 autoreload.py`, so if you would normally do
```bash
python3 your_script.py arg1 arg2
```
then do this:
```bash
python3 autoreload.py your_script.py arg1 arg2
```

`your_script.py` will be then run in python. Whenever any python script in the current directory or subdirectories is changed, it will terminate the previously started script(if it's still running), and start it again. 

If `your_script.py` terminates, `autoreload` will wait for a change to be made and then will run it again.


It's probably best to turn it into an alias using an absolute path so that you can use it anywhere like this:
```bash
autoreload your_script.py arg1 arg2
```

So to your rc file add something like:
```bash
alias autoreload='python3 ~/code/autoreload-python/autoreload.py'
```
