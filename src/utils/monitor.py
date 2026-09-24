import sys, os, time, webbrowser

fname = input("file name (without ending)?\n>>> ")

last = os.stat(fname + ".md").st_mtime

os.system("firefox " + "../" + fname + ".rjs.html")
os.system("firefox https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/311-sp26.html")

print("Monitoring " + fname + ".md...")

os.system("quarto render " + fname + ".md")

while True:
    time.sleep(1)
    curr = os.stat(fname + ".md").st_mtime
    if curr != last:
        os.system("quarto render " + fname + ".md")
        last = curr
        print(last)
