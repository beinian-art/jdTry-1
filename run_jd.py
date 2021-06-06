import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import urllib2, urllib
from json import *

cookie = "shshshfpa=f4cc9329-5037-42d4-8ce9-958fe557faea-1620402319; shshshfpb=a46voe9p9xen74oev1bsirQ%3D%3D; __jdu=1620402281395724102596; mba_muid=1620402281395724102596; unpl=V2_ZzNtbRVVQEF8WxEGfhpaAGJQQFsSVEJGfF8RUXgZDlcwUBIIclRCFnUUR1BnGVgUZwcZWEJcQhRFCEdkex5fDGQzElhCU0ESdw5OZEsaXDVmMxJaQVZGFHYLT1R5EVgDZAYSXEFTSxJFOEZcfyls0fKoytbVBQJXrLjjgtG3bAJiBBRUS1JHJXQ4R2Qwd11IZwQRXEdWQBZ8CERcfx9fAGcCEVlKUHMURQs%3d; mobilev=html5; webp=1; visitkey=9464124898559833; sc_width=1536; cid=9; retina=1; TrackerID=BuM4_FNgn54ZLyY8Zs71dl4UD0I6yxQMKs7xbVT4qVZVeWe1zRgTHYcZtm1xUGHOEVqjHX5wNqcELsCXIhRpHiwX8PXXoxwGlC7h3RL-2sYqvqbOs4VRgSxo5AnOKrZdnLbN9FZvxddQ8b8l2eAPfA; pt_key=AAJgn8fNADCHLrpf7Y2PYyZZVQcbJpxUNLiNFjboWyuTfT-5m6tNTVf7gMh6zumuJJj7qX8OFcg; pt_pin=%E8%A7%A3%E6%99%93%E4%B8%9C1314520; pt_token=gsmjcirg; pwdt_id=%E8%A7%A3%E6%99%93%E4%B8%9C1314520; shshshfp=434eb624e83d2c01cc473408ebffe43f; cartLastOpTime=1621086947; cartNum=13; kplTitleShow=1; wq_addr=519247372%7C5_142_42544_60043%7C%u6CB3%u5317_%u77F3%u5BB6%u5E84%u5E02_%u6865%u897F%u533A_%u957F%u5174%u8857%u9053%7C%u6CB3%u5317%u77F3%u5BB6%u5E84%u5E02%u6865%u897F%u533A%u957F%u5174%u8857%u9053%u957F%u5174%u885718%u53F7%u5357%u90ED%u82B1%u56ED%u5C0F%u533A17-1-704%7C114.40508%2C38.05178; jdAddrId=5_142_42544_60043; jdAddrName=%u6CB3%u5317_%u77F3%u5BB6%u5E84%u5E02_%u6865%u897F%u533A_%u957F%u5174%u8857%u9053; mitemAddrId=5_142_42544_60043; mitemAddrName=%u6CB3%u5317%u77F3%u5BB6%u5E84%u5E02%u6865%u897F%u533A%u957F%u5174%u8857%u9053%u957F%u5174%u885718%u53F7%u5357%u90ED%u82B1%u56ED%u5C0F%u533A17-1-704; __wga=1621087901784.1621086934729.1621083149112.1621083149112.10.2; __jda=122270672.1620402281395724102596.1620402281.1621086935.1622984059.8; __jdc=122270672; __jdv=122270672|github.com|-|referral|-|1622984058815; areaId=5; ipLoc-djd=5-258-0-0; __jdb=122270672.4.1620402281395724102596|8.1622984059; 3AB9D23F7A4B3C9B=Z7L2TG77AG2VNRVTI25SYKD52DCJMT6ZGOGNZDA7N5WMDUMGLZ6AYDRCS2AQV4AXK3CNO74DFJBW4BHP74PUM2HUD4; wlfstk_smdl=c25i6bem5yyp2pge32o8tfj2gfu415cd; TrackID=1bo4JtWjwrkj1kfl_3lqLCKbuK3HtLhAUnMJuqsP0roXueUBaf-b7HatfUXO4bATj4dIIcTO_7ugZSn4YTwib3HFYM0eUZOPcwwdvqza7yhfV54t9Tvyv3mbFEmaLybLE; thor=E3EC322C57FA76ECB298FC82BDE916F2050617203E17F5E7B684FB70D65E06E5A81EBD6A8C4FC3E7E1FA083297E0FC5E5722F1735879CECD55C8F87012DE3FC55B3C664F3960388F381003FC0D656B514D4427AA06967F800D552F5E91478694269D1B55BEF1F75C2136F1B6BF1CA14133B5813A8E13E6C25CFEFCB7CB19876D819B152879B2BA83CB507B2A62359EF7; pinId=3Iy_yevFLa5KgOktfhYvaw; pin=wdFbhCQUvuVFaA; unick=%E6%B7%98%E5%B0%8F%E5%8C%97%E5%90%96; ceshi3.com=203; _tp=2WUwMbg%2Bxqe4nL7954NCMQ%3D%3D; logining=1; _pst=wdFbhCQUvuVFaA"

def foo(actid): 
    f = urllib2.Request(
        url     = 'http://try.jd.com/migrate/apply?activityId='+actid+'&source=0',
        )
    f.add_header('Cookie', cookie);
    response = urllib2.urlopen(f)
    g = response.read()
    print g.decode('UTF-8','ignore')
    return 0

def foo2(actList): 
    f = urllib2.Request(
        url     = 'http://try.jd.com/user/getApplyStateByActivityIds?activityIds=' + ','.join(actList),
        )
    f.add_header('Cookie', cookie);
    f.add_header('Referer','http://try.jd.com/activity/getActivityList?page=1&activityState=0')
    response = urllib2.urlopen(f)
    g = response.read()
    d=JSONDecoder().decode(g)
    actlist2 = []
    for i in d:
        actlist2.append(str(i['activityId']))
    return set(actList) - set(actlist2)
    
def foo3(page): 
    f = urllib2.Request(
        url     = 'http://try.jd.com/activity/getActivityList?page='+str(page)+'&activityState=0',
        )
    response = urllib2.urlopen(f)
    d = response.read()
    soup = BeautifulSoup(d)

    actList = []
    for lind in soup.find_all('li'):
        actid = lind.get('activity_id')
        if actid:
            actList.append(str(actid))

    return actList
    
def foo4(): 
    f = urllib2.Request(
        url     = 'http://try.jd.com/activity/getActivityList?activityState=0',
        )
    response = urllib2.urlopen(f)
    d = response.read()
    soup = BeautifulSoup(d)

    count = 0
    start =  str(soup.head.script).find('{')
    end = str(soup.head.script).rfind('}') + 1
    jsonStr = str(soup.head.script)[start:end]
    jsonStr = jsonStr.replace('\'', "\"")

    d=JSONDecoder().decode(jsonStr)
    return d["pagination"]["pages"]

total = foo4()

for i in xrange(total+1):
    print i
    actList = foo3(i)
    actList = foo2(actList)
    for actid in actList:
        foo(actid)
        time.sleep(5)
print 'end'
while True:
    pass
