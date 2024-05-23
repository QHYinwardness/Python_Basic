import sys
import re
import collections

WORD_RE = re.compile(r"\w+")

# create a dict to save the location of every words
# key of dict will be the word
# value of the dict will be (line_no,column_no)
# line no from txt fp
# column from word index
index = collections.defaultdict(list)

with open("my_dic.txt", encoding="utf-8") as fp:
    for line_on, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_on, column_no)
            index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


# import sys
# import re

# WORD_RE = re.compile(r"\w+")

# # create a dict to save the location of every words
# # key of dict will be the word
# # value of the dict will be (line_no,column_no)
# # line no from txt fp
# # column from word index
# index = {}

# with open("my_dic.txt", encoding="utf-8") as fp:
#     for line_on, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_on, column_no)
#             # set word as the key of index if key not exist return []
#             # if the key be found add the location list into the dict as the key-value pair
#             index.setdefault(word, []).append(location)

#     for word in sorted(index, key=str.upper):
#         print(word, index[word])

#     # if the key didn't exist in the dict, we will also need a default which will be better than
#     # just raise an error message

#     # method one : return to the reference

#     import collections


# import sys
# import re

# WORD_RE = re.compile(r"\w+")

# index = collections.defaultdict()

# with open("my_dic.txt", encoding="utf-8") as fp:
#     for line_on, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_on, column_no)

#             # occurrences here are used to handle with if no keys in the dict
#             occurrences = index.get(word, [])
#             # add list value into the list
#             occurrences.append(location)
#             # add list value into dict
#             index[word] = occurrences
