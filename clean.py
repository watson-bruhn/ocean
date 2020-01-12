f = open("output","r") #Open file with output from dwave
qdata = f.read()
qlist = qdata.split("Sample(sample={") #Split by each sample into list
qlist = [e.split(", ") for e in qlist] #Split each index

for i in range(1,len(qlist[1])-3):
    qlist[0].append(i)
qlist[0].append("energy")
qlist[0].append("num_occurrences")
qlist[0].append("chain_break_fraction")
(qlist[0])[0] = 0

#del qlist[0] #Remove the first element which isn't a return

for i in range(1,len(qlist)): #Strip out extrenious data
    for j in range(0,len(qlist[1])-4):
        (qlist[i])[j] = ((qlist[i])[j])[-1]
    (qlist[i])[len(qlist[i])-4] = ((qlist[i])[len(qlist[i])-4])[-2]

for i in range(1,len(qlist)):
    for j in range(len(qlist[1])-3,len(qlist[1])):
        (qlist[i])[j] = ((qlist[i])[j])[len((qlist[0])[j])+1:]

g = open("returns","r")
returns = g.read()
returns = returns.split(",")
del returns[len(returns)-1]

cost = [""]

for i in range(1,len(qlist)):
    temp = 0
    for j in range(0,len(returns)):
        temp += float((qlist[i])[j]) * float(returns[j])
    cost.append(temp)

print("\r\n")
print(returns)

print("\r\n")
for i in range(0,len(qlist)):
    print(qlist[i])
    print(" _______________ ")
    print(cost[i])
    print("\r")

quit()

qsize = len(qlist)
qwidth = len(qlist[4])
import numpy as np
outputdata = np.zeros((qsize-1,qwidth-3))
for i in range(1, qsize):
    for j in range(0, qwidth-4):
        outputdata[i-1,j] = ((qlist[i])[j])[-1]
    outputdata[i-1,qwidth-4] = ((qlist[i])[qwidth-2])[-1]
cleandata = np.zeros((qsize-1,2))
for i in range(0,qsize-1):
    cleandata[i,1] = outputdata[i,qwidth-4]
    for j in range(0,48):
        cleandata[i,0] += outputdata[i,j] * 10**j
for i in range(0,qsize-1):
    for j in range(i,qsize-1):
        if cleandata[i,0] == cleandata[j,0]:
            cleandata[i,1] += cleandata[j,1]
maxrow = np.where(cleandata[:,1] == np.amax(cleandata[:,1]))[0]

stocks = ["Inbev 22.89","adidas 52.69","bayer 12.32","BBVA 4.11","BMW 1.29","BNP 29.95","CRH 41.36","Daimler 3.5","Danone 20.39", "DE Borse 29.0", "DE Post 36.82", "DE Tel -3.22", "Ahold 0.9", "Enel 39.84", "Engie 15.53", "Eni -1.6", "Essilor 22.97", "Fresenius 12.38", "Iberdrola 35.84", "Inditex 38.97", "Ing 11.31", "intesa 17.55", "Kering 51.21", "Air Liquide 29.78", "Linde 34.32", "Loreal 31.95", "LVMH 66.87", "Munchener 39.44", "Nokia -29.5", "Orange -7.14", "Philips 45.54", "Safran 31.18", "Sonofi 20.49", "Santander -8.4", "Airbus 59.68", "SAP 38.03", "Schneider 55.43", "Seimens 18.32", "Soc gen 21.29", "Telefonica -16.87", "TOTAL 7.58", "VINCI 36.7", "Vivendi 22.89", "volkwagen 25.58","Allianz 23.75", "Amadeus 21.98", "ASML 100.41", "AXA 32.41", "BASF 5.36"]

print(cleandata)
print(maxrow)

print("number of occurances: %f" % cleandata[maxrow[1],1])

print("\r\nstocks selected: ")
for i in range(0,48):
    if outputdata[maxrow[1],i] == 1:
        print(stocks[i])
        print("\r\n")
print(outputdata[maxrow[1],:])

print(stocks)

#print(np.where(cleandata[:,1] == np.amax(cleandata[:,1]))[0])

#'x0': 0, 'x1': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0, 'x14': 0, 'x15': 0, 'x16': 0, 'x17': 0, 'x18': 0, 'x19': 0, 'x2': 0, 'x20': 0, 'x21': 0, 'x22': 0, 'x23': 0, 'x24': 1, 'x25': 0, 'x26': 0, 'x27': 0, 'x28': 0, 'x29': 0, 'x3': 1, 'x30': 1, 'x31': 0, 'x32': 0, 'x33': 0, 'x34': 1, 'x35': 1, 'x36': 1, 'x37': 1, 'x38': 0, 'x39': 1, 'x4': 0, 'x40': 0, 'x41': 0, 'x42': 0, 'x43': 0, 'x44': 1, 'x45': 0, 'x46': 0, 'x47': 0, 'x48': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0
