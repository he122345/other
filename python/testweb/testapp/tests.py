students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 98, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 47, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 89, 'tel': '1388888888', 'gender': 'unknown'}]
count = 0
for x in students:
    if x['score'] < 60:
        count += 1
print("不及格学生的个数:", count)
print("不及格学生的名字和对应的成绩:", end="")
for x in students:
    if x['score'] < 60:
        print(x['name'], x['score'], end=",")
print()
count = 0
for x in students:
    if x['age'] < 18:
        count += 1
print("未成年学生的个数:", count)
print("手机尾号是8的学生的名字:", end="")
for x in students:
    if int(x['tel'][-1]) == 8:
        print(x['name'], end=",")
print()
m = 0
print("最高分和对应的学生的名字:", end="")
for x in students:
    if m < x['score']:
        m = x['score']
for x in students:
    if m == x['score']:
        print(x['name'], x['score'], end=",")
print()
for x in students:
    if x['gender'] == "unknown":
        students.remove(x)
print("删除性别不明的所有学生:")
for x in students:
    print(x)
s=sorted(students, key=lambda x: x['score'], reverse=True)
print("将列表按学生成绩从大到小排序:")
for x in s:
    print(x)