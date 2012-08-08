import datetime

#############################################
#               Parameters                  #
#############################################

inFile  = 'testData.tsv'

outFile = 'output.txt'

format  = "%m/%d/%Y"

owner   = "username"

hour =  8

def parseLine(line):
    try:
        a = str.split(line)
        d = datetime.datetime.strptime(a[0], format)
        out = "0 " + str(hour) + " " + str(d.day) + " " + str(d.month)
        out += " * python sendMail.py " + a[1] + "@mit.edu\n"
        return out
    except:
        #do nothing
        pass

def run():
    f = open(inFile)
    f2 = open(outFile, "w")
    f2.write("PATH=/mit/%s/cron_scripts:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/X11R6/bin\n" % (owner) +
             "MAILTO=\"%s@mit.edu\"\n" % (owner))
    for x in f:
      f2.write(parseLine(x)+"\n")
