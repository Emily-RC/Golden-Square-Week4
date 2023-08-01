class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i += 1
        return self.text
    
remover = VowelRemover("aiaiaiai")
print(remover.remove_vowels())

# Because we have removed the first letter "a" we are then +1 
# and it goes to i as it skips over e, it doesn't take into account
# a new index as e will now be index [0], and i will be aadding 1
