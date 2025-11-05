import re

text = open("text.txt","r").read()
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result_cleaned = []
list_tokens_no_duplicates = []
list_token_duplicates = []
list_next = []
list_probabilities = []

n = 0
b = 0

for i in range(len(result) - n):
    if result[i] != " " and result[i] != "":
        result_cleaned.append(result[i])

result_cleaned_no_duplicates = list(dict.fromkeys(result_cleaned))

for i in range(len(result_cleaned_no_duplicates)):
    list_tokens_no_duplicates.append(i)

for i in range(len(result_cleaned)):
    for j in range(len(result_cleaned_no_duplicates)):
        if result_cleaned[i] == result_cleaned_no_duplicates[j]:
            list_token_duplicates.append(list_tokens_no_duplicates[j])

print(list_token_duplicates)
input_1 = input("Enter the text: ")

for i in range(len(result_cleaned)):
    if input_1 == result_cleaned[i]:
        list_next.append(result_cleaned[i + 1])
    if input_1 in result_cleaned:
        b = 1
    if input_1 != result_cleaned[i] and b == 0:
        print("word not in para")

list_next_no_duplicates = list(dict.fromkeys(list_next))

for i in range(len(list_next_no_duplicates)):
    list_probabilities.append((list_next.count(list_next_no_duplicates[i])/len(list_next)))
try:
    majority = max(list_next, key=list_next.count)
    print(f"The next word is : {majority}")
except ValueError:
    pass


