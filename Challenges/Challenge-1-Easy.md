Welcome to my documentation on how I will try to write these CTF challenges.

This is so exciting! I can't believe I'm about to write my own CTFs.

This was meant for beginners in my school, so almost everything in this CTF is intentionally very easy.

Not only as a way to encourage others to dive deeper into cybersecurity, but also as a result of the limitations of my current capabilities and skills in creating CTF challenges.

Let's begin.



CTF Name: eduCTF 

Challenge Name: PLACEHOLDERPLACEHOLDERPLACEHOLDERPLACEHOLDER

Category: Forensics (Steganography)

Difficulty: Easy

Challenge Description: "PLACEHOLDERPLACEHOLDERPLACEHOLDER"

Hints: PLACEHOLDERPLACEHOLDERPLACEHOLDERPLACEHOLDER

TOOLS USED TO WRITE CHALLENGE:

    mkdir

    mv

    cd
    
    exiftool

CHALLENGE CREATION PROCESS:

Create a directory to organize files meant only for this CTF.

    ┌──(hellopo㉿rald)-[~]
    └─$ mkdir eduCTF2026/

Create more directories to further organize it per challenge.

    ┌──(hellopo㉿rald)-[~/eduCTF2026]
    └─$ mkdir Challenge1Easy/

Next, download a sample placeholder image to experiment on.

For this, I'll take a random image of my good friend X(Of course, not his real name)

I just took it from his Facebook and Downloaded it through my web browser.

Now, I have X.jpg. It's currently in my default dir, so let's move it into the dir we want it to be in.

    ┌──(hellopo㉿rald)-[~]
    └─$ mv X.jpg eduCTF2026/Challenge1Easy/

Move to Challenge1Easy, and begin to edit the metadata of the image using exiftool.

    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge1Easy]
    └─$ exiftool -Artist="eduCTF{TEST}" X.jpg 


The -Artist flag just edits the field used to determine the image's creator.

In this case, we'll edit this field to hide the information we want.

Using the -Comment flag was my first thought, but after using the file cmd on the image, it actually displays the flag on it.

Editing the -Artist flag doesn't do that. So this is what we're going with.

Now let's test how it looks as a competitor trying to solve it:

    ┌──(hellopo㉿rald)-[~/eduCTF2026/Challenge1Easy]
    └─$ exiftool marck.jpg                     
    ExifTool Version Number         : 13.50
    File Name                       : X.jpg
    Directory                       : .
    File Size                       : 400 kB
    File Modification Date/Time     : 2026:04:15 11:07:28-04:00
    File Access Date/Time           : 2026:04:15 11:08:41-04:00
    File Inode Change Date/Time     : 2026:04:15 11:07:28-04:00
    File Permissions                : -rw-rw-r--
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    JFIF Version                    : 1.01
    Exif Byte Order                 : Big-endian (Motorola, MM)
    X Resolution                    : 1
    Y Resolution                    : 1
    Resolution Unit                 : None
    Artist                          : eduCTF{TEST}

Great! This will be enough for the first challenge. 

My goal here is to give my competitors that fuzzy feeling in their stomach when feeling like they're smart after finding the flag. 

So ultimately, I don't want the easy problems to get that complicated.

Nice. 
