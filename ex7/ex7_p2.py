fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()   #strip는 문자열의 오른쪽 공백을 제거하는 메서드이다
    if line.startswith('From:'): #startswith는 찾고싶은 부분만 찾아 출력할 수 있도록 도와주는 메서드이다
        print(line)
