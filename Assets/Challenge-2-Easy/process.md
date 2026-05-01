┌──(unixhellopo㉿AL15-41P)-[/mnt/c/Users/Gerald/OneDrive/Documents/eduCTF 2026/Challenge 2 Easy]
└─$ head -c 5000000 /dev/urandom > memory_leak.bin

┌──(unixhellopo㉿AL15-41P)-[/mnt/c/Users/Gerald/OneDrive/Documents/eduCTF 2026/Challenge 2 Easy]
└─$ echo "DEBUGLOG_2026: eduCTF{d1d_y0u_us3_str1ngs_Er1ch?_5432}" > flag.txt
dd if=flag.txt of=memory_leak.bin bs=1 seek=2500000 conv=notrunc
55+0 records in
55+0 records out
55 bytes copied, 0.0487758 s, 1.1 kB/s

┌──(unixhellopo㉿AL15-41P)-[/mnt/c/Users/Gerald/OneDrive/Documents/eduCTF 2026/Challenge 2 Easy]
└─$ rm flag.txt
