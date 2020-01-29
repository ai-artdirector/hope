from utils import *
import numpy as np
import pickle

def load_word_to_id(corpus_pkl_path):
    path = corpus_pkl_path
    word_to_id = create_word_to_id(path)
    return word_to_id

# 미디 파일 전체 리스트 불러오기, [[midi 1], [midi 2],...]]
def load_list_all(list_all_pkl_path):
    path = list_all_pkl_path
    with open(path,'rb') as f:
        list_all = pickle.load(f)
    return list_all

# 미디 파일 전체에 대한 '입력'과 '레이블'을 sequence_length를 이용해서 
# numpy ndarray 형식으로 생성한다  
def get_measure_id_sequence(word_to_id, list_all):
    sequence_length = 1  # inut과 label의 크기(길이)를 결정하는 요소
    word_to_id = word_to_id
    list_all = list_all
    input_seq_list = []
    label_seq_list = []
    for midi in list_all:
        print(len(midi))
        measure_id_seq = [] # 미디 파일 1개의 각 마디를 단어 id로 변환시킨 결과를 담을 list 생성
        for measure in midi:
            measure_id = word_to_id[measure]  # convert measure to id
            measure_id_seq.append(measure_id)
        # 미디 파일 1개에 대한 '입력'과 '레이블'을 numpy ndarray 형식으로 생성한다  
        input_id_seq = np.array(measure_id_seq)[:-sequence_length]
        label_id_seq = np.roll(np.array(measure_id_seq), -sequence_length)[:-sequence_length]

        print('input_id_seq', input_id_seq)
        print('label_id_seq', label_id_seq)

        # 미디 파일 전체에 대한 '입력'과 '레이블'을 numpy ndarray 형식으로 생성한다
        input_seq_list.append(input_id_seq)
        label_seq_list.append(label_id_seq)

    return input_seq_list, label_seq_list

if __name__ == '__main__':
    word_to_id = load_word_to_id('corpus.pkl')
    list_all = load_list_all('list_all.pkl')
    get_measure_id_sequence(word_to_id, list_all)