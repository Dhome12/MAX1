import EGY
from EGY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#eGy-NgapaK
egy = LineClient(authToken='')
egy.log("Auth Token : " + str(egy.authToken))
channel = LineChannel(cl)
egy.log("Channel Access Token : " + str(channel.channelAccessToken))

egy1 = LineClient(authToken='')
egy1.log("Auth Token : " + str(egy1.authToken))
channel1 = LineChannel(egy2)
egy1.log("Channel Access Token : " + str(channel1.channelAccessToken))

egy2 = LineClient(authToken='')
egy2.log("Auth Token : " + str(egy2.authToken))
channel2 = LineChannel(egy2)
egy2.log("Channel Access Token : " + str(channel2.channelAccessToken))

egy3 = LineClient(authToken='')
egy3.log("Auth Token : " + str(egy3.authToken))
channel3 = LineChannel(egy3)
egy3.log("Channel Access Token : " + str(channel3.channelAccessToken))

boz = LineClient(authToken='')
boz.log("Auth Token : " + str(boz.authToken))
channel11 = LineChannel(boz)
boz.log("Channel Access Token : " + str(channel11.channelAccessToken))

print "Succeszz Login eGy-NgapaK TegaL-City"
poll = LinePoll(egy)
call = egy
creator = [""]
owner = [""]
admin = [""]
staff = [""]
mid = egy.getProfile().mid
Amid = egy1.getProfile().mid
Bmid = egy2.getProfile().mid
Cmid = egy3.getProfile().mid
Zmid = boz.getProfile().mid
KAC = [egy,egy1,egy2,egy3]
ABC = [egy1,egy2,egy3]
Bots = [mid,Amid,Bmid,Cmid,Zmid]
Dpk = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []

