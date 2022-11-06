---
# See defaults in _config.yml
title: "Why the EPA’s EV Efficiency Numbers Don’t Add Up"
author: Matt Popovich
date: 2022-11-06 00:27:19 -0700
categories: [Blog, YouTube] # <=2 values here: top category and sub category
tags: [youtube, tesla, electric vehicles, epa]       # TAG names should always be lowercase
layout: post
pin: false
---

<!-- TODO: Put a bounding box around AOI in images-->

## Intro
Happy belated halloween!

While I was working on a future video, I found something spooky (👻) in the EPA’s (United States Environmental Protection Agency) fuel economy numbers for electric vehicles and I couldn’t quite figure out what was going on. But after further research, I’ve gotten to the bottom of this mystery.

In my future video, I’ll be driving my Tesla Model 3 up Pike’s Peak to see how much battery it uses, but while doing some quick maffs trying to see how my efficiency fared vs what the car is rated for, the EPA’s numbers for efficiency didn’t seem to add up... While I’ll be examining a Tesla Model 3 in this video, as that’s the vehicle that I have, this video will be applicable to any EV (electric vehicle) on the EPA’s [fuel economy website](https://fueleconomy.gov/).

## Double Checking the EPA's Numbers
If you’re buying an EV, two of the more important numbers to look for is how efficient the vehicle is and how much range does the vehicle have. Efficiency for internal combustion engines is given in miles per gallon (or km per liter if you’re across the pond). For EVs it’s similar with miles per kWh (kilowatt hour) or, it can be given as the inverse of that, Wh/mi (watt-hour per mile). I’m not sure which one is more popular but Jason from [Engineering Explained](https://www.youtube.com/@engineeringexplained) has a [good video on why we should use energy per distance](https://youtu.be/oLQmwOX6Xds) so I’ll be using Wh/mi for this video. I imagine they use Wh/km pretty much everywhere that’s not the United States so I’ll add conversions throughout the article for those that don’t use the *good ol’ proprietary American mile™* (🦅).

If you go to the EPA’s website (screenshot below), you’ll see that [it lists](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=45011&id=43401&id=42275&id=41190) a 2020 long range all wheel drive Tesla Model 3 as using 28kWh per 100 miles, or 280Wh/mi (174Wh/km). Also cool to see that Tesla is making their vehicles more and more efficient by requiring less energy to go the same distance with each model year... Except for ’22, not sure what happened there. Additionally, because the vehicles are becoming more efficient, that is giving them more range with each model year as well. However, this isn't the case with the 2022 model year but yet it *still* received a longer range than the previous year. This leads to the next question of are these cars getting more range because of the efficiency, or is Tesla also making the battery larger? Here’s where the rabbit hole begins...

[![Comparisons between different years of Tesla's Model 3 LR AWD on fueleconomy.gov](/assets/img/posts/2022-11-05-why-the-epas-ev-efficiency-numbers-dont-add-up/TeslaModel3-LR-AWD_fueleconomy.gov.png)](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=45011&id=43401&id=42275&id=41190)*Comparisons between different years of Tesla's Model 3 Long Range All-Wheel Drive*

For the 2020 model year, 28kWh/100mi * 322mi of range = 174kWh/100km * 518km = ~90kWh battery. And that actually makes sense if you compare it to other EVs. The [Mustang Mach E has 88kWh](https://ev-database.org/imp/car/1243/Ford-Mustang-Mach-E-ER-RWD), [Audi's e-tron GT quattro has 85kWh](https://ev-database.org/imp/car/1420/Audi-e-tron-GT-quattro), [Porsche Taycan Turbo at ~84kWh](https://ev-database.org/car/1229/Porsche-Taycan-Turbo) (all "usable" capacities, more on that later...).
So let’s double check how big the battery is to confirm these numbers make sense and we’ll be on our way. Spoiler alert, it’s not 90kWh.

## Gross Battery Capacity vs Usable Battery Capacity
The EPA publishes the documentation sent in by the automakers for a “certificate of conformity”. Basically it’s a document where the automaker says “Hey, here’s some numbers on our engine, it meets EPA requirements”. This [document for the 2020 Model 3 LR AWD](https://iaspub.epa.gov/otaqpub/display_file.jsp?docid=48712&flag=1#page=020) says the battery has a weight of 480kg and it has a density of 150Wh/kg. This amounts to a 480kg * 150Wh/kg = 72kWh battery, although most other websites that I’ve looked at give closer to 75kWh: [75kWh](https://en.wikipedia.org/wiki/Tesla_Model_3#Specifications_table) [75kWh](https://www.evspecifications.com/en/model/0a86df) [73.5kWh](https://ev-database.org/car/1138/Tesla-Model-3-Long-Range-Dual-Motor) [75kWh](https://www.guideautoweb.com/en/makes/tesla/model-3/2020/specifications/long-range-awd/).

I haven’t quite nailed down why there is this discrepancy between Tesla’s documentation and what most other websites give. I want to chalk it up to “manufacturing tolerances and differences” but I haven’t been able to confirm that. Regardless, just when I thought I had the battery capacity figured out, I stumble upon a site that listed both capacity and “usable capacity”... Yep, this rabbit hole goes deeper. <!-- (https://teslamotorsclub.com/tmc/posts/5576513/) -->
The site was evspecifications.com, and they list a “usable capacity” around 75kWh with a total capacity of 79.5kWh (screenshot below). What’s the difference?

[![Tesla Model 3 Long Range All-Wheel Drive Battery Capacity](/assets/img/posts/2022-11-05-why-the-epas-ev-efficiency-numbers-dont-add-up/TeslaModel3-LR-AWD_batteryCapacity.png)](
https://www.evspecifications.com/en/comparison/7cbc182a) *Tesla Model 3 Long Range All-Wheel Drive Total Battery Capacity vs Usable Capacity*

From what I can find, the “usable capacity” is how much energy you can use taking your battery from 100% down to 0%. That *usable capacity* is 75kWh. Now, you might be thinking, “Matt, what more is there between 100% and 0%”. I’ll refer you to the idiom of ["giving 110 percent"](https://en.wiktionary.org/wiki/give_110%25). For Teslas, they can actually give 104.5%. Tesla has built in a small buffer of ~4.5% that **should not be depended on** <small><small>but may be available</small></small> after your car hits 0%. So really when a Tesla hits 0%, it’s kinda actually at 4.5%. And when Tesla did its range tests, it takes the car from 100%, past 0%, and to the point where the car [says no más](https://en.wikipedia.org/wiki/Roberto_Dur%C3%A1n_vs._Sugar_Ray_Leonard_II) (“no more”) and can’t move any further.

If we look deeper into the the documentation Tesla submitted, we will see that they managed to get ~79.8kWh out of the fully charged battery. And when Tesla gives you the “total range of the car”, this is the value that they are using for the amount of energy stored in the battery. So we’re now up to a ~80kWh battery, but the numbers from the EPA that we calculated earlier gave us a battery size of ~90kWh. So how did they get that?

## Charging Losses
After taking the car the whole way down to 0% (or should I say -4.5%...), once the battery was fully dead, they tracked how much energy they needed to bring the car back up to 100%. That amount of energy was ~89.9kWh. You can see the slightly different numbers for each of the Long Range (LR) Model 3’s [here](https://iaspub.epa.gov/otaqpub/display_file.jsp?docid=48712&flag=1#page=019), they’re all close to 90kWh of recharge energy.
￼
So, now the question is, how did they manage to put ~90kWh into a car with a 79.5kWh battery pack? That answer is “charging losses”. The battery pack stores direct current (DC) energy, but the grid provides alternating current (AC) energy. There are some losses with converting AC to DC, and those losses are about 11.5%. In other words, the conversion is ~88.5% efficient

[![Detailed results from EPA's EV Multicycle Tests for 2020 Tesla Model 3 LR AWD](/assets/img/posts/2022-11-05-why-the-epas-ev-efficiency-numbers-dont-add-up/2020TeslaModel3LRAWD-MulticycleCalculator.png)](https://iaspub.epa.gov/otaqpub/display_file.jsp?docid=48712&flag=1#page=028)*Detailed results from EPA's EV Multicycle Tests for 2020 Tesla Model 3 LR AWD*

## Summary
All right... That was a lot, so let’s recap. The numbers that the EPA shows for efficiency can be thought of as [“wall - to - wheel” efficiency](https://teslamotorsclub.com/tmc/posts/5578886/), which means they take into account charging losses from converting AC at the wall to DC in the battery pack. I guess this is fair because you could say they do a similar thing for internal combustion vehicles, it’s just that hopefully there shouldn’t be any leaks from the gas pump to your car!
The conversion from AC to DC is about 88.5% efficient using a 240V level 2 charger ([less efficient with a 120V level 1 charger](https://ieeexplore.ieee.org/document/7046253) due to less voltage and ohm’s law among other factors), so the 280Wh/mi (174Wh/km) from the wall that the EPA shows is equivalent to 280*88.5% = 247.8Wh/mi (154Wh/km) once the energy is in the battery pack. This is the number that your car will display, and my lifetime efficiency number is...  **exactly** that!

![My 2020 Tesla Model 3 LR AWD's Lifetime Efficiency](/assets/img/posts/2022-11-05-why-the-epas-ev-efficiency-numbers-dont-add-up/MattPopovich_2020TeslaModel3-LR-AWD_LifetimeEfficiency.jpg) *My 2020 Tesla Model 3 LR AWD's Lifetime Efficiency*

Lastly, given the car’s usable battery of 75kWh, the car should have a range of 75kWh / 0.2478kWh/mi = 302.7mi (487.1km). However, Tesla doesn’t tell you about a 4.5% buffer that *may be available* after the car hits 0% battery. This takes the gross battery size up to 75 * 1.045 = ~78.4kWh, giving us a total range (in emergencies) to ~316mi (~509km)... close enough to the 322mi (518.2km) number advertised.

## The Next Exercise for the Reader
So that is where the numbers on the EPA’s fuel economy come from. There’s a whole other discussion to be had on how the EPA obtains that 280Wh/mi (174Wh/km) number. Yes, it includes charging losses, but it also includes a highway test, a city test, a high speed test, and an air conditioning test. [Here's a video]((https://www.youtube.com/watch?v=b6Oel4klhjI)) that goes over this in a bit more detail. Not all of the tests that I just mentioned are mandatory and manufacturers are allowed to decrease the total range number given by the EPA for whatever reason they want. [Porsche does this](https://electrek.co/2020/04/24/porsche-voluntarily-lowered-taycans-official-range-numbers-from-200-to-192-miles/) I speculate to give what they think is a better real world number. [Tesla used to do it](https://electrek.co/2018/07/24/tesla-model3-epa-ratings-advertise/) because their AWD variants were less efficient than their RWD models. So to not make them not look like a worse car in comparison, they handicapped the RWD models so that the range differences weren’t as drastic, especially for the AWD Performance model which was the least efficient. This was back when the Model 3 Dual Motor was first coming out. They have since stopped that practice and now let the EPA's numbers more closely reflect the differences. If you think this would be an interesting topic for me to go into further detail, let me know in the comments below and I'll consider it for my next post!

## Outro
Thank you if you made it this far, I hope you were able to follow along and that you can now understand where the EPA’s numbers are coming from. If anything isn’t clear, please let me know in the comments.

I guess the moral of the story is... *your mileage may vary*.

😅
