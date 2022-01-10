# 프로그래머스 코딩테스트 연습 레벨 2 방금그곡 
# 참고한 풀이 : https://json1995.tistory.com/entry/Python프로그래머스Level-2-방금그곡 (# 붙은 음 바꾸는 함수 만들기)

def solution(m, musicinfos):
    answer = ""
    melody = change(m)
    result = []
    
    for info in musicinfos:
        storage = list(info.split(","))
        dur = (int(storage[1][3:]) - int(storage[0][3:])) + (int(storage[1][:2]) - int(storage[0][:2]))*60
        
        storage[3] = change(storage[3])
        notes = list(storage[3])
        
        songnotes = ["H"] * dur
        for j in range(len(songnotes)):
            songnotes[j] = notes[j % len(notes)]
        
        song = "".join(songnotes)
        
        if melody in song:
            result.append([dur, storage[2]])
    
    container = []
    
    if not result:
        answer = "(None)"
    else:
        times = []
        for l in range(len(result)):
            times.append(result[l][0])
        for data in result:
            if data[0] == max(times):
                container.append(data[1])
        answer = container[0]
    
    return answer

def change(notes): # 풀이에서 참고한 부분 - 반음 올라간 음표의 문자열을 치환해 주는 함수
    if "C#" in notes: notes = notes.replace("C#", "c")
    if "D#" in notes: notes = notes.replace("D#", "d")
    if "F#" in notes: notes = notes.replace("F#", "f")
    if "G#" in notes: notes = notes.replace("G#", "g")
    if "A#" in notes: notes = notes.replace("A#", "a")
    return notes

# 원래 내가 짠 코드에서는, 리스트로 뿌려 주고 바로 뒤의 #을 자기한테 붙인 다음 모든 #을 제거하는 방법을 썼다.
# 잘 작동했지만, 문자열로 붙이면 의미가 없어질 게 뻔했고, 그래서 들은 멜로디도 리스트로 만들어 비교했다.
# 논리적으로는 잘 작동해야 말이 되지만, 이상하게 잘 안 됐던 걸 보면 아무튼 그 부분에 문제가 있긴 했던 모양.
# #이 붙은 음표를 소문자로 치환하고, 문자열끼리 직접 비교하니까 아무튼 오류가 나지 않았다.
# 또한 그것을 제외한 나머지 세부 조건은 잘 구현했다.

# 내가 짠 코드 - 실패한 테스트케이스 3, 4, 6, 8, 18, 19

"""
def solution(m, musicinfos):
    answer = ''
    
    heard = list(m)
    for n in range(len(heard)-1):
        if heard[n+1] == "#":
            heard[n] += "#"
    while "#" in heard:
        heard.remove("#")
    
    result = []
    
    for info in musicinfos:
        storage = list(info.split(","))
        dur = (int(storage[1][3:]) - int(storage[0][3:])) + (int(storage[1][:2]) - int(storage[0][:2]))*60
        
        notes = list(storage[3])
        for i in range(len(notes)-1):
            if notes[i+1] == "#":
                notes[i] += "#"
        while "#" in notes:
            notes.remove("#")
        
        song = ["H"] * dur
        for j in range(len(song)):
            song[j] = notes[j % len(notes)]
        
        if len(song) > len(heard):
            for k in range(len(song) - len(heard)):
                if song[k:k+len(heard)] == heard:
                    result.append([dur, storage[2]])
    
    container = []
    
    if not result:
        answer = "(None)"
    else:
        times = []
        for l in range(len(result)):
            times.append(result[l][0])
        for data in result:
            if data[0] == max(times):
                container.append(data[1])
        answer = container[0]
    
    return answer
"""