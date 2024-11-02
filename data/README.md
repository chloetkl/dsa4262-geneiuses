# Test Data Generation Steps
1. We found the number of lines in dataset0 using `wc -l dataset0.json` and file size using `ls -lh dataset0.json`. This file is 597mb and has 121838 lines. Therefore, we will take 0.1% of its lines to reduce it below 100mb.
2.  We will take 1 line out of every 1000 lines. Final file details: 60MB, 12183 lines
```
$ sed -n '0~10p' dataset0.json > test_data.json
$ ls -lh test_data.json
-rw-rw-r-- 1 ubuntu ubuntu 553K Nov  2 08:13 test_data.json
$ wc -l test_data.json
121 test_data.json
```
