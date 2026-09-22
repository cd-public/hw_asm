from os import system

cmd = "curl https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/slides/lecture%02d.pdf -o %s.pdf 2>/dev/null && markitdown %s.pdf -o %s.md && rm %s.pdf"

for i in range(26):
    j = "%X%X" % ((i-1) // 2, (i-1) % 2)
    system(cmd % (i, j, j, j, j))
