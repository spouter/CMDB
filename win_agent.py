import wmi

womaiwh = wmi.WMI ()
#for s in c.Win32_Service ():
#  if s.State == 'Stopped':
#    print s.Caption, s.State

#CPU
for processor in womaiwh.Win32_Processor(): 
	print "CPU ID: %s" % processor.DeviceID
	print "\nCPU Name: %s" % processor.Name.strip()+'\n'
#MEM
totalMemSize=0
for memModule in womaiwh.Win32_PhysicalMemory():  
	totalMemSize+=int(memModule.Capacity)
print "MEM: %.2fGB" %((totalMemSize+1048575)/1048576/1024)+'\n'
#DISK
for physical_disk in womaiwh.Win32_DiskDrive ():
    tmpdict = {} 
    tmpdict["Caption"] = physical_disk.Caption 
    tmpdict["Size"] = long(physical_disk.Size)/1024/1024/1024 
print "DISK Name: %s" % tmpdict["Caption"]
print "\nDISK Size: %s" % tmpdict["Size"]+'GB\n'
#intelface
tmplist=[]
for interface in womaiwh.Win32_NetworkAdapterConfiguration (IPEnabled=1): 
    tmpdict = {} 
    tmpdict["Description"] = interface.Description 
    tmpdict["IPAddress"] = interface.IPAddress[0] 
    tmpdict["IPSubnet"] = interface.IPSubnet[0] 
    tmpdict["MAC"] = interface.MACAddress 
    tmplist.append(tmpdict) 
for i in tmplist: 
    print i["Description"] 
    print '\t' + "MAC :" + '\t' + i["MAC"] 
    print '\t' + "IPAddress :" + '\t' + i["IPAddress"] 
    print '\t' + "IPSubnet :" + '\t' + i["IPSubnet"]

for sys in womaiwh.Win32_OperatingSystem(): 
      print "\nVersion :\t%s" % sys.Caption.encode("GBK") 
      print "Vernum :\t%s" % sys.BuildNumber 
#bios
for bios_id in womaiwh.Win32_BIOS():
	encrypt_str = encrypt_str+bios_id.SerialNumber.strip()
	print "bios number:", bios_id.SerialNumber.strip()
	print "encrypt_str:", encrypt_str
#BaseBoard
for board_id in c.Win32_BaseBoard():
	encrypt_str = encrypt_str+board_id.SerialNumber.strip()
	print "main board id:",board_id.SerialNumber.strip()
