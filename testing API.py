import requests

percent = 97
rating = 5.5

newrating = 5.6
#abc=[]

req5 = requests.get('https://osu.ppy.sh/api/get_user_recent?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&type=string&u=lwke&limit=2')
#print(req5)
abc=req5.json()
print(abc)

req1 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=2&mods=64&mode=0')
tester = req1.json()
#print (tester)


req2 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&s=600702')
tester1= req2.json()
#print(tester1)


APIBest = requests.get('https://osu.ppy.sh/api/get_scores?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&b=2993975')
BestScore=APIBest.json()
#print(BestScore)

# APIRecommend = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&since=2014-05-16')
# abc = APIRecommend.json()
# print (abc)

# for i in abc:
#     print (i)
#     print ('AAAAAAAAAAAAAAA')

# for i in tester:
#     if i['difficultyrating'] > newrating:
#         print('yes')