import json



f = open('followers_1.json')
followers = json.load(f)
f.close()
e = open('following.json')
following = json.load(e)
e.close()
followinglist = []
followerlist = []


for x in following["relationships_following"]:
    username = x["string_list_data"][0]["value"]
    followinglist.append(username)

for y in followers:
    username = y["string_list_data"][0]["value"]
    followerlist.append(username)


a = 0
for x in followinglist:
    if x not in followerlist:
        print(x)
        a+=1

print(a)













# get instagram follower count


