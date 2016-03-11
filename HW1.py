f = open("a.txt", 'r')
lines = f.readlines()

total_count = 0
max_count = 0
max_line = 0
words = {}
for i, line in enumerate(lines, 1):
    now_count = line.count(' ') + 1
    total_count += now_count
    if( now_count > max_count ):
        max_count = now_count
        max_line = i

    w = line.split()
    for word in w:
        if not words in words:

    words = {() for word in w }


print("단어수 : %d" % total_count)
print("줄수 : %d" % len(lines))
print("가장 많이 쓰인 단어 : %d")
print("단어가 가장 많이 포함된 라인 : %d" % max_line)
print("단어가 가장 많이 포함된 라인의 단어 수 : %d" % max_count)