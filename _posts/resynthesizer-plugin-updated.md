Ok, this is an updated and **much easier** tutorial compared to my last attempt.


TLDR:
1. Download and install GIMP
2. Download and extract the Resynthesizer plugin
3. Try to run it
4. If it fails, create a symbolic link
   * `cd /Applications/GIMP-2.10.app/Contents/Resources/lib`
   * `ln -s libintl.8.dylib libintl.9.dylib`
5. Restart GIMP!