responsename1 = egy1.getProfile().displayName
responsename2 = egy2.getProfile().displayName
responsename3 = egy3.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"NGINTIP NIH YEEE 😊",
    "Respontag":"TAG TEG TAG TEG DOOOOORRRRRR 😃 😃 😃",
    "welcome":"Selamat datang & semoga betah nd janlupa jln'' note yh kk.... 😊 😊 😊",
    "comment":"Like & like by eGy-NgapaK",
    "message":"Terimakasih sudah add saya 😊 😊 😊 \nSakken kk eGy-NgapaK",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        egy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        egy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(egy.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        egy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        egy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(egy.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        egy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        egy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = egy.getAllContactIds()
        gid = egy.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n⏩ Group : "+str(len(gid))+"\n⏩ Teman : "+str(len(teman))+"\n⏩ Expired : In "+hari+"\n⏩ Version : ANTIJS2\n⏩ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n⏩ Runtime : \n • "+bot
        egy.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        egy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "❧MENU HELP❧\n" + \
                  "1" + key + "Me\n" + \
                  "2" + key + "Mid「@」\n" + \
                  "3" + key + "Info「@」\n" + \
                  "4" + key + "Nk「@」\n" + \
                  "5" + key + "Kick1「@」\n" + \
                  "6" + key + "Mybot\n" + \
                  "7" + key + "Status\n" + \
                  "8" + key + "About\n" + \
                  "9" + key + "Restart\n" + \
                  "10" + key + "Runtime\n" + \
                  "11" + key + "Creator\n" + \
                  "12" + key + "Speed/Sp\n" + \
                  "13" + key + "Sprespon\n" + \
                  "14" + key + "Tagall/Sepi/Kumpul\n" + \
                  "15" + key + "Joinall/Ngapak join/bye\n" + \
                  "16" + key + "Byeall\n" + \
                  "17" + key + "Byeme\n" + \
                  "18" + key + "Leave「Namagrup」\n" + \
                  "19" + key + "Ginfo\n" + \
                  "20" + key + "Open\n" + \
                  "21" + key + "Close\n" + \
                  "22" + key + "Url grup\n" + \
                  "23" + key + "Gruplist\n" + \
                  "24" + key + "Infogrup「angka」\n" + \
                  "25" + key + "Infomem「angka」\n" + \
                  "26" + key + "Remove chat\n" + \
                  "27" + key + "Lurking「on/off」\n" + \
                  "28" + key + "Lurkers\n" + \
                  "29" + key + "Sider「on/off」\n" + \
                  "30" + key + "Updatefoto\n" + \
                  "31" + key + "Updategrup\n" + \
                  "32" + key + "Updatebot\n" + \
                  "33" + key + "Broadcast:「Text」\n" + \
                  "34" + key + "Setkey「New Key」\n" + \
                  "35" + key + "Mykey\n" + \
                  "36" + key + "Resetkey\n" + \
                  "37" + key + "ID line:「Id Line nya」\n" + \
                  "38" + key + "Sholat:「Nama Kota」\n" + \
                  "39" + key + "Cuaca:「Nama Kota」\n" + \
                  "40" + key + "Lokasi:「Nama Kota」\n" + \
                  "41" + key + "Music:「Judul Lagu」\n" + \
                  "42" + key + "Lirik:「Judul Lagu」\n" + \
                  "43" + key + "Ytmp3:「Judul Lagu」\n" + \
                  "44" + key + "Ytmp4:「Judul Video」\n" + \
                  "45" + key + "Profileig:「Nama IG」\n" + \
                  "46" + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "47" + key + "Jumlah:「angka」\n" + \
                  "48" + key + "Spamtag「@」\n" + \
                  "49" + key + "Spamcall:「jumlahnya」\n" + \
                  "50" + key + "Spamcall\n" + \
                  "51" + key + "Notag「on/off」\n" + \
                  "52" + key + "Allpro「on/off」\n" + \
                  "53" + key + "Protecturl「on/off」\n" + \
                  "54" + key + "Protectjoin「on/off」\n" + \
                  "55" + key + "Protectkick「on/off」\n" + \
                  "56" + key + "Protectcancel「on/off」\n" + \
                  "57" + key + "Antijs「on/off」\n" + \
                  "58" + key + "Antijs stay\n" + \
                  "59" + key + "Ghost「on/off」\n" + \
                  "60" + key + "Sticker「on/off」\n" + \
                  "61" + key + "Respon「on/off」\n" + \
                  "62" + key + "Contact「on/off」\n" + \
                  "63" + key + "Autojoin「on/off」\n" + \
                  "64" + key + "Autoadd「on/off」\n" + \
                  "65" + key + "Welcome「on/off」\n" + \
                  "66" + key + "Autoleave「on/off」\n" + \
                  "67" + key + "Admin:on\n" + \
                  "68" + key + "Admin:repeat\n" + \
                  "69" + key + "Staff:on\n" + \
                  "70" + key + "Staff:repeat\n" + \
                  "71" + key + "Bot:on\n" + \
                  "71" + key + "Bot:repeat\n" + \
                  "72" + key + "Adminadd「@」\n" + \
                  "73" + key + "Admindell「@」\n" + \
                  "74" + key + "Staffadd「@」\n" + \
                  "75" + key + "Staffdell「@」\n" + \
                  "76" + key + "Botadd「@」\n" + \
                  "77" + key + "Botdell「@」\n" + \
                  "78" + key + "Refresh\n" + \
                  "79" + key + "Listbot\n" + \
                  "80" + key + "Listadmin\n" + \
                  "81" + key + "Listprotect\n" + \
                  "eGy-NgapaK"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "HELP eGy-BOT\n" + \
                  "eGy" + key + "Blc\n" + \
                  "eGy" + key + "Ban:on\n" + \
                  "eGy" + key + "Unban:on\n" + \
                  "eGy" + key + "Ban「@」\n" + \
                  "eGy" + key + "Unban「@」\n" + \
                  "eGy" + key + "Talkban「@」\n" + \
                  "eGy" + key + "Untalkban「@」\n" + \
                  "eGy" + key + "Talkban:on\n" + \
                  "eGy" + key + "Untalkban:on\n" + \
                  "eGy" + key + "Banlist\n" + \
                  "eGy" + key + "Talkbanlist\n" + \
                  "eGy" + key + "Clearban\n" + \
                  "eGy" + key + "Refresh\n" + \
                  "eGy" + key + "Cek sider\n" + \
                  "eGy" + key + "Cek spam\n" + \
                  "eGy" + key + "Cek pesan \n" + \
                  "eGy" + key + "Cek respon \n" + \
                  "eGy" + key + "Cek welcome\n" + \
                  "eGy" + key + "Set sider:「Text」\n" + \
                  "eGy" + key + "Set spam:「Text」\n" + \
                  "eGy" + key + "Set pesan:「Text」\n" + \
                  "eGy" + key + "Set respon:「Text」\n" + \
                  "eGy" + key + "Set welcome:「Text」\n" + \
                  "eGy" + key + "Myname:「Nama」\n" + \
                  "eGy" + key + "Bot1name:「Nama」\n" + \
                  "eGy" + key + "Bot2name:「Nama」\n" + \
                  "eGy" + key + "Bot3name:「Nama」\n" + \
                  "eGy" + key + "Bot3ngapak:「Nama」\n" + \
                  "eGy" + key + "Bot1up「Kirim fotonya」\n" + \
                  "eGy" + key + "Bot2up「Kirim fotonya」\n" + \
                  "eGy" + key + "Bot3up「Kirim fotonya」\n" + \
                  "eGy" + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "eGy" + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "NgapaK-CitY"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if egy.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            egy.reissueGroupTicket(op.param1)
                            X = egy.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            egy.updateGroup(X)
                            egy.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if egy1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                egy1.reissueGroupTicket(op.param1)
                                X = egy1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                egy1.updateGroup(X)
                                egy.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if egy2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    egy2.reissueGroupTicket(op.param1)
                                    X = egy2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    egy2.updateGroup(X)
                                    egy.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if egy3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        egy3.reissueGroupTicket(op.param1)
                                        X = egy3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        egy3.updateGroup(X)
                                        egy.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if egy.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            egy.reissueGroupTicket(op.param1)
                                            X = egy.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            egy.updateGroup(X)
                                            egy.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if egy1.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                egy1.reissueGroupTicket(op.param1)
                                                X = egy1.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                egy1.updateGroup(X)
                                                egy1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy.acceptGroupInvitation(op.param1)
                        ginfo = egy.getGroup(op.param1)
                        egy.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        egy.leaveGroup(op.param1)
                    else:
                        egy.acceptGroupInvitation(op.param1)
                        ginfo = egy.getGroup(op.param1)
                        egy.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy.acceptGroupInvitation(op.param1)
                        ginfo = egy.getGroup(op.param1)
                        egy.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        egy.acceptGroupInvitation(op.param1)
                        ginfo = egy.getGroup(op.param1)
                        egy.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy1.acceptGroupInvitation(op.param1)
                        ginfo = egy1.getGroup(op.param1)
                        egy1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        egy1.leaveGroup(op.param1)
                    else:
                        egy1.acceptGroupInvitation(op.param1)
                        ginfo = egy1.getGroup(op.param1)
                        egy1.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy2.acceptGroupInvitation(op.param1)
                        ginfo = egy2.getGroup(op.param1)
                        egy1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        egy2.leaveGroup(op.param1)
                    else:
                        egy2.acceptGroupInvitation(op.param1)
                        ginfo = egy2.getGroup(op.param1)
                        egy2.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy3.acceptGroupInvitation(op.param1)
                        ginfo = egy3.getGroup(op.param1)
                        egy3.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        egy3.leaveGroup(op.param1)
                    else:
                        egy3.acceptGroupInvitation(op.param1)
                        ginfo = egy3.getGroup(op.param1)
                        egy3.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = egy.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            egy.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = egy1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                egy1.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = egy2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    egy2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = egy3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        egy3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = egy.getGroup(op.param1)
                contact = egy.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                egy.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	egy3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                egy1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    egy2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        egy.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        egy.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = egy.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        egy.updateGroup(G)
                        invsend = 0
                        Ticket = egy.reissueGroupTicket(op.param1)
                        boz.acceptGroupInvitationByTicket(op.param1,Ticket)
                        boz.kickoutFromGroup(op.param1,[op.param2])
                        boz.leaveGroup(op.param1)
                        X = egy.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        egy.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boz.acceptGroupInvitation(op.param1)
                        G = boz.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        boz.updateGroup(G)
                        Ticket = boz.reissueGroupTicket(op.param1)
                        egy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        egy1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        egy2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        egy3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        boz.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        boz.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        boz.leaveGroup(op.param1)
                        egy.inviteIntoGroup(op.param1,[Zmid])
                        egy.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        egy.kickoutFromGroup(op.param1,[op.param2])
                        egy.findAndAddContactsByMid(op.param3)
                        egy.inviteIntoGroup(op.param1,[Zmid])
                        egy.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        egy.kickoutFromGroup(op.param1,[op.param2])
                        egy.findAndAddContactsByMid(op.param3)
                        egy.inviteIntoGroup(op.param1,[Zmid])
                        egy.sendMessage(op.param1,"=AntiJS Invited=")
                       
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            egy.kickoutFromGroup(op.param1,[op.param2])
                            egy.findAndAddContactsByMid(op.param3)
                            egy.inviteIntoGroup(op.param1,[op.param3])
                            egy.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            egy1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                egy2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    egy3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        egy1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            egy2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                egy.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy1.kickoutFromGroup(op.param1,[op.param2])
                        egy1.inviteIntoGroup(op.param1,[op.param3])
                        egy.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            egy2.kickoutFromGroup(op.param1,[op.param2])
                            egy2.inviteIntoGroup(op.param1,[op.param3])
                            egy.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                egy3.kickoutFromGroup(op.param1,[op.param2])
                                egy3.inviteIntoGroup(op.param1,[op.param3])
                                egy.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = egy1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    egy1.kickoutFromGroup(op.param1,[op.param2])
                                    egy1.updateGroup(G)
                                    Ticket = egy1.reissueGroupTicket(op.param1)
                                    egy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = egy1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    egy1.updateGroup(G)
                                    Ticket = egy1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        egy1.kickoutFromGroup(op.param1,[op.param2])
                                        egy1.inviteIntoGroup(op.param1,[op.param3])
                                        egy.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            egy2.kickoutFromGroup(op.param1,[op.param2])
                                            egy.inviteIntoGroup(op.param1,[op.param3])
                                            egy.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy2.kickoutFromGroup(op.param1,[op.param2])
                        egy2.inviteIntoGroup(op.param1,[op.param3])
                        egy1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            egy3.kickoutFromGroup(op.param1,[op.param2])
                            egy3.inviteIntoGroup(op.param1,[op.param3])
                            egy1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                egy.kickoutFromGroup(op.param1,[op.param2])
                                egy.inviteIntoGroup(op.param1,[op.param3])
                                egy1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = egy2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    egy2.kickoutFromGroup(op.param1,[op.param2])
                                    egy2.updateGroup(G)
                                    Ticket = egy2.reissueGroupTicket(op.param1)
                                    egy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = egy2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    egy2.updateGroup(G)
                                    Ticket = egy2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        egy2.kickoutFromGroup(op.param1,[op.param2])
                                        egy2.inviteIntoGroup(op.param1,[op.param3])
                                        egy1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            egy3.kickoutFromGroup(op.param1,[op.param2])
                                            egy3.inviteIntoGroup(op.param1,[op.param3])
                                            egy1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy3.kickoutFromGroup(op.param1,[op.param2])
                        egy3.inviteIntoGroup(op.param1,[op.param3])
                        egy2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            egy.kickoutFromGroup(op.param1,[op.param2])
                            egy.inviteIntoGroup(op.param1,[op.param3])
                            egy2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                egy1.kickoutFromGroup(op.param1,[op.param2])
                                egy1.inviteIntoGroup(op.param1,[op.param3])
                                egy2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = egy3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    egy3.kickoutFromGroup(op.param1,[op.param2])
                                    egy3.updateGroup(G)
                                    Ticket = egy3.reissueGroupTicket(op.param1)
                                    egy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = egy3.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    egy3.updateGroup(G)
                                    Ticket = egy3.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        egy1.kickoutFromGroup(op.param1,[op.param2])
                                        egy1.inviteIntoGroup(op.param1,[op.param3])
                                        egy2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            egy3.kickoutFromGroup(op.param1,[op.param2])
                                            egy3.inviteIntoGroup(op.param1,[op.param3])
                                            egy2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy.kickoutFromGroup(op.param1,[op.param2])
                        egy.inviteIntoGroup(op.param1,[op.param3])
                        egy3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            egy1.kickoutFromGroup(op.param1,[op.param2])
                            egy1.inviteIntoGroup(op.param1,[op.param3])
                            egy3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                egy2.kickoutFromGroup(op.param1,[op.param2])
                                egy2.inviteIntoGroup(op.param1,[op.param3])
                                egy3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = egy.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    egy.kickoutFromGroup(op.param1,[op.param2])
                                    egy.updateGroup(G)
                                    Ticket = egy.reissueGroupTicket(op.param1)
                                    egy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    egy3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = egy.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    egy.updateGroup(G)
                                    Ticket = egy.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        egy.kickoutFromGroup(op.param1,[op.param2])
                                        egy.inviteIntoGroup(op.param1,[op.param3])
                                        egy3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            egy1.kickoutFromGroup(op.param1,[op.param2])
                                            egy1.inviteIntoGroup(op.param1,[op.param3])
                                            egy3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy.kickoutFromGroup(op.param1,[op.param2])
                        egy.findAndAddContactsByMid(op.param1,admin)
                        egy.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            egy1.kickoutFromGroup(op.param1,[op.param2])
                            egy1.findAndAddContactsByMid(op.param1,admin)
                            egy1.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                egy2.kickoutFromGroup(op.param1,[op.param2])
                                egy2.findAndAddContactsByMid(op.param1,admin)
                                egy2.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        egy1.kickoutFromGroup(op.param1,[op.param2])
                        egy1.findAndAddContactsByMid(op.param1,staff)
                        egy1.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            egy2.kickoutFromGroup(op.param1,[op.param2])
                            egy2.findAndAddContactsByMid(op.param1,staff)
                            egy2.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                egy3.kickoutFromGroup(op.param1,[op.param2])
                                egy3.findAndAddContactsByMid(op.param1,staff)
                                egy3.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = egy.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = egy.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        egy.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           egy.sendMessage(msg.to, wait["Respontag"])
                           egy.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           egy.mentiontag(msg.to,[msg._from])
                           egy.sendMessage(msg.to, "Jangan tag saya....")
                           egy.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    egy.sendMessage(msg.to,"「Cek ID Sticker」\n❧STKID : " + msg.contentMetadata["STKID"] + "\n❧STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❧STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    egy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = egy.getContact(msg.contentMetadata["mid"])
                        path = egy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        egy.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        egy.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    egy.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    egy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = egy.getContact(msg.contentMetadata["mid"])
                        path = egy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        egy.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        egy.sendImageWithURL(msg.to, image)
#NgapaK ADD
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        egy.sendMessage(msg.to,"Contact kui uwis dadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        egy.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        egy.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        egy.sendMessage(msg.to,"Contact itu bukan anggota bot Dpk")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        egy.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        egy.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        egy.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        egy.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        egy.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        egy.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        egy.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        egy.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        egy.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        egy.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        egy.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        egy.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        egy.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        egy.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        egy.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        egy.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = egy.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            egy.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = egy.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     egy.updateGroupPicture(msg.to, path)
                     egy.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = egy.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            egy.updateProfilePicture(path)
                            egy.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = egy1.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            egy1.updateProfilePicture(path)
                            egy1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = egy2.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            egy2.updateProfilePicture(path)
                            egy2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = egy3.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            egy3.updateProfilePicture(path)
                            egy3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = boz.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            boz.updateProfilePicture(path)
                            boz.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = egy1.downloadObjectMsg(msg_id)
                     path2 = egy2.downloadObjectMsg(msg_id)
                     path3 = egy3.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     egy1.updateProfilePicture(path1)
                     egy1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     egy2.updateProfilePicture(path2)
                     egy2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     egy3.updateProfilePicture(path3)
                     egy3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        egy.sendChatChecked(msg.to, msg_id)
                        egy1.sendChatChecked(msg.to, msg_id)
                        egy2.sendChatChecked(msg.to, msg_id)
                        egy3.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               egy.sendMessage(msg.to, str(helpMessage))
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': 'u7a02fd8b9a35dac64e3615ffa35e93aa'}
                               egy.sendText(msg.to,"creator by:eGy-NgapaK")
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                egy.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                egy.sendText(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               egy.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "NgapaK PŘØŤĘČŤÎØŇ\n"
                                if wait["sticker"] == True: md+="❧Sticker「ON」\n"
                                else: md+="❧Sticker「OFF」\n"
                                if wait["contact"] == True: md+="❧Contact「ON」\n"
                                else: md+="❧Contact「OFF」\n"
                                if wait["talkban"] == True: md+="❧Talkban「ON」\n"
                                else: md+="❧Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="❧Notag「ON」\n"
                                else: md+="❧Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="❧Respon「ON」\n"
                                else: md+="❧Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="❧Autojoin「ON」\n"
                                else: md+="❧Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="❧Autoadd「ON」\n"
                                else: md+="❧Autoadd「OFF」\n"
                                if msg.to in welcome: md+="❧Welcome「ON」\n"
                                else: md+="❧Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="❧Autoleave「ON」\n"
                                else: md+="❧Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="❧Protecturl「ON」\n"
                                else: md+="❧Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="❧Protectjoin「ON」\n"
                                else: md+="❧Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="❧Protectkick「ON」\n"
                                else: md+="❧Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="❧Protectcancel「ON」\n"
                                else: md+="❧Protectcancel「OFF」\n"
                                if msg.to in protectantijs: md+="❧Antijs「ON」\n"
                                else: md+="❧Antijs「OFF」\n"  
                                if msg.to in ghost: md+="❧Ghost「ON」\n"
                                else: md+="❧Ghost「OFF」\n"                                   
                                egy.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': 'u7a02fd8b9a35dac64e3615ffa35e93aa'}

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                egy.sendText(msg.to,"Creator Bot eGy-NgapaK") 
                                ma = ""
                                for i in creator:
                                    ma = egy.getContact(i)
                                    egy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               egy.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               egy.sendMessage1(msg)

                        elif text.lower() == "mid":
                               egy.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = egy.getContact(key1)
                               egy.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               egy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               egy.sendMessage(msg.to, "❧Nama : "+str(mi.displayName)+"\n❧Mid : " +key1+"\n❧Status Msg"+str(mi.statusMessage))
                               egy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(egy.getContact(key1)):
                                   egy.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   egy.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               egy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               egy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               egy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               egy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               egy.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   egy.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                             #      egy.removeAllMessages(op.param2)
                                   egy1.removeAllMessages(op.param2)
                                   egy2.removeAllMessages(op.param2)
                                   egy3.removeAllMessages(op.param2)
                                   egy.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = egy.getGroupIdsJoined()
                               for group in saya:
                                   egy.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   egy.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   egy.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               egy.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               egy.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               egy.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = egy.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(egy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                egy.sendMessage(msg.to, "❧NgapaK FAMZ GRUP info\n\n❧Nama Group : {}".format(G.name)+ "\n❧ID Group : {}".format(G.id)+ "\n❧Pembuat : {}".format(G.creator.displayName)+ "\n❧Waktu Dibuat : {}".format(str(timeCreated))+ "\n❧Jumlah Member : {}".format(str(len(G.members)))+ "\n❧Jumlah Pending : {}".format(gPending)+ "\n❧Group Qr : {}".format(gQr)+ "\n❧Group Ticket : {}".format(gTicket))
                                egy.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                egy.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                egy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = egy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = egy.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(egy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "❧NgapaK Fams Grup Info\n"
                                ret_ += "\n❧Nama Group : {}".format(G.name)
                                ret_ += "\n❧ID Group : {}".format(G.id)
                                ret_ += "\n❧Pembuat : {}".format(gCreator)
                                ret_ += "\n❧Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n❧Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n❧Jumlah Pending : {}".format(gPending)
                                ret_ += "\n❧Group Qr : {}".format(gQr)
                                ret_ += "\n❧Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                egy.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = egy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = egy.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "❧"+ str(no) + ". " + mem.displayName
                                egy.sendMessage(to,"❧Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = egy.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = egy.getGroup(i)
                                if ginfo == group:
                                    egy1.leaveGroup(i)
                                    egy2.leaveGroup(i)
                                    egy3.leaveGroup(i)
                                    egy.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = egy.getAllContactIds()
                               for i in gid:
                                   G = egy.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               egy.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = egy.getGroupIdsJoined()
                               for i in gid:
                                   G = egy.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = egy1.getGroupIdsJoined()
                               for i in gid:
                                   G = egy1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               egy1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = egy2.getGroupIdsJoined()
                               for i in gid:
                                   G = egy2.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               egy2.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = egy3.getGroupIdsJoined()
                               for i in gid:
                                   G = egy3.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               egy3.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = egy.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   egy.updateGroup(X)
                                   egy.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = egy.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   egy.updateGroup(X)
                                   egy.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = egy.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      egy.updateGroup(x)
                                   gurl = egy.reissueGroupTicket(msg.to)
                                   egy.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                egy.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                egy.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                egy.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                egy1.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                egy2.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                egy3.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                boz.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = egy.getProfile()
                                profile.displayName = string
                                egy.updateProfile(profile)
                                egy.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = egy1.getProfile()
                                profile.displayName = string
                                egy1.updateProfile(profile)
                                egy1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = egy2.getProfile()
                                profile.displayName = string
                                egy2.updateProfile(profile)
                                egy2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = egy3.getProfile()
                                profile.displayName = string
                                egy3.updateProfile(profile)
                                egy3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("botngapak: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boz.getProfile()
                                profile.displayName = string
                                boz.updateProfile(profile)
                                boz.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "sepi" or text.lower() == 'kumpul':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = egy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                             try:
                                 lur = len(nama)//20
                                 for fu in range(lur+1):
                                     hdc = u''
                                     sell=0
                                     com=[]
                                     for rid in gname.members[fu*20 : (fu+1)*20]:
                                         com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                         sell += 7
                                         hdc += u'@A_NgapaK\n'
                                         atas = '\n Heheee {} '.format(str(gname.name))
                                         atas += '\n Nah {} Member'.format(str(len(local)))
                                     egy.sendMessage(send, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                             except Exception as error:
                                 egy.sendMessage(send, str(error))

                        elif cmd == "tagall" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = egy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)r
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +egy.getContact(m_id).displayName + "\n"
                                egy.sendMessage(msg.to,"❧NgapaK  bot\n\n"+ma+"\nTotal「%s」 Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +egy.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +egy.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +egy.getContact(m_id).displayName + "\n"
                                egy.sendMessage(msg.to,"❧NgapaK  admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」 NgapaK" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +egy.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +egy.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +egy.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +egy.getGroup(group).name + "\n"
                                egy.sendMessage(msg.to,"❧NgapaK Fams Protection\n\n❧PROTECT URL :\n"+ma+"\n❧PROTECT KICK :\n"+mb+"\n❧PROTECT JOIN :\n"+md+"\n❧PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga  eGy-NgapaK" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                egy1.sendMessage(msg.to,"NgapaK satu kodir bozz")
                                egy2.sendMessage(msg.to,"NgapaK dua kodir bozz")
                                egy3.sendMessage(msg.to,"NgapaK tiga kodir bozz")
                                egy.sendMessage(msg.to,"Mantaaaaapppppp brooo")

                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Amid]
                                    egy.inviteIntoGroup(msg.to, anggota)
                                    egy2.acceptGroupInvitation(msg.to)
                                    egy3.acceptGroupInvitation(msg.to)
                                    egy1.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = egy.getGroup(msg.to)
                                    egy.inviteIntoGroup(msg.to, [Zmid])
                                    egy.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass
    
                        elif cmd == "joinall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                ginfo = egy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                egy.updateGroup(G)
                                invsend = 0
                                Ticket = egy.reissueGroupTicket(msg.to)
                                egy1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                egy2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                egy3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = egy3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                egy3.updateGroup(G)

                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                egy1.sendText(msg.to, "Pappaaayyyyyy fams "+str(G.name))
                                egy1.leaveGroup(msg.to)
                                egy2.leaveGroup(msg.to)
                                egy3.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                egy.sendText(msg.to, "Assalamualaikum.wr.wb. Pappaaayyyyyy fams "+str(G.name))
                                egy.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = egy.getGroupIdsJoined()
                                for i in gid:
                                    h = egy.getGroup(i).name
                                    if h == ng:
                                        egy1.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        egy1.leaveGroup(i)
                                        egy2.leaveGroup(i)
                                        egy3.leaveGroup(i)
                                        egy.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                ginfo = egy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                egy.updateGroup(G)
                                invsend = 0
                                Ticket = egy.reissueGroupTicket(msg.to)
                                egy1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = egy1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                egy1.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                ginfo = egy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                egy.updateGroup(G)
                                invsend = 0
                                Ticket = egy.reissueGroupTicket(msg.to)
                                egy2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = egy2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                egy2.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                ginfo = egy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                egy.updateGroup(G)
                                invsend = 0
                                Ticket = egy.reissueGroupTicket(msg.to)
                                egy3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = egy3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                egy3.updateGroup(G)

                        elif cmd == "ngapak join":
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                ginfo = egy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                egy.updateGroup(G)
                                invsend = 0
                                Ticket = egy.reissueGroupTicket(msg.to)
                                boz.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = boz.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                boz.updateGroup(G)

                        elif cmd == "ngapak bye":
                            if msg._from in admin:
                                G = egy.getGroup(msg.to)
                                boz.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                egy.sendMessage(msg.to, "❧NgapaK Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               egy.sendMessage(msg.to, "Ngitung speed bozzx...")
                               elapsed_time = time.time() - start
                               egy.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               egy1.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               egy2.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               egy3.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 egy.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 egy.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(egy.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        egy.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    egy.sendText(msg.to, "User kosong...")
                            else:
                                egy.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  egy.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  egy.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  egy.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n❧Lokasi : " + data[0]
                                         ret_ += "\n❧" + data[1]
                                         ret_ += "\n❧" + data[2]
                                         ret_ += "\n❧" + data[3]
                                         ret_ += "\n❧" + data[4]
                                         ret_ += "\n❧" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  egy.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n❧Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n❧Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n❧Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n❧Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n❧Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                egy.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n❧Location : " + data[0]
                                    ret_ += "\n❧Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                egy.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          egy.sendText(msg.to, str(ret_))
                                   except:
                                       egy.sendText(to, "Lirik Ra ono bozzz")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      egy.sendText(msg.to, str(ret_))
                                      egy.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      egy.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      egy.sendText(to, "Musik Ra ono bozz")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    egy.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    egy.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧Author : ' + str(vid.author)
                                    durasi = '\n❧Duration : ' + str(vid.duration)
                                    suka = '\n❧Likes : ' + str(vid.likes)
                                    rating = '\n❧Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧Deskripsi : ' + str(vid.description)
                                egy.sendVideoWithURL(msg.to, me)
                                egy.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                egy.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n❧Author : ' + str(vid.author)
                                    durasi = '\n❧Duration : ' + str(vid.duration)
                                    suka = '\n❧Likes : ' + str(vid.likes)
                                    rating = '\n❧Rating : ' + str(vid.rating)
                                    deskripsi = '\n❧Deskripsi : ' + str(vid.description)
                                egy.sendImageWithURL(msg.to, me)
                                egy.sendAudioWithURL(msg.to, shi)
                                egy.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                egy.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "❧Link : " + "https://www.instagram.com/" + instagram
                                text = "❧Name : "+namaIG+"\n❧Username : "+usernameIG+"\n❧Biography : "+bioIG+"\n❧Follower : "+followerIG+"\n❧Following : "+followIG+"\n❧Post : "+mediaIG+"\n❧Verified : "+verifIG+"\n❧Private : "+privateIG+"" "\n" + link
                                egy.sendImageWithURL(msg.to, profileIG)
                                egy.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    egy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            egy.sendMessage(msg.to,"❧I N F O R M A S I ❧\n\n"+"❧Date Of Birth : "+lahir+"\n❧Age : "+usia+"\n❧Ultah : "+ultah+"\n❧Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                egy.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                egy.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                egy.sendMessage1(msg)
                                            except Exception as e:
                                                egy.sendText(msg.to,str(e))
                                    else:
                                        egy.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = egy.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                egy.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        egy.sendText(msg.to,str(e))
                                else:
                                    egy.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      egy.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      egy1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      egy2.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      egy3.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      egy.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      egy1.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      egy2.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      egy3.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = egy.findContactsByUserid(msgs)
                              if True:
                                  egy.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  egy.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = egy.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'Allpro' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = egy.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = egy.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  egy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = egy.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    egy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = egy.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           egy.updateGroup(G)
                                           invsend = 0
                                           Ticket = egy.reissueGroupTicket(msg.to)
                                           boz.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           boz.kickoutFromGroup(msg.to, [target])
                                           boz.leaveGroup(msg.to)
                                           X = egy.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           egy.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           egy.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           egy.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           egy.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           admin.remove(target)
                                           egy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           staff.remove(target)
                                           egy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           Bots.remove(target)
                                           egy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                egy.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = egy.getContact(i)
                                    egy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = egy.getContact(i)
                                    egy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = egy.getContact(i)
                                    egy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                egy.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                egy.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                egy.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                egy.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                egy.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                egy.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                egy.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                egy.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                egy.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                egy.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                egy.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                egy.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                egy.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                egy.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                egy.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                egy.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                egy.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                egy.sendText(msg.to,"Autojoin Tiket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           egy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           egy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           egy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           egy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                egy.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                egy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +egy.getContact(m_id).displayName + "\n"
                                egy.sendMessage(msg.to,"❧NgapaK Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                egy.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +egy.getContact(m_id).displayName + "\n"
                                egy.sendMessage(msg.to,"NgapaK Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    egy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = egy.getContact(i)
                                        egy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = egy.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              egy.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  egy.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  egy.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  egy.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  egy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  egy.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  egy.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  egy.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  egy.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  egy.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  egy.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               egy.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = egy.findGroupByTicket(ticket_id)
                                     egy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     egy.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = egy1.findGroupByTicket(ticket_id)
                                     egy1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     egy1.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = egy2.findGroupByTicket(ticket_id)
                                     egy2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     egy2.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = egy3.findGroupByTicket(ticket_id)
                                     egy3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     egy3.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
