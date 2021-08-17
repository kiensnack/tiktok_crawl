from TikTokApi import TikTokApi
from datetime import datetime
from datetime import date

api = TikTokApi()
results = 4
count = 0
username="kingofrap.viva"
tiktoks = api.byUsername(username, results )
videoname="_video.mp4"
for tiktok in tiktoks:

    count = count +1


    vid = tiktok['id']
    url = 'https://www.tiktok.com/@' + username + '/video/' + vid + '?lang=vi' #link to download video by user

    today = date.today().strftime('%Y-%m-%d ')
    ts = tiktok['createTime']
    a = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d ')

    if (a == today):
        tiktokData = api.get_Video_No_Watermark(url, return_bytes=1)  # download video tiktok
        with open(str(count)+username + "$" + videoname, 'wb') as out:  # save model
            out.write(tiktokData)
    else:
        print(username + "has no new video")








    #tiktokData = api.get_Video_No_Watermark(url, return_bytes=1) #download video tiktok

    #print(tiktok)

    #with open(username+"_"+videoname, 'wb') as out:  #save model
         #out.write(tiktokData)


    '''
    print(tiktok['itemInfos']['id'])
    '''
#print(len(tiktoks))
