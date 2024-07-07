title: Home server build plans
date: 2024-05-01
description: Everything about my brand new server pc build that is going to mark the beginning of my homelab, It's also my first time building a computer! So thats gonna be fun.
slug: home-server-build

# A quick introduction 👋
After just over a year of being a developer its finally time for a home server so I can gain hands on experience with physical server hardware and setting it up on premises, this will further advance my skillset helping me with getting a job

This will also advance my networking knowledge as I need to find a way to get around my dynamic Ip address, isolate my server from the rest of my network and learn how to safely port forward without putting the rest of my home network at risk of an attack.

The idea for this popped up mid 2023, at the time I was hosting lots of minecraft servers on Oracle Cloud and wanted to deploy my own self-hosted server for more control, improve my experience/skills and just have some fun.


# Hardware we chose 🛠️
The hardware has constantly changed these past few months, as my use case has frequently changed, however I have found these to be the most optimal components/specs for my build. Props to 2 of my friends for helping me find these parts, im not very literate with computer hardware so I really do appreciate knowing people that actually have experience and expertise in the field.

- AMD Ryzen 5 5500 Desktop Processor 6C/12T AM4

We went with a Ryzen processer as they are great bang for the buck, having lots of threads was also a priority since game servers typically use up multiple threads, and I wanted to run multiple game servers.

- Memory: Corsair Vengeance LPX 32GB (2x16GB) DDR4 3200MHz

To make sure this build lasted for a while, we ensured that the ram could be upgraded down the line, opting for a 2 stick kit and going for a 4 slot motherboard, so whenever I need more ram I can just buy a 2nd kit and put them into the extra 2 ram slots.

- Storage/SSD: Kingston - NV2 M.2 PCIe 4.0 NVMe 1TB

Went with this SSD as I needed a high quality drive with a good amount of storage for an affordable price, planning to setup in a RAID soon when I can afford a 2nd one.

- Motherboard: MSI B450M PRO-VDH Max

We made sure to get a high quality motherboard to ensure optimal longevity, we also made sure that it had 4 ram slots (Further explained in the ram section).

- Power Supply: Corsair RM750x

As this thing was gonna run 24/7, I made sure to get a high quality power supply from corsair with quality japanese parts.

- Case: Thermaltake Versa H18

We went for this case because it was cheap, the build quality was good enough, it didn't take up that much space and it perfectly fit our budget.


# Software I plan to run 🎣
The software on this computer is going to range from things like low powered web applications running in docker using less than 1 thread and 1gb of ram, to full on high-performance game servers utilizing multiple threads and multiple gigabytes of ram. This also explains why my hardware is so overkill, I genuinely don't really know exactly what I'm going to run, but below is a general idea of what I'm going to run.

- Game Servers: Minecraft, ARK, Valheim, Terraria 

I'm going to use Pterodactyl control panel to deploy and manage my game servers. Its perfect for the job since it utilizes docker on the backend and is super easy to get started with. I'm likely going to start out with just an Ark server since thats something me and my friends have wanted to start for ages

- Self-hosted applications/web apps

I currently plan to run some simple lightweight applications such as WordPress, Hastebin, Ntfy, Picsur, Uptime Kuma, etc. This will likely use less than 25% of the systems resources, leaving tons of space for game servers

- Base operating system: Ubuntu 24.04

I would go with Debian 12, however Ubuntu is much more user friendly and the performance difference won't be that significant due to the hardware I'm using. I currently don't have any experience with Linux outside of Debian based distros so anything else is not doable for me.


# The build schedule ⌚

Below is the estimated time for when the parts will arrive, I currently have no more information than this except for the fact that its gonna be ready in either May or June.

- Arriving May 14th

Power Supply (Tecnoware ATX 550W)

- Arriving May 16th

Motherboard (MSI B450M), Case (Thermaltake Versa H18), Thermal Paste (Grizzly Kryonaut), Fans (upHere Long Life 120mm)

The rest is being picked up irl using facebook marketplace, or being purchased later