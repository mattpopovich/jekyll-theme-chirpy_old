---
title: "How to Diagnose and Fix Low Coolant Warning for Audi (A3 8V) / VW"
author: matt_popovich         # Reference author_id in _data/authors.yml
date: 2022-03-20 17:00:48 -0700
categories: [Blog, YouTube]   # <=2 values here: top category and sub category
tags: [youtube, audi, audi a3 8v, how to, tutorial]       # TAG names should always be lowercase
layout: post
pin: false
---

<div style="text-align:center">
<iframe width="560" height="315"
src="https://www.youtube.com/embed/rRbSVmFteuY"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>
</div>


Hey guys! Matt Popovich here. Today in my [series of Audi A3 tutorials](/tags/audi/), I’m going to explain what it means to have a “low coolant” warning and how to fix it from the prospective of a 2015 Audi A3 8V. When you first start your car, beeps and chimes will start going off like your car is very unhappy with you, but don’t freak out as it’s not the end of the world yet... although it *could* be if you don’t keep an eye on things.
## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Check the engine temperature gauge
  - If it stays in the middle, you are fine to keep driving.
  - If it goes above the middle, you will want to pull over, shut the engine off, and add coolant (if low).
2. Check coolant reservoir level
  - The coolant reservoir is on the passenger side of the engine bay.
  - When the car is cold, coolant should be between the maximum and minimum line. When the engine is warm, the coolant can rise to be slightly above the maximum marking.
3. Add coolant
  - Use G13 coolant as stated on the reservoir. Cut coolant concentrate 50/50 with distilled water.
    - The manual states that you can also use G12++, but I will follow what is printed on my reservoir.
4. Done
  - You do not have to reset anything in the car for the low coolant warning to go away. Once you drive it again, the sensor should read the coolant levels and the coolant light should turn off.

## First steps: can you keep driving?

![Audi A3 8V Dash Engine Temperature Gauge](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/engine-temperature-gauge.jpg){: width="600"} *Location of Engine Temperature Gauge (Highlighted)*

The first thing you’re going to want to do is to keep an eye on your engine temperature gauge (the location for a S3/RS3 is different, watch [this video](https://www.youtube.com/watch?v=jSTC5FCfJdA) for how to find it, and watch [this video](https://www.youtube.com/watch?v=--jgt7jy-xo) for how to modify the car’s settings via [OBD2](https://en.wikipedia.org/wiki/On-board_diagnostics) to add engine oil temperature to the instrument cluster). Coolant has two functions: it keeps the engine from overheating and it protects the engine from freezing in the winter. I just started my car after it was sitting for a ~day so the engine is cold. After a few minutes, the engine temperature will creep back up to the normal level, which is where it should be while you are driving. It’s "okay" to keep driving with the low coolant light on as long as your engine stays at normal operating temperature. You’ll need to keep an eye on it. Ideally, you’ll want to check the physical, liquid coolant level as soon as you can for some additional peace of mind. If the car doesn’t get to normal operating temperature or if it goes past the midpoint line, that’s a bad sign and you should pull over, open the hood and check the coolant level in the coolant reservoir. Let me show you how to do that now.

## Checking the coolant level
First, open the driver door so that we can pull the lever to pop the hood. We will want to park on a level surface so that the coolant in the reservoir isn’t tilting to any side. Next, we’ll go around to the front of the car and feel under the hood, above the Audi symbol for a button or latch to release the hood. From here, we can find our coolant reservoir which will be on the passenger side of the engine.

![Audi A3 8V Coolant Reservoir](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/coolant-reservoir.jpg){: width="400" .right}

As we can see, my coolant is below the minimum line, so we’ll need to add some more. When the car is cold, coolant should be between the maximum and minimum line. When the engine is warm, the coolant can rise to be slightly above the maximum marking. As it is right now, it’s “okay” for me to drive with the coolant level below the minimum line, as I do have coolant in the reservoir, but I need to keep an eye on the engine temperature gauge while I’m driving.

## Which coolant to use?

![Audi A3 8V Coolant Reservoir G13 Symbol](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/coolant-reservoir-g13.jpg){: width="100" .left}

For coolant, I need to use G13 coolant as stated on the reservoir.

The manual states that you can also use G12++, but I will follow what is printed on my reservoir. While you can technically mix the two, it’s not ideal. If you want to switch from G12++ to G13 or vice versa, you should flush all of the old coolant out first ("[When changing fluid types to a newer fluid, you must flush the old coolant out](https://www.fcpeuro.com/products/pp-coolant-antifreeze-g012a8gm1-1-5l#description)").

G12++ and G13 will be pinkish / purple in color. Do not mix it with any blue, green, orange, yellow, or any other colored coolants as they are not compatible.
Coolant can be bought as either concentrate (100% strength concentrate) or as diluted or mixed (50/50 concentrate and distilled water). If you buy concentrate, you will need to cut the strength yourself with distilled water. Do not use tap water, do not use bottled water. **Use distilled water**.

![Owner's Manual Note on Adding Coolant](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/owners-manual_adding-coolant.png){: width="350" .right}

> Side note: If you’ve ever heard the term “antifreeze”, that technically refers to concentrate whereas “coolant” technically refers to the 50/50 mixture of concentrate with distilled water. They’re sometimes used interchangeably but while doing some research, I learned that they are [technically different](https://www.cars.com/articles/what-is-coolant-and-is-it-the-same-as-antifreeze-436143/).

I will be using OEM coolant, which is the coolant that the **o**riginal **e**quipment **m**anufacturer (aka Audi) uses. You’re probably fine using off brand G13 substitutes but I personally think coolant is cheap enough that I won’t be using an off brand (prices and links below). The OEM coolant is [Pentosin Pentofrost E](https://crpautomotive.com/wp-content/uploads/2020/06/Pentosin-Product-Data-Sheet-Antifreeze-Pentofrost-E.pdf):

You can get distilled water from anywhere, most grocery stores carry it (and I have links below).

When you mix it, you don’t have to go full Bill Nye with it to make sure it’s a perfect 50/50 ratio. The manual states that the concentrate should be at least 50% but less than 60% of the solution. If you’re in a place with extremely cold climates, it wouldn’t hurt to be closer to 60% concentrate. I’m going to go half Bill-Nye and eyeball my solution.

![Pentosin Pentofrost E 1.5L Container](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/pentosin-pentofrost-e.jpg){: width="300" .right}

* OEM Uses Pentosin Pentofrost E
    * 1.5L Part Number: 8113106
      * [1.5L concentrate](https://www.fcpeuro.com/products/pp-coolant-antifreeze-g012a8gm1-1-5l) (~$15 + shipping from FCP Euro)
      * [1.5L concentrate](https://shop.advanceautoparts.com/p/pentosin-pentofrost-e-g13-hoat-silicate-european-concentrate-antifreeze-coolant-1.5-liters-8113106-8112106/10007846-P) (~$20 from Advance Auto Parts)
    * 5L Part Number: 8113206
      * [5L concentrate](https://www.fcpeuro.com/products/copy-of-pp-coolant-antifreeze-g012a8gm1-1-5l) (~$40 + shipping from FCP Euro)
      * [5L concentrate](https://shop.advanceautoparts.com/p/pentosin-pentofrost-e-g13-hoat-silicate-european-concentrate-antifreeze-coolant-5-liters-8113206-8112206/10024262-P) (~$60 from Advance Auto Parts)

Distilled water can be bought from anywhere such as grocery stores.

* [128oz from Amazon ~$2 (affiliate link)](https://amzn.to/3RnV4E5)

## Adding coolant

Now that we’ve made our coolant, we need to add it to the reservoir. Before you open the reservoir, make sure you let the engine cool down. Do not open the reservoir when the engine is hot as coolant will typically be around 200°F (93°C). So to prevent burns, let the engine cool down beforehand. If you can’t or don’t have time, use a large, thick cloth to open the reservoir to protect you from escaping coolant and steam. Be careful not to get drips anywhere as ethylene glycol (AKA coolant) hitting a hot engine can catch fire under certain circumstances.


![Hot Coolant Warning from Owner's Manual](/assets/img/posts/2022-03-20-how-to-diagnose-and-fix-low-coolant-warning-for-audi-a3-8v--vw/owners-manual_hot-coolant-warning.png){: width="300" .right}

Once open, add your coolant to get you between the min and max lines. Do this slowly, especially if the coolant tank is empty so that you don’t trap any air in the line. I decided to take the anti-bill nye approach and it required multiple refill attempts to get me between the lines... "Our actions have consequences".

## Wrapping up
Now that we’re topped off, make sure you fully tighten the lid and hear a click. We need it to be fully sealed so that none of the distilled water can evaporate and be a source for escaping coolant. Speaking of this, the coolant system is a sealed system. **No coolant should be able to escape**. Thus, if you’re low on coolant, that suggests a problem. If you have to add coolant regularly, you should get that checked out as you probably have a leak somewhere in the system. *Regularly*, as in every couple of weeks. If you need to add coolant once or twice a year, it’s not a *huge* deal as coolant is pretty cheap to add, but again, you shouldn’t have to do that because it is a closed system.

Once we close the lid, we’re free to drive off and keep an eye on the engine temperature gauge, but our work here is done. You do not have to reset anything in the car for the low coolant warning to go away. Once you drive it again, the sensor should read the coolant levels and the coolant light should turn off.

## Outro
That’s a wrap! Hopefully this helped. If there’s anything I missed, feel free to let me know in the comments. I’m working on a whole series of Audi A3 [videos](https://www.youtube.com/playlist?list=PLjsTlizXPX-Ehv0dsmDnp5B3oHIYXBM02) and [posts](/tags/audi), so feel free to check some of those out as well. Thanks for reading! I’ll catch you in the next one.



<div style="text-align:center">
<iframe
src="https://open.spotify.com/embed/track/29XO76OgiJZpD6ySALy1h8?si=7e419ee6027940dd"
width="300" height="380" frameborder="0"
allowtransparency="true"
allow="encrypted-media">
</iframe>
</div>

