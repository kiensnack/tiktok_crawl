from TikTokApi import TikTokApi
from datetime import datetime
from datetime import date
import random
users = ["dangnhung1409","philinh_","kingofrap.viva","nguyenngochonglan_410"
        ,"longchunchun","chaomini","luongthingocha","luongchidien","trucanh.nguyen98",
         "tra.dang.904","fuu_2003","0206_tv_","mr.dat2k","teenefff","teenefff","bongtim96",
         "nguyenngochan266","lf.tlinh","lebong95","cat_20s","po.trann77","mocachodien","yenjiivu",
         "___midi___","laamiizzz","hoaa.hanassii","tra.dang.904"]
api = TikTokApi()
for user in users:
    results = 1
    did = str(random.randint(10000, 999999999))
    #print(did)
    tiktoks = api.byUsername(user, results,custom_did=did)
    videoname = "video.mp4"
    count =0
    for tiktok in tiktoks:

        count = count +1

        #vid = tiktok['id']
        #url = 'https://www.tiktok.com/@' + user + '/video/' + vid + '?lang=vi'  # link to download video by user
        #b = tiktok["video"]["downloadAddr"]
        today = date.today().strftime('%Y-%m-%d ')    #get date today
        ts = tiktok['createTime']
        a = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d ')  #convert unix time of tiktok video to normal date
        #b = tiktok
        if (a == today):
            print(str(count)+user +" has  new video")
            #tiktokData = api.get_Video_By_DownloadURL(b)  # download video tiktok
            tiktokData = api.get_Video_By_TikTok(tiktok, custom_did=did)
            with open(str(count)+user + videoname, 'wb') as out:  # save model
                out.write(tiktokData)
        else:
            print(user + " has no new video")