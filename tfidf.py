import jieba,math

class TFIDF:

    def __init__(self, cors) -> None:
        self.length = 0
        self.d = len(list(cors))     #文档总数
        self.dic = {}
        self.cut = []
        self.tfidf = {}
        for i in cors:
            words = list(jieba.cut(i))
            self.cut.append(words)
            for word in words:
                self.length += len(list(words))
                if word not in self.dic:
                    self.dic[word] = 1
                else:
                    self.dic[word] += 1


    def TF(self, word):   #计算某词语TF值

        return self.dic[word]/self.length

    def IDF(self, word):  #计算某词语IDF值

        count = 1
        for i in self.cut:
            if word in i:
                count += 1
        return math.log(self.d/count)

    def TF_IDF(self, word):  #计算某个词语tfidf值
        return self.TF(word)*self.IDF(word)


    def all_tfidf(self):
        for i in self.dic.keys():
            self.tfidf[i] = self.TF_IDF(i)
        return self.tfidf




data = ['苹果是水果中的一种','水果是苹果','西瓜也是水果']

aa = TFIDF(data)