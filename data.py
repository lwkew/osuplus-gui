import requests
global recentscore
global recentmap
global req1
        
req1 = requests.get('https://osu.ppy.sh/api/get_user_recent?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=20&u=lwke')

recentscore = []
recentmap = []

class userinfo():
    def __init__(self):
        pass

    def GetRecentScore():
        recentscore = req1.json()
        return recentscore

    def GetRecentTitle():
        recentscore=req1.json()
        titlelist=[]
        for i in range (len(recentscore)):
            latest_test = recentscore[i]
            BeatmapID=latest_test['beatmap_id']
            APITitle = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&b=' + str(BeatmapID))
            recentmap = APITitle.json()
            titlelist.append(recentmap[0]['title'])
        return titlelist


class recommendinfo():
    def __init__(self):
        self._Latest_300=[]
        pass
    
    def GetLatestPercent(self):
        print(recentscore)
        self._Latest_300 = recentscore['count300']
        print(self._Latest_300)


r=recommendinfo()
r.GetLatestPercent

