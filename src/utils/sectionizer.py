def sectionize(fname):
    lines = open(fname).readlines()
    next_is_header = False
    prev = ""
    new_lines = []
    for i in range(len(lines)-2):
        if lines[i-2].strip().isdigit() and lines[i-1].isspace() and "#" not in lines[i]:
            new_lines += "## " + lines[i]
        elif lines[i].strip().isdigit() and lines[i+1].isspace():
            pass
        else:
            new_lines += lines[i]
    new_lines += lines[len(lines)-2]
    open(fname, "w").writelines(new_lines)

for i in range(24):
    print("%X%X.md" % i //)
