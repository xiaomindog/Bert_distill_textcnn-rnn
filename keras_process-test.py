# import jieba
# from keras.preprocessing import *
#
# texts = [' '.join(jieba.cut(line.split('\t', 1)[1].strip())) \
#          for line in open('data/{}/{}.txt'.format('hotel', 'hotel'), encoding="utf-8",
#                           ).read().strip().split('\n')]
#
# tokenizer = text.Tokenizer()
#
# tokenizer.fit_on_texts(texts)
# print(tokenizer.word_counts)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a,b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in dict(fab(5)):
    print(n)
for n in fab(5):
    print(n)
