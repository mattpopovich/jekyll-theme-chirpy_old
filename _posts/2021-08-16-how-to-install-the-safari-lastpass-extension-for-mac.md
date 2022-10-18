---
# See defaults in _config.yml
title: "How to Install the Safari LastPass Extension for Mac"
author: Matt Popovich
date: 2021-08-16 22:30:33 -0600
categories: [Blog] # <=2 values here: top category and sub category
tags: [apple, big sur, osx, mac, how to, tech, tutorial, not youtube]       # TAG names should always be lowercase
layout: post
pin: false
---

LastPass extension for Safari not showing? Safari LastPass extension not working? Read on!

## What is LastPass?
[LastPass](https://www.lastpass.com/) is a password manager for nearly all operating systems and browsers. It is a competitor to [1Password](https://1password.com/), [Keeper](https://www.keepersecurity.com/), [ZOHO](https://www.zoho.com/vault/), etc. The idea is nowadays, with many different accounts for banking, social networks, shopping, and more - it's impossible to create and remember secure passwords for all the different sites that we use. Instead, you could remember one long, secure password, which you give to your password manager to then "unlock" all your other passwords. All of your other passwords are completely random, very secure, and stored by your password manager. This prevents you from having to remember multiple passwords - and eventually forgetting your passwords, as well as the [dangerous tactic of password reuse](https://expertinsights.com/insights/5-reasons-you-should-never-reuse-passwords/)!

I highly recommend looking into a password manager!

## Intro
Not to spoil the beans or anything... but I just bought a [2020 M1 Mac Mini](https://support.apple.com/kb/SP823?locale=en_US)! It should greatly enhance my video production capabilities (coming from a [2014 MacBook Pro](https://support.apple.com/kb/SP704?locale=en_US) which did not have H.265 encoding/decoding via hardware acceleration). Excited to see what this M1 chip is capable of and to help give me a better idea if I should get a 2021 16" MacBook Pro with a possible M2 chip in it... possibly being released in September 2021 🤞 ([spoiler alert](https://www.apple.com/newsroom/2021/10/apple-unveils-game-changing-macbook-pro/)!!)

I'm running a fresh install of Big Sur and am trying to install various things. One that got me hung up for a bit is the Lastpass extension for Safari. Here's how you should install it:

## Installation
You can basically follow [these instructions](https://support.logmeininc.com/lastpass/help/how-do-i-install-the-safari-app-extension-on-my-mac-lp010097). Or, in my own words:
* If you already have LastPass installed, uninstall it - especially if you installed it from the Mac App Store:
  * Drag the LastPass app from /Applications to the trash
  * Empty the trash
* Go to the LastPass [downloads page](https://lastpass.com/misc_download2.php)
* Click "Download" next to "LastPass for Safari"
  * I do not know why they offer a different download for "LastPass Mac App". It downloads the same thing as "LastPass for Safari" as of May 15, 2022.
* Follow whatever prompts necessary to open, mount, and install the LastPass app.
* It first installs the LastPass for Mac App. Once you open that up, it will prompt you to then install the LastPass browser extension for Safari.
  * It will also ask you for "full keyboard access"... Which is [not necessary in my opinion](https://support.logmeininc.com/lastpass/help/why-do-i-nbsp-see-a-message-that-lastpassapp-would-like-to-receive-keystrokes-from-any-application-and-should-i-nbsp-allow-it) (weird that they even have a feature that would ask) and I did not enable it.
* This *should* get the extension working for you.
  * If not, I'd recommend the usual:
    * Quit and restart Safari
    * Uninstall and reinstall LastPass
    * Reboot your Mac

## My Issue
My issues was that I attempted to install [Lastpass via the Mac App Store](https://apps.apple.com/us/app/lastpass/id926036361) (it has a 2.6/5 rating for a reason). After installing it, it did not prompt me to install the Safari extension.  Uninstalling it and installing the [direct download from LastPass](https://lastpass.com/misc_download2.php) worked for me.

