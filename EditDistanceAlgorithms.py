
def levenshtein_distance(str1,str2):
    len_str1=len(str1)+1
    len_str2=len(str2)+1
    matrix=[[0 for _ in range(len_str2)] for _ in range(len_str1)]

    for i in range(len_str1):
        matrix[i][0]=i
    for j in range(len_str2):
        matrix[0][j]=j

    for i in range(1,len_str1):
        for j in range(1,len_str2):
            cost=0 if str1[i-1]==str2[j-1] else 1
            matrix[i][j]=min(
                matrix[i-1][j]+1,
                matrix[i][j-1]+1,
                matrix[i-1][j-1]+cost
                )
    return matrix[len_str1-1][len_str2-1]
def suggest_correction(word,word_list):
    distances=[(w,levenshtein_distance(word,w))for w in word_list]
    distances.sort(key=lambda x:x[1])
    return distances[0][0]
input_word="creature"
dictionary=["nature","world","python","spell","correct","algorithm"]

suggested_correction=suggest_correction(input_word,dictionary)
print(f"Suggested Correction for '{input_word}': {suggested_correction}")

def retrieve_information(query, dictionary):
    query_words = query.split()
    corrected_words = [suggest_correction(word, dictionary) for word in query_words]
    corrected_query = ' '.join(corrected_words)
    print(f"Retrieving information for corrected query: '{corrected_query}'")
user_query = "speling correctin algorithm"
dictionary = ["creature", "correction", "algorithm", "information", "retrieval", "system"]
retrieve_information(user_query, dictionary)
