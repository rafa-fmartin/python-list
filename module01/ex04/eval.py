class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) == len(coefs):
            summ = 0
            for word, value in zip(words, coefs):
                summ += len(word)*value
            print(summ)
        else:
            print(-1)
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) == len(coefs):
            summ = 0
            for index, word in enumerate(words):
                summ += len(word)*coefs[index]
            print(summ)
        else:
            print(-1)
