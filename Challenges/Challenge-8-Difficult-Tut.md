1. awesomeyoufoundme.png <- congratulations.gzip
= zip [newname] awesomeyoufoundme.png
= zip congratulations.gzip awesomeyoufoundme.png

2. congratulations.gzip <- howdidyoufindme.zip
= bzip2 -c congratulations.gzip > howdidyoufindme.zip

3. howdidyoufindme.zip <- doyoureallytrustme.pdf
= 7z a doyoureallytrustme.pdf howdidyoufindme.zip
