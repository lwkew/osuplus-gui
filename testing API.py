import requests
import json
percent = 97
rating = 5.5
json_data = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&s=600702').json()
newrating = 5.6
#abc=[]

req5 = requests.get('https://osu.ppy.sh/api/get_user_recent?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&type=string&u=lwke&limit=2').json()
# print(req5)


req1 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=2&mods=64&mode=0')
tester = req1.json()
#print (tester)


req2 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&s=600702').json()
print(req2)

with open('data.json', 'w+') as f:
    
    f.write(json.dumps(json_data))


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