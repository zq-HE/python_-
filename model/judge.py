from model import getRank, getData3,getData
import getpath
# 获取数据
def judge(js):
    data = getData3.get(getpath.get_root_path()+'/data/data.json')
    person = getData.get(js)
    userId = person.loc[0, 'userId']
    data = data.append(person).reset_index(drop=True)
    totalRank = getRank.get(data)
    rank = totalRank[totalRank.userId == str(userId)].index[0]
    final_score = totalRank[totalRank.userId == str(userId)].loc[rank, 'final_score']
    return {'rank': rank + 1, 'personal_data': totalRank.loc[rank], 'final_score': final_score, 'totalRank': totalRank}
