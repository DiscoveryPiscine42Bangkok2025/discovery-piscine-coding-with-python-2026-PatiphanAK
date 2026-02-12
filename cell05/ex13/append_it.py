#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    found = False
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")
            found = True

# ?> ./append_it.py | cat -e
# none$
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$
# ?>
