from functools import reduce

indata = input().replace("0", "")
indata = [int(n) for n in indata]

while(len(indata)>1):
    indata = str(reduce((lambda x, y: x * y), indata))
    indata = indata.replace("0", "")
    indata = [int(n) for n in indata]

print(indata[0])
