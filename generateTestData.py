import random

# Generate a series of morse code sentenses including some noise and varying bleep lengths 

morseTranslation = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    " ": "    "
}

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
lengthOfDataSet = 1
for i in range(lengthOfDataSet):
    sentenceLength = random.randint(3,10)
    minDotLength = random.randint(10,20)
    minDashLength = random.randint(minDotLength + 10,70)
    minSpaceLength = random.randint(20,80)
    sentence = ""
    morseSentence = ""
    for j in range(sentenceLength):
        letter = random.choice(letters)
        sentence += letter
        for c in morseTranslation[letter]:
            if c == "-":
                morseSentence += ("-" * int(minDashLength * (random.randrange(10,13)/10)))
            if c == ".":
                morseSentence += ("-" * int(minDotLength * (random.randrange(10,13)/10)))
            morseSentence += (" " * int(minSpaceLength * (random.randrange(10,13)/10)))
        morseSentence += (" " * int(minSpaceLength * (random.randrange(10,13)/10)))


print(sentence)
print(morseSentence)