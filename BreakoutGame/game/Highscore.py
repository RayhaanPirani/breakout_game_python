import fileinput, hashlib, operator

class Highscore:
    def __init__(self, ):
        self.__highscores = self.load()

    def get_scores(self):
        return self.__highscores

    def load(self):
        highscores = []
        for line in fileinput.input("highscore.dat"):
            name, score, md5 = line.split("::")
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name+score+"breakout"))).hexdigest()) == str(md5):
                highscores.append([str(name), int(score), str(md5)])

        highscores.sort(key=operator.itemgetter(1), reverse=True)
        highscores = highscores[0:11]
        return highscores

    def add(self, name, score):
        hash = hashlib.md5((str(name+str(score)+"breakout")).encode('utf-8'))
        self.__highscores.append([name, str(score), hash.hexdigest()])

        file = open("highscore.dat", 'w')
        for name, score, md5 in self.__highscores:
            file.write(str(name)+"::"+str(score)+"::"+str(md5)+"\n")
        file.close()