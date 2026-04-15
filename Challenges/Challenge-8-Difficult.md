CTF Name: eduCTF

Challenge Name: PLACEHOLDERPLACEHOLDERPLACEHOLDERPLACEHOLDER

Category: Forensics (Steganography), Cryptography

Difficulty: Easy

Challenge Description: "PLACEHOLDERPLACEHOLDERPLACEHOLDER"

Hints: You modify something to change it, so how did the suspect change something about this image?

TOOLS USED TO WRITE CHALLENGE:

    mkdir
    
    mv
    
    exiftool
    
    cd
    
    bash scripting
    
    ls
    
    cat
    
GENERAL IDEA:

The idea comes from the Russian Nested Dolls. You think there's only 1 doll, turns out there's like 5 smaller ones nested inside.

Using this concept, we will create a single image containing the flag, but it is compressed so many times in many different ways that it may disorient a beginner.

Additionally, the file extensions will provide even more confusion because it'll all be a distraction. 

The file extensions will be intentionally set incorrectly so as to confuse the player.

They'll have to use the "file" cmd to double check the true file extension for every time they decompress it.

So it'll be a lot of mental gymnastics for them lol.

And then by the time it's time to open the image, they'll have to know the xdg-open tool or else how the heck do you open it.

(Draft:) 
(And worst of all, the image they get is STILL encrypted. It'll have the hex version of the flag, which they'll have to decrypt.)

This takes huge inspiration from OverTheWire Wargames: Bandit. Big thanks to them. If any players have been doing their homework, they should be rewarded with the knowledge of knowing how to solve this problem. Otherwise, it might just be hell.

Let's begin.

CHALLENGE WRITING PROCESS:

Let's first decide on an flag. Let's go with eduCTF{th4t_t00k_f0r3v3r_6767}

Now let's create the image we need on figma. 

<img width="1440" height="1024" alt="Challenge-8-Flag" src="https://github.com/user-attachments/assets/b3136885-4ff7-4fdc-b64b-1ded6a657fdf" />

Perfect. Now I'll just upload this image on GDrive, set it to public viewer, and install it from my Kali VM to work with it.

I've also moved the image 
