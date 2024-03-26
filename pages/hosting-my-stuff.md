title: How I host all of my stuff as a programmer
date: 2024-03-26
description: Hosting is something I have put a lot of time, effort and money into. (I still wouldn't say im an "expert" in this subject) but I have had a lot of experience in it. In this post I talk about why its important and my recommendations 
slug: hosting-my-stuff

If your a programmer, developer or just a self hoster you probably know how hard it is to decide how your going to host all of your stuff, its an annoying subject because there are just so many options to choose from, and once your already using one its really annoying to switch off it easily.

## Why its important
Every single thing on the internet needs to be hosted by some sort of server. Thats all the internet is, just millions of computers and servers interconnected. If your running your own apps on the internet, either programming them or just using open-source apps and hosting them, you typically need some sort of Linux server. There are thousands of hosting providers to choose from because of how easy it is to start a hosting business these days, so you need to choose wisely.

## Location effects everything
Where you live can change a lot of things, I assume you want your stuff hosted reasonably close to where you live for the best speed when you access it. Different locations can affect the pricing and also the companies available in that region. I was already at a bit of a disadvantage just based on my location

## My Recommendations
I am not an "expert" in this topic, this is what I have just found to be the best for me as a small developer/enthusiast, these have been great price to performance specifically for my use case. I have tested all of these myself as well.
### Specific Locations
- Australia / Asia Pacific (Any part: Sydney, Melbourne, Adelaide, Perth, Singapore) I reccomend BinaryLane, they have competitve pricing, some of the most flexible plans I have ever seen and they are based in Australia as well

- Germany: Datalix, they have really cheap plans with fast discord based support and web support. Since they are a small company they also have tons of really good deals happen every once in a while

- North America: Sparked Host, they are cheap, reliable and are just a cool company in general, they have a massive discord server with ticket based support on their website. You have both vps / dedicated server hosting, web hosting and game hosting

### Free Hosting

- Oracle Cloud: Good for what it is, would definitely recommend making backups of your servers located somewhere not on oracle as have not have a good experience with them when it comes to account termination

- Google Cloud Free Tier: Very limiting as it is only 1gb of ram and 2vcpus but for my use case which is just a monitoring server it works great.

## My Software Stack
These are what I use to push my projects and apps to the public internet, it is definitely not perfect and im still learning.

- Container Software (Docker): I deploy everything in containers as it is very convenient, fast and easy to manage, I also use docker compose so I can deploy stuff within 2 minutes.

- Web Proxy (Nginx): Software that I use to secure my web servers with ssl and also deploy them on my domains, it also lets me run multiple services from the same ip address so I don't need a seperate server for every application.

- Linux Distro (Ubuntu 22.04 LTS): Chose this linux distro as I am very familiar with it and it just does everything I need to do, im familiar with security on here and I have deployed it many times on my own hardware and in the cloud 

I hope your learnt something and have a good rest of your day/night.