import glob
import pickle
from music21 import converter, instrument, note, chord
import numpy as np

""" 
함수에 필요한 미디 파일이나 피클 파일은 각자의 경로에 맞게 설정하십시오
예시) "melody/*.mid" --> 각자의 path
"""

def get_vocab():
    vocab = []   # 마디 전체를 담을 리스트 생성
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
        vocab += list_one 

    # 중복 제거 전 마디(단어) 전체의 크기 확인
    print("마디(단어) 전체의 크기 : {}".format(len(vocab)))

    # 중복 제거 작업
    vocab_remove = list(set(vocab))
    print("중복 제거 후 마디(단어)의 크기 : {}".format(len(tmp)))


    # pickle 파일 형태로 vocab 저장하기, file path는 각자의 경로에 맞게 설정
    with open('vocab.pkl', 'wb') as f:
        pickle.dump(vocab, f)

    # pickle 파일 형태로 vocab_remove 저장하기, file path는 각자의 경로에 맞게 설정
    with open('vocab_remove.pkl', 'wb') as f:
        pickle.dump(vocab_remove, f)

if __name__ == '__main__':
    get_vocab()