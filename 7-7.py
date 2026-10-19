scores = {
    "Kim": [80, 90, 70],
    "Lee": [100, 90, 85],
    "Park": [95, 85, 100]
}

# 학생별 평균 점수 계산 후 저장
averages = {}
for name, score_list in scores.items():
    avg = sum(score_list) / len(score_list)
    averages[name] = round(avg)  # 정수로 깔끔하게 출력되도록 round() 적용 (생략 가능)

print("averages =", averages)

# 평균 점수가 90점 이상인 학생
names = []
for name, avg in averages.items():
    if avg >= 90:
        names.append(name)

print("names =", names)