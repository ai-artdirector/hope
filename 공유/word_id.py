import pickle

def get_word_id():
    with open('vocab_remove.pkl','rb') as f:
        vocab_remove = pickle.load(f)

    print("데이터 불러오기가 끝났습니다.")

    # dict(사전) 생성 : key = 마디, value = id(인덱스)
    word_to_id = dict((w,i) for i, w in enumerate(vocab_remove))
    print("단어장의 크기 : {}".format(len(word_to_id)))

    # dict(사전) 생성 : key = id(인덱스), value = 마디
    id_to_word = dict((i, w) for i, w in enumerate(vocab_remove))
    print("단어장의 크기 : {}".format(len(word_to_id)))

    # pickle 파일 형태로 word_to_id 저장하기, file path는 각자의 경로에 맞게 설정
    with open('word_to_id.pkl', 'wb') as f:
        pickle.dump(word_to_id, f)   

    # pickle 파일 형태로 id_to_word 저장하기, file path는 각자의 경로에 맞게 설정
    with open('id_to_word.pkl', 'wb') as f:
        pickle.dump(id_to_word, f)  

    return word_to_id, id_to_word

if __name__ == '__main__':
    get_word_id()   