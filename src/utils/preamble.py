from os import system

# cmd = "curl https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/slides/lecture%02d.pdf -o %s.pdf 2>/dev/null && markitdown %s.pdf -o %s.md && rm %s.pdf"

cmd = "cat preamble.txt %s%s.md > %s%s.tmp && rm preamble.txt" # && mv %s%s.tmp %s%s.md" 
pre = """---
title: Podman
subtitle: "w%sd%s"
---

# Logistics

## Announcements

- **Welcome** to HW/`asm`
- **Action Items** discussion

# 

"""


for i in range(26):
    w, d = "%X" % (i // 2), "%X" % (i % 2)
    # open("preamble.txt", "w").write(pre % (w, d))
    # system(cmd % (w, d, w, d))
    system("mv %s%s.tmp %s%s.md" % (w, d, w, d))
