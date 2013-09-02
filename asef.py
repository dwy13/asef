#!/usr/bin/python
import os
import argparse
import sys
import time
import subprocess


apkurl = sys.argv[1]

#set tools dir
adb = "/home/yu/android-sdks/platform-tools/adb"
aapt = "/home/yu/android-sdks/build-tools/18.0.1/aapt"

#read apkinfo
apkinfo = os.popen(aapt+" d badging "+ apkurl)
apkinfo = apkinfo.read()

#get apkname
start = apkinfo.find("package")
end = apkinfo.find("versionCode",start)
apkpackage = apkinfo[start:end-1]
apkname = apkpackage[apkpackage.find("'")+1:apkpackage.rfind("'")]

#get launch activity
start = apkinfo.find("launchable-activity")
end = apkinfo.find("label",start)
apkactivity = apkinfo[start:end-1]
apkactivity = apkactivity[apkactivity.find("'")+1:apkactivity.rfind("'")]

print apkname
print apkactivity
'''
if os.path.exists("results") == False:
	os.mkdir("results")

timeformat = "%y_%m_%d-%X"
testdir = "/TEST_"+time.strftime(timeformat)
if os.path.exists("results/"+apkname) == False:
	os.mkdir("results/"+apkname)
os.mkdir("results/"+apkname+testdir)

netdir = "results/"+apkname+testdir+"/network_traffic.pcap"
'''

#install apk
os.system(adb+" -e install "+apkurl)

#launch apk
os.system(adb+" -e shell am start -W "+apkname+"/"+apkactivity)

time.sleep(10)

#send gestures
os.system(adb+" -e shell monkey -p "+apkname+" 100")

#unistall apk
os.system(adb+" -e uninstall "+apkname)
