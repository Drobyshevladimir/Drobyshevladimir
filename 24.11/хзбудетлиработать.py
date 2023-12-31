class Atbash:
        alphabet =  "эцгщбжюояшсчзайпимтехьлрнвыёфкдъу"
        alphabet2 = "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё"
        def __init__(self):
            lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet2)}
            uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet2)}
            self._encode = lowercase_code
            self._encode.update(uppercase_code)

        def encode(self, text):
            return ''.join([self._encode.get(char, char) for char in text])


cipher = Atbash()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()
        
