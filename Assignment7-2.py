# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
total=0
count=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        val=float(line[20:])
        count=count+1
        total=total+val
print("Average spam confidence:", total/count)