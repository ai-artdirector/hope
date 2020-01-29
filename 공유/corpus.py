import pickle

"""
corpus : 미디 파일 전체의 각 마디를 곡 순서 대로 word_to_id를 사용하여 단어 id로 만들어 놓은 list 데이터
"""
def create_corpus():
    with open('word_to_id.pkl','rb') as f:
        word_to_id = pickle.load(f)
    # corpus 생성    
    corpus = [word_to_id[w] for w in vocab]

    # pickle 파일 형태로 corpus 저장하기, file path는 각자의 경로에 맞게 설정
    with open('corpus.pkl', 'wb') as f:
        pickle.dump(corpus, f)

    return corpus

if __name__ == '__main__':
    create_corpus()