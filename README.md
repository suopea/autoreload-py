# python autoreload

This script detects when you save changes in your script, and automatically runs it again.

Lots of time and attention gets wasted on switching between an editor and the terminal, manually running the script after making changes. Even if it's just a few keypresses, we do it so often that it might as well be automated. 


![autoreload doing what's described below](gif/autoreload.gif)

## how to use it

There's no dependencies, you only need the `autoreload.py` file!

Just replace `python3` with `python3 autoreload.py`, so if you would normally do
```bash
python3 your_script.py arg1 arg2
```
then do this:
```bash
python3 autoreload.py your_script.py arg1 arg2
```

`your_script.py` will run. Whenever any python script in the current directory or subdirectories is changed, it will terminate the previously started script(if it's still running), and start it again. 

If `your_script.py` terminates, `autoreload` will wait for a change to be made and then will run it again.

## usage with one or none scripts

![autoreload handling an empty directory](gif/empty_dir.gif)

If there's only one .py file in the current directory, you can just run `autoreload` and it will automatically run the lonely script. 

You can even run `autoreload` without arguments in an empty directory, in which case it will wait for a script to be created, then run it

## you'll want to have an alias

The previous example assumes that `autoreload.py` is in the same directory as `your_script.py`. You probably don't want that, so instead make an alias using an absolute path so that you can use it anywhere like this:
```bash
autoreload your_script.py arg1 arg2
```

So to your rc file add something like:
```bash
alias autoreload='python3 ~/code/autoreload-py/autoreload.py'
```
