import requests

percent = 97
rating = 5.5

newrating = 5.6



req1 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=2&mods=64&mode=0')
tester = req1.json()
#print (tester)


req2 = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=1&s=600702')
tester1= req2.json()
#print(tester1)

APIRecommend = requests.get('https://osu.ppy.sh/api/get_beatmaps?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=2')
abc = APIRecommend.json()
print (abc)

# for i in abc:
#     print (i)
#     print ('AAAAAAAAAAAAAAA')

# for i in tester:
#     if i['difficultyrating'] > newrating:
#         print('yes')