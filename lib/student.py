class Student:
    def hello(self, brief="Hey there! I'm so excited to learn stuff."):
        self.brief = brief
        print(self.brief)

    def raise_hand(self, attention="Pick me!"):
        self.attention = attention
        print(attention)

class ChattyStudent(Student):
    def hello(self,phrase="How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."): 
        
        self.phrase = phrase
        super().hello()
        print(self.phrase)

    def raise_hand(self):
        i = 0
        while i < 10:
            super().raise_hand()
            i+=1