from TikTokApi import TikTokApi
from datetime import datetime
from datetime import date

users = ["dangnhung1409","philinh_","kingofrap.viva","nguyenngochonglan_410","longchunchun","chaomini","luongthingocha"]
api = TikTokApi()
for user in users:
    results = 1
    tiktoks = api.byUsername(user, results)
    videoname = "_video.mp4"
    count =0
    for tiktok in tiktoks:

        count = count +1

        #vid = tiktok['id']
        #url = 'https://www.tiktok.com/@' + user + '/video/' + vid + '?lang=vi'  # link to download video by user
        b = tiktok["video"]["downloadAddr"]
        print(b)
        today = date.today().strftime('%Y-%m-%d ')    #get date today
        ts = tiktok['createTime']
        a = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d ')  #convert unix time of tiktok video to normal date

        if (a == today):
            print(str(count)+user +" has  new video")
            tiktokData = api.get_Video_By_DownloadURL(b)  # download video tiktok
            with open(str(count)+user + "$" + videoname, 'wb') as out:  # save model
                out.write(tiktokData)
        else:
            print(user + " has no new video")