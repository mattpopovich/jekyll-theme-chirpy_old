---
# See defaults in _config
title: "How to install the Resynthesizer plugin for GIMP on Mac (2021)"
author: Matt Popovich
date: 2021-04-10 12:23:02 -0600
categories: [Blog, YouTube] # <=2 values here: top category and sub category
tags: [youtube, linux, ubuntu, GIMP, tech, tutorial, how to]       # TAG names should always be lowercase
layout: post
pin: false
---

# UPDATE:
⚠️ There is an easier way to do this!! ⚠️

Please see my updated blog post [here](/posts/updated-how-to-install-the-resynthesizer-plugin-for-gimp-on-mac-2022/) for the details!

Below is the old method...

<div style="text-align:center">
<iframe width="560" height="315"
src="https://www.youtube.com/embed/MHwtKg0tws8"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>
</div>

# Intro
This article goes over how to install the Resynthesizer plugin for GIMP on Mac. It likely will not work when you immediately install it, but there's a pretty simple solution. I spent *waaaay* too much time one Sunday trying fix this, from building GIMP from source, then trying to rebuild this plugin, etc... thankfully none of that is necessary. There's a very easy solution that [Werner Eugster](http://homepage.agrl.ethz.ch/eugsterw/knowhow/gimp-resynthesizer/) found and below I'll elaborate on how to successfully use his solution to run the Resynthesizer plugin to automatically remove an object from an image. Let's go!

# [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Download and install [GIMP](https://www.gimp.org/downloads/)
2. Download the Resynthesizer plugin for Mac: [ResynthesizerPlugin-Gimp-2.10-osx.tgz
](https://github.com/aferrero2707/gimp-plugins-collection/releases/download/continuous/ResynthesizerPlugin-Gimp-2.10-osx.tgz)
3. Extract the plugin and copy its contents to `/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins`
4. Try to run it on an image (Filters --> Enhance --> "Heal selection...").
  * If it works, you're good to go! If not, continue
5. Check if you have `libintl` installed: `ls /usr/local/lib/libintl*`
  * If you have `libintl.9` installed and Resynthesizer is not working... not sure how to help you :(
  * If you have `libintl` installed, skip to step 8
  * If you don't have `libintl` installed, continue
6. Check if you have brew installed `$ brew`. If not, install it from [https://brew.sh](https://brew.sh).
7. Fully update and upgrade brew via `brew update` and `brew upgrade` (this will take some time, ~10mins/command)
8. You should now have `libintl.8` (or others?) installed. Create a symbolic link to fake that you have `libintl.9` installed: `ln -s libintl.8.dylib libintl.9.dylib`
9. Restart GIMP, *Heal selection...* should now work! 🤞


# Download and Install GIMP
For starters, we need to download and install GIMP. You can download it from [here](https://www.gimp.org/downloads/). The current version (that I used for this tutorial) is 2.10.22 (revision 3). If you're on Mac, you can open (mount) that downloaded file then click and drag GIMP to the Applications folder. If you're on another OS, follow the instructions GIMP gives you :)

# Download and Install the Resynthesizer Plugin
We can download the Resynthesizer plugin from aferrero2707's repo on GitHub: [gimp-plugin-collections](https://github.com/aferrero2707/gimp-plugins-collection). If you navigate to the releases and then to continuous build, you can scroll down and see all the plugins available. We want to download [ResynthesizerPlugin-Gimp-2.10-osx.tgz
](https://github.com/aferrero2707/gimp-plugins-collection/releases/download/continuous/ResynthesizerPlugin-Gimp-2.10-osx.tgz). Once downloaded, you can extract it and open up the resulting folder to see a bunch of Python files. We need to copy them to GIMP's plugin folder. To find GIMP's plugin folder, you can open GIMP, then go to GIMP-2.10 (in the menu bar) --> Preferences --> scroll down on the left column to Folders, click on Folders to expand it --> Plug-ins. You will likely see two different options for placing these plugin files:
```
/Users/<username>/Libary/Application Support/GIMP/2.10/plug-ins
/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins
```
You can copy to either one, but `/Applications` is easier (you need to create the folder for `/Users`). You can click on the `/Applications/...` path in the window to select it, then you can open that path by clicking on the office cabinet-looking icon on the top right which will show the tooltip "Show file location in the file manager". Once that is open, we can select and drag all of the python files over to that window, quit GIMP (Command (⌘) + Q or GIMP-2.10 --> Quit GIMP-2.10), re-open GIMP, and the Resynthesizer plugin should appear as an option under Filters --> Enhance --> "Heal selection..."!

# Testing the Resynthesizer Plugin (Heal selection)
Now that we have installed the Resynthesizer plugin, we can give it a quick test to see if it will work (likely not). Let's start by importing an image into GIMP (click and drag an image into GIMP, then [if necessary] click convert to change the color profile to what GIMP prefers). Next, we can select an area that contains an object we want to remove (by selecting the "Free Select" tool [press "f"] and clicking around the outside of our object or by selecting the "Rectangle Select" tool [press "r"] and making a rectangle around our object (less precise)). Finally, we can try to run the Resynthesizer plugin: Filters --> Enhance --> "Heal selection..." --> OK. If it works, you're good to go! Unfortunately for me, I was presented with [the following errors](https://github.com/aferrero2707/gimp-plugins-collection/issues/10):

```
Calling error for procedure 'gimp-procedural-db-proc-info':
Procedure 'plug-in-resynthesizer' not found
```
```
An error occurred running python_fu_heal_selection
error: procedure not found
```
```
Traceback (most recent call last):
  File "/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 740, in response
    dialog.res = run_script(params)
  File "/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 361, in run_script
    return apply(function, params)
  File "/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins/plugin-heal-selection.py", line 148, in heal_selection
    pdb.plug_in_resynthesizer(timg, tdrawable, 0,0, useBorder, work_drawable.ID, -1, -1, 0.0, 0.117, 16, 500)
error: procedure not found
```

# Fixing the Resynthesizer Plugin via a Symbolic Link
In computer terms, the plugin is looking to use a library that we do not have: `libintl.9`. I don't know how to get that *exact* version of the library, but we can easily get `libintl.8`, tell the plugin to use that version and carry on our merry way.

## Checking for `libintl`
To check if you already have `libintl.8` installed, open *Terminal*, go to the `/usr/local/lib` directory via `cd /usr/local/lib`, and try to list all files named "libintl" via `ls libintl*`. If it outputs `libintl.8` or even `libintl.9`, then move onto the [symbolic link portion of this article](#creating-symbolic-link-to-fake-having-libintl9). If it outputs "No such file or directory", then we will need to install it.
```console
username@Mac:~$ cd /usr/local/lib
username@Mac:/usr/local/lib$ ls libintl*
ls: libintl*: No such file or directory
```
<my-caption>Example of not having libintl installed</my-caption>


## Installing `libintl`
Installing `libintl.8` can be done by installing **brew** and making sure it is **update**d and **upgrade**d. You can check if you have brew by running `brew` in your terminal. If you get a "command not found", then you'll need to install brew from [https://brew.sh/](https://brew.sh/). If you have brew, it will give some example usage when you try to run it:
```console
username@Mac:~$ brew
Example usage:
  brew search [TEXT|/REGEX/]
  brew info [FORMULA...]
  brew install FORMULA...
  brew update
  brew upgrade [FORMULA...]
  brew uninstall FORMULA...
  brew list [FORMULA...]

Troubleshooting:
  brew config
  brew doctor
  brew install --verbose --debug FORMULA

Contributing:
  brew create [URL [--no-fetch]]
  brew edit [FORMULA...]

Further help:
  brew commands
  brew help [COMMAND]
  man brew
  https://docs.brew.sh
```
<my-caption>Verifying brew is successfully installed</my-caption>


Now that brew is installed, we'll need to make sure it is up to date. You can update everything by running `brew update` and `brew upgrade` in no particular order. Sometimes they will output instructions to run other commands, follow the instructions. At the end of the day, once brew tells you everything is up to date after running both `brew upgrade` and `brew update`, you know you are done.
```console
username@Mac:~$ brew update
Already up-to-date.
username@Mac:~$ brew upgrade
username@Mac:~$
```
<my-caption>A fully updated and upgraded brew</my-caption>


Below are the commands that I ran in order to get brew fully updated and upgraded. Note that these commands will take some time (~10 mins each).
```console
username@Mac:~$ brew update
[...]
username@Mac:~$ brew update
Error:
  homebrew-core is a shallow clone.
To `brew update`, first run:
  git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
[...]
username@Mac:~$ git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
[...]
username@Mac:~$ brew update
[...]
username@Mac:~$ brew upgrade
[...]
```
<my-caption>My experience updating brew</my-caption>


## Creating a symbolic link to "fake" having `libintl.9`
We should now have `libintl.8` installed:
```console
username@Mac:~$ cd /usr/local/lib
username@Mac:/usr/local/lib$ ls libintl*
libintl.8.dylib libintl.a     libintl.dylib
```

The Resynthesizer plugin is looking for `libintl.9.dylib`. We can "cheat" and tell it to use `libintl.8.dylib` via `ln -s libintl.8.dylib libintl.9.dylib`:
```console
username@Mac:~$ cd /usr/local/lib
username@Mac:/usr/local/lib$ ln -s libintl.8.dylib libintl.9.dylib
username@Mac:/usr/local/lib$ ls -lah libintl*
lrwxr-xr-x  1 username  admin    42B Jan  3 21:09 libintl.8.dylib -> ../Cellar/gettext/0.21/lib/libintl.8.dylib
lrwxr-xr-x  1 username  admin    15B Mar 13 18:40 libintl.9.dylib -> libintl.8.dylib
lrwxr-xr-x  1 username  admin    36B Jan  3 21:09 libintl.a -> ../Cellar/gettext/0.21/lib/libintl.a
lrwxr-xr-x  1 username  admin    40B Jan  3 21:09 libintl.dylib -> ../Cellar/gettext/0.21/lib/libintl.dylib
```

As we can see, `libintl.9.dylib` now points to `libintl.8.dylib`, similar to a "shortcut".

# Using the Resynthesizer Plugin
That's it! You should now be able to restart GIMP (quit and open it back up), and once you select an object, then go through the same steps to use the Resynthesizer plugin (Filters --> Enhance --> "Heal selection..." --> OK), it should now synthesize successfully! 🤞

![Example of a successful use of the Resynthesizer plugin](/assets/img/posts/2021-04-05-how-to-install-the-resynthesizer-plugin-for-gimp-on-mac-2021/before-and-after-resynthesizer-plugin-GIMP.png){: width="480"} *Example of a successful use of the Resynthesizer plugin!*

Pretty nice for an automatic tool!

# Bonus: Alternative to the Resynthesizer Plugin
If the above seemed like too much, we can get similar results to the Resynthesizer tool manually by using the *heal* and *clone* tools that GIMP provides. I'm not going to do a full writeup about it here, but I did go into a quick example in the [YouTube video above](https://youtu.be/MHwtKg0tws8?t=802). I'm sure you could find some similar or even better tutorials on those tools online.


That's a wrap! Thanks again to [Werner Eugster](http://homepage.agrl.ethz.ch/eugsterw/).

If you have any questions or suggestions, feel free to comment in Disqus below.

Catch you in the next one!

&nbsp;

<div style="text-align:center">
<iframe
src="https://open.spotify.com/embed/track/4MAJ62sRxctluSpGf76HA5"
width="300" height="380" frameborder="0"
allowtransparency="true"
allow="encrypted-media">
</iframe>
</div>

