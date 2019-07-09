import argparse
import re
import collections


def read_word_file(file_name):
    """
    Takes a text file and returns a list of strings with each word as one segment
    :param file_name: the name of the file to part out word by word
    :return: a list of the words in the file
    """
    words = []

    with open(file_name) as file:
        for line in file:
            for word in re.findall(r'\w[^\d\W]+\b', line):
                words.append(word)

    return words


def sort_list_and_change_case(incoming_list):
    """
    Takes a list of strings (words) and changes the case to all lower and sorts alphabetically
    If you want case-sensitive sorting (Alice != alice) remove the first line
    :param incoming_list: the list of words to sort and make all lowercase
    :return: a list of alphabetically sorted strings (words) in all lower-case
    """
    incoming_list = [item.lower() for item in incoming_list]
    incoming_list.sort()

    return incoming_list


def get_tuple_of_uncommon_words(common_words_list, text_list):
    """
    Remove the common strings (words) from the text list and return the results as a tuple
    :param common_words_list: the list of strings (words) that are 'common'
    :param text_list: the list of strings (words) that is the main text
    :return: a tuple of the strings (words)
    """
    uncommon_words_list = [x for x in text_list if not x in common_words_list]

    return tuple(uncommon_words_list)


parser = argparse.ArgumentParser(description='Read a txt file, remove all words from common words file and output the \
remaining word count descending')
parser.add_argument('common_words_filename', type=str, help='The input common words file')
parser.add_argument('text_filename', type=str, help='The input text file')
args = parser.parse_args()

common_words = read_word_file(args.common_words_filename)
text_words = read_word_file(args.text_filename)

common_words = sort_list_and_change_case(common_words)
text_words = sort_list_and_change_case(text_words)

uncommon_words_tuple = get_tuple_of_uncommon_words(common_words, text_words)

unique_words = sorted(set(uncommon_words_tuple for uncommon_words_tuple in uncommon_words_tuple))

final_word_dict = {}

for word in unique_words:
    final_word_dict[word] = uncommon_words_tuple.count(word)

final_word_dict = collections.OrderedDict(final_word_dict.items())

for w in sorted(final_word_dict, key=final_word_dict.get, reverse=True):
    print('{:{width}}'.format(w, width='15'), final_word_dict[w])
