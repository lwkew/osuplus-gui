from main import *
from typing import Final
import requests
global recentscore
global recentmap
global req1
#09fe03d3b80c29a27e0b75b07e0c483c54657817


#GLOBAL REQUEST FOR THE DATA FROM THE PLAYER IN THE GAME
req1 = requests.get('https://osu.ppy.sh/api/get_user_recent?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=20&u=lwke')

recentscore = []
recentmap = []

#FORMATTING THE DATA FOR THE LATEST SCORES TABLE
class userinfo():
    def __init__(self):
        pass

    def GetRecentScore():
        recentscore = req1.json()
        return recentscore

    def GetRecentTitle():
        recentscore=req1.json()
        titlelist=[]
        #LOOPING THROUGH THE LAST 20 RECENT PLAYS AND MAKING THEM AVAILABLE TO BE INPUT INTO THE TABLE
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
        self._map_rating = 0
        recentscore = req1.json()
        latest_score1 = recentscore[0]
        self._Latest_300 = int(latest_score1['count300'])
        
        
        BeatmapID=latest_score1['beatmap_id']
        APIBest = requests.get('https://osu.ppy.sh/api/get_scores?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&b=' + str(BeatmapID))
        BestScore=APIBest.json()
        Pull1 = BestScore[0]
        self._Best300 = int(Pull1['count300'])

        APITitle = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&b=' + str(BeatmapID))
        recentmap1 = APITitle.json()
        pull2 = recentmap1[0]
        self._map_rating = float(pull2['difficultyrating'])
        
        #APIRecommend = 

    def printer(self):
        print('map rating:', self._map_rating)
        print('latest 300 count:', self._Latest_300)
        print('best 300 count:', self._Best300)


    #CALCULATING THE PLAYERS STAR RATING FOR THE RECOMMENDATION, BASED OFF OF THEIR LAST PLAY
    def CalculateMapStars(self):
        self._new_rating = 0
        FinalPercent = (self._Latest_300 / self._Best300) *100
        print('final percent:', FinalPercent)
        
        if FinalPercent == 100:
            self._new_rating = self._map_rating +0.3
        elif FinalPercent >= 99:
            self._new_rating = self._map_rating + 0.3
        elif FinalPercent >= 97:
            self._new_rating = self._map_rating +0.2
        elif FinalPercent >=95:
            self._new_rating = self._map_rating +0.1
        elif FinalPercent >=93:
            self._new_rating = self._map_rating 
        elif 93 >= FinalPercent and FinalPercent >= 85:
            self._new_rating = self._map_rating - 0.1
        else:
            self._new_rating = self._map_rating - 0.2

        
        print('new star rating for recommend:', self._new_rating)

    def FindMap(self):
        abc = []
        dateloop = 2010
        
        for j in range (0,10):
            dateloop = dateloop +1
            APIRecommend = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=500&since=' + str(dateloop) + '-01-01')
            abc = APIRecommend.json()
            possible_recommend = []
            for i in abc:
                if (self._new_rating -0.1) < float(i['difficultyrating']) < (self._new_rating +0.1):
                    possible_recommend.append(i)
        return possible_recommend

    # def ModChoice(self):
    #     m=MainWindow()
    #     if m.CheckBox() == 1:
    #         self._new_rating = self._new_rating -0.2
    #     if m.Check_Box() ==2:
    #         self._new_rating = self._new_rating 
    #     if m.Check_Box() == 3:
    #         self._new_rating = self._new_rating -2
    #     if m.Check_Box() == 4:
    #         self._new_rating = self._new_rating -3
    

        

# m=recommendinfo()
# m.CalculateMapStars()
# m.FindMap()
        

 
