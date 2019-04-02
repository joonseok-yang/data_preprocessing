from statistics import mean, median, stdev

data = [(10, 20), (30, 80), (50, 60)]   # (kor, eng) scores
data1 = [{'kor': 70, 'eng': 90}, {'kor': 50, 'eng': 40}]

f = filter(lambda v: v[0] >= 30, data)
print(list(f))

f = filter(lambda v: v.get('kor') >= 60, data1)
print(list(f))

print(max(data, key=lambda v: v[0]))
print(max(data1, key=lambda v: v['eng']))

print(list(map(lambda v: v[0] + 2, data)))


rst = sorted(data1, key=lambda v: v['kor'], reverse=True)
print(rst)

print(sum([score[0] for score in data]))
print(sum([score.get('kor') for score in data1]))
print(sum([score['kor'] for score in data1]))
print(sum([score[0] for score in data]))


print("mean")
print(mean([10, 20, 30]))
print(mean([score[0] for score in data]))

print("median")
print(median([10, 20, 30]))
print(median([score[0] for score in data]))

print("stdev")
print(stdev([10, 20, 30]))
print(stdev([score[1] for score in data]))
