from TikTokApi import TikTokApi
import random
api = TikTokApi()
results = 1
count = 0
did = str(random.randint(10000, 999999999))
username="charlidamelio"
tiktoks = api.byUsername(username, results,custom_did=did)


for tiktok in tiktoks:



        #vid = tiktok['id']
        #url = 'https://www.tiktok.com/@' + user + '/video/' + vid + '?lang=vi'  # link to download video by user
        b = tiktok
        tiktokData = api.get_Video_By_TikTok(b,custom_did=did)
        print(b)
        with open("video.mp4", "wb") as out:  # save model
                out.write(tiktokData)