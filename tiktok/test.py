from TikTokApi import TikTokApi


api = TikTokApi()
results = 1
count = 0
username="longchunchun"
tiktoks = api.byUsername(username, results)
videoname="_video.mp4"
for tiktok in tiktoks:

    count = count +1

    vid = tiktok['id']
    url = 'https://www.tiktok.com/@' + username + '/video/' + vid + '?lang=vi'  # link to download video by user
    b = tiktok["video"]["downloadAddr"]
    #print(b)
    tiktokData = api.get_Video_By_DownloadURL(b,language='vi')
    with open("video.mp4", "wb") as out:  # save model
        out.write(tiktokData)
    #print(tiktok)
print(tiktok)