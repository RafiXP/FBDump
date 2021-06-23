import os,sys,requests,json,time,random
from termcolor import cprint

#####BANNER#####
def banner():
 cprint ('''
  ---------------------------------------------------------------
    _____ ____  ____                         | FBDump V.1.0 BETA
   |  ___| __ )|  _ \ _   _ _ __ ___  _ __   | Coded By : RafiXP
   | |_  |  _ \| | | | | | | '_ ` _ \| |_ \  | Team : IndoXploit Sec
   |  _| | |_) | |_| | |_| | | | | | | |_) | | Status Tools : Legal
   |_|   |____/|____/ \__,_|_| |_| |_| .__/  | Dev By : Facebook.inc
                                     |_|     |
  ---------------------------------------------------------------
''','blue')

def data():
 print
os.system('clear')
banner()
tok = raw_input('[?] Token User: ')
idt = raw_input('[?] ID Target : ')
print
a = requests.get('https://graph.facebook.com/me?access_token='+tok)
b = json.loads(a.text)
try :
 if b["verified"]==True:
   cprint ('[*] Data Dan Akses Diterima !','yellow')
   time.sleep(2)
   cprint ('[*] Login Berhasil !','yellow')
   time.sleep(1)
   "res()"
 elif b["verified"]==False:
   cprint ('[*] Data Dan Akses Diterima !','yellow')
   time.sleep(2)
   cprint ('[*] Login Berhasil !','yellow')
   time.sleep(1)
   "res()"
 elif b == "error":
   cprint ('[!] Akun Terkena Checkpoint','red')
   time.sleep(2)
   cprint ('[!] Data Dan Akses Ditolak !','red')
   cprint ('[!] Keluar','red')
   os.system('exit')
except KeyError:
 pass

def res():
 print
os.system('clear')
banner()
c = requests.get('https://graph.facebook.com/me?access_token='+tok)
d = json.loads(c.text)

nama=b["name"]
id=b["id"]

print (' [*] Username : '+nama)
print (' [*] ID User  : '+id)
print
time.sleep(2)
cprint ('[*] Mendapatkan Data Dari Target...','green')
print

q = requests.get('https://graph.facebook.com/'+idt+'/?access_token='+tok)
r = json.loads(q.text)

try :
  print
  cprint ('Hasil :','yellow')
  print
  print "Nama Pengguna  :", r["name"]
  print "Nama Awal      :", r["first_name"]
  print "Nama Akhir     :", r["last_name"]
  print "ID Pengguna    :", r["id"]
  print "Tanggal Lahir  :", r["birthday"]
  print "Bahasa Kustom  :", r["locale"]
  print "Timezone       :", r["timezone"]
  print "Link Facebook  :", r["link"]
  print "No.telepon     :", r["mobile_phone"]
  print "Username       :", r["username"]
  print "Email Pengguna :", r["email"]

except KeyError:
 pass

print "\n"
bk=raw_input(' [ Back ]')
data()
