import glob
import pickle
from music21 import converter, instrument, note, chord

""" 
beat를 기준으로, beat =1이 될 때 마다 새로운 마디를 생성하였음 
1마디의 구성은 [offset(악보 상의 위치), 음표의 숫자 표현(G4=60) / 쉼표의 경우 '^'으로 표현]
1마디의 생성은 beat값 1을 기준으로 했지만, 이를 오프셋으로 표현하는 것이 해석하기가 편리한 것 같아서, 
beat 정보는 생략하고 오프셋만 표현하였음. 시작 offset 0.0 -> 4.0 -> 8.0 -> ...
"""

def get_notes():
    list_all = []   # 전체 곡에 대한 리스트 처리용 빈 리스트 생성
    for file in glob.glob("melody/*.mid"):
        midi = converter.parse(file)
        notes_to_parse = midi.recurse()
        notes_one = ""   # 1곡에 대한 처리용 빈 문자열 생성

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                measure_str1 = str(element.offset)+' '+str(element.pitch.midi)+' '
                if element.beat == 1: 
                    notes_one += "\n"
                notes_one += measure_str1
            elif isinstance(element, note.Rest):
                measure_str2 = str(element.offset)+' '+"^"+' '
                if element.beat == 1:
                    notes_one += "\n"
                notes_one += measure_str2 

        tmp = notes_one.split('\n')

        list_one = [] # 1곡에 대한 list 처리
        for data in tmp:
            if data == '':
                continue        
            list_one.append(data)
        if len(list_one) != 0: # 비어있는 list 제거
            list_all.append(list_one) # 전곡에 대한 list 처리

    # pickle 파일 형태로 저장하기    
    with open('list_all.pkl', 'wb') as f:
        pickle.dump(list_all, f)

if __name__ == '__main__':
    get_notes()