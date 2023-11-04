import csv

# 教科の対応付け
subject_mapping = {
    '1': '国語',
    '2': '数学',
    '3': '理科',
    '4': '社会',
    '5': '英語',
}

# 生徒ごとのデータを格納する辞書
student_data = {}

# 入力CSVファイルの読み込み
with open('input_12.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name, subject, score = row
        if name not in student_data:
            student_data[name] = {}
        if subject not in student_data[name]:
            student_data[name][subject] = []
        student_data[name][subject].append(int(score))

# 通知簿CSVファイルの出力
for name, subjects in student_data.items():
    with open(f'生徒{name[-1]}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # ヘッダ行を出力
        header = ['教科', '平均点', '順位', '成績', '判定']
        writer.writerow(header)
        
        for subject, scores in subjects.items():
            # 平均点を計算
            average_score = round(sum(scores) / len(scores), 1)
            
            # 順位を計算
            rank = sorted(student_data.keys(), key=lambda x: -sum(student_data[x][subject]))\
                .index(name) + 1
            
            # 成績を計算
            if rank == 1:
                grade = 'A'
            elif rank <= 3:
                grade = 'B'
            elif rank <= 7:
                grade = 'C'
            elif rank <= 9:
                grade = 'D'
            else:
                grade = 'E'
            
            # 判定を計算
            if min(scores) < 11 or scores.count(30) >= 3:
                judgment = '不合格'
            elif grade == 'D':
                judgment = '再テスト'
            else:
                judgment = '合格'
            
            row = [subject_mapping[subject], average_score, rank, grade, judgment]
            writer.writerow(row)