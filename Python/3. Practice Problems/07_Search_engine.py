# Practice Problem 7 - Search Engine
import re


def matchingWords(word, sentence):
    match = re.findall(word, sentence, flags=re.IGNORECASE)
    return len(match)


if __name__ == '__main__':
    # customisable input
    sentences = ["This is good", "Python is good", "Python is not python snake"]

    query = input("Please input your query string:\n")
    query_lst = re.split(r"\s+", query)

    # maintaining a dictionary of search result
    search_result = {}

    for index, sentence in enumerate(sentences):
        match_count = 0
        for word in query_lst:
            if word != "":
                match_count += matchingWords(word, sentence)
        if match_count != 0:
            search_result[index] = match_count

    sorted_lst = sorted(search_result.items(), reverse=True)
    print(f"{len(sorted_lst)} results found!")
    for index, score in sorted_lst:
        print(f"\"{sentences[index]}\": with a score of {score}")
