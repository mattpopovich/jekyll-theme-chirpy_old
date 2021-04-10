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

<div style="text-align:center">
<iframe width="560" height="315" 
src="https://www.youtube.com/embed/MHwtKg0tws8"
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
</div>

**Good Afternoon!**

## Intro
This article goes over how to install the Resynthesizer plugin for GIMP on Mac. It likely will not work when you immediately install it, but there's a pretty simple solution. I spent *waaaay* too much time one Sunday trying fix this, from building GIMP from source, then trying to rebuild this plugin, etc... thankfully none of that is necessary. There's a very easy solution that [Werner Eugster](http://homepage.agrl.ethz.ch/eugsterw/) found and below I'll elaborate on how to successfully use his solution to run the Resynthesizer plugin to automatically remove an object from an image. Let's go!

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Download and install [GIMP](https://www.gimp.org/downloads/)
2. Download the Resynthesizer plugin for Mac: [ResynthesizerPlugin-Gimp-2.10-osx.tgz
](https://github.com/aferrero2707/gimp-plugins-collection/releases/download/continuous/ResynthesizerPlugin-Gimp-2.10-osx.tgz)
3. Extract the plugin and copy its contents to `/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins`
4. Try to run it on an image (Filters --> Enhance --> "Heal selection..."). 
  * If it works, you're good to go! If not, continue to step 5
5. 



## Install GIMP
For starters, we need to download and install GIMP. You can download it from [here](https://www.gimp.org/downloads/). If you're on Mac, you can open (mount) that downloaded file and click and drag GIMP to the Applications folder. If you're on another OS, follow the instructions given to you. 

## Install Resynthesizer Plugin
We can download the Resynthesizer plugin from aferrero2707's repo on GitHub: [gimp-plugin-collections](https://github.com/aferrero2707/gimp-plugins-collection). If you navigate to the releases and then to continuous build, you can scroll down and see all the plugins available. We want to download [ResynthesizerPlugin-Gimp-2.10-osx.tgz
](https://github.com/aferrero2707/gimp-plugins-collection/releases/download/continuous/ResynthesizerPlugin-Gimp-2.10-osx.tgz). Once downloaded, you can extract it and open up the resulting folder to see a bunch of Python files. We need to copy them to GIMP's plugin folder. To find GIMP's plugin folder, you can open GIMP, then go to GIMP-2.10 (in the menu bar) --> Preferences --> scroll down on the left column to Folders, click on Folders to expand it --> Plug-ins. You will likely see two different options for placing these plugin files: 
```
/Users/<username>/Libary/Application Support/GIMP/2.10/plug-ins
/Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins
```
You can copy to either one, but `/Applications` is easier (you need to create the folder for `/Users`). You can click on the `/Applications/...` path in the window to select it, then you can open that path by clicking on the office cabinet-looking icon on the top right which will show the tooltip "Show file location in the file manager". Once that is open, we can select and drag all of the python files over to that window, restart GIMP (Command (⌘) + Q or GIMP-2.10 --> Quit GIMP-2.10), and the Resynthesizer plugin should appear as an option under Filters --> Enhance --> "Heal selection..."! 

## Testing the Resynthesizer plugin (Heal selection)
Now that we have installed the Resynthesizer plugin, we can give it a quick test to see if it will work (likely not). Let's start by importing an image into GIMP (click and drag an image into GIMP, then click convert to change the color profile to what GIMP prefers). Next, we can select an area that contains an object we want to remove (by selecting the "Free Select" tool [press "f"] and clicking around the outside of our object or by selecting the "Rectangle Select" tool [press "r"] and making a rectangle around our object (less precise)). Finally, we can try to run the Resynthesizer plugin: Filters --> Enhance --> "Heal selection...". Your mileage may vary but I was presented with the following errors: 

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







<div style="text-align:center">
<iframe
src="https://open.spotify.com/embed/track/4MAJ62sRxctluSpGf76HA5" 
width="300" height="380" frameborder="0" 
allowtransparency="true" 
allow="encrypted-media">
</iframe>
</div>

