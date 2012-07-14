import datetime

#############################################
#               Parameters                  #
#############################################

inFile = 'testData.tsv'

outFile = 'output.txt'

format = "%m/%d/%Y"

hour =  8

def parseLine(line):
    try:
        a = str.split(line)
        d = datetime.datetime.strptime(a[0], format)
        out = "0 " + str(hour) + " " + str(d.day) + " " + str(d.month)
        out += " * python sendMail.py " + a[1] + "@mit.edu\n"
        print out
    except:
        #do nothing
        pass

def run():
    f = open(inFile)
    for x in f:
        parseLine(x)
