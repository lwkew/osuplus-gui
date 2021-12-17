from typing import Final
import requests
global recentscore
global recentmap
global req1
#09fe03d3b80c29a27e0b75b07e0c483c54657817



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
        self._maprating = 0
        recentscore = req1.json()
        latest_score1 = recentscore[0]
        self._Latest_300 = int(latest_score1['count300'])
        
        
        BeatmapID=latest_score1['beatmap_id']
        APIBest = requests.get('https://osu.ppy.sh/api/get_scores?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&b=' + str(BeatmapID))
        BestScore=APIBest.json()
        Pull1 = BestScore[0]
        self._Best300 = int(Pull1['count300'])

        # APITitle = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&b=' + str(BeatmapID))
        # recentmap1 = APITitle.json()
        # self._map_rating = int(recentmap1['difficultyrating'])
        
    def printer(self):
        #print(self._map_rating)
        print(self._Latest_300)
        print(self._Best300)



    def CalculateMapStars(self):
        recommendation_percent = 0
        FinalPercent = (self._Latest_300 / self._Best300) *100
        print(FinalPercent)
        
        if FinalPercent == 100:
            recommendation_percent = self._maprating +0.3
        elif FinalPercent >= 99:
            recommendation_percent = self._maprating + 0.3
        elif FinalPercent >= 97:
            recommendation_percent = self._map_rating +0.2
        elif FinalPercent >=95:
            recommendation_percent = self._map_rating +0.1

        
        print(recommendation_percent)
        

 
