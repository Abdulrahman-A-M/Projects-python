
with open('C:\\Program Files\\python\\Projects_python\\story.txt', 'r') as f:
        story = f.read()


words =set()

start_of_words=-1

target_start="<"
target_end=">"

for i,char in enumerate(story):
        if char == target_start:
                start_of_words=i
        
        if char == target_end and start_of_words !=-1:
                word=story[start_of_words:i+1]
                words.add(word)
                start_of_words=-1




answers={}

for word in words:

    answer=input('Enter a word'+word +': ')
    answers[word]=answer


for word in words:
       story=story.replace(word,answers[word])
print(story)
