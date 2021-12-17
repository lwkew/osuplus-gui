from typing import Final
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
        self._Latest_300 = 0
        self._Best300 = 0
    
    def GetLatestPercent(self):
        self._Latest_300 = int(recentscore['count300'])
        return self._Latest_300

    def GetBestPercent(self):
        recentscore=req1.json()
        latest_test = recentscore[0]
        BeatmapID=latest_test['beatmap_id']
        APIBest = requests.get('https://osu.ppy.sh/api/get_scores?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&b=' + str(BeatmapID))
        BestScore=APIBest.json()
        Pull1 = BestScore[0]
        self._Best300 = int(Pull1['count300'])
        return self._Best300

def CalculateMapStars(self):
    FinalPercent = (self._Latest_300 / self._Best300) *100
    if FinalPercent == 100:
        Recommendation_percent = FinalPercent +2
    elif FinalPercent >= 99:
        Recommendation_percent = FinalPercent +2
