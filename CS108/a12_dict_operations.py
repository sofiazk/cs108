# file: a12_dict_operations.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: 
    
def print_dict(d):
    '''Prints out all (key, value) pairs in the parameter d one per line,
    in ascending order by key'''
    # Fetch keys to a list
    keys_list = list(d.keys())
    keys_list.sort() # Sorting

    # iterate over sorted list and get values from dict
    for key in keys_list:
        print("%s : %s" %(key, d[key]))


def letter_counts(text):
    '''
    Method to count the number of occurrences of alphabets in string
    :param text: input string
    :return: dictionary
    '''
    # Initialise dict with all counts as 0
    d = {}
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabets:
        d[c] = 0

    # convert to lower
    text = text.lower()

    # Iterate over text and increment count
    for c in text:
        if c in d.keys():
            d[c] += 1
    return d


def letter_frequencies(text):
    '''
    Method to compute frequencied for each char in input text.
    :param text: input string
    :return: frequency dict
    '''
    # Get letter counts
    d = letter_counts(text)

    # Get total letters present
    total_letters = 0
    for key in d.keys():
        total_letters += d[key]

    # Iterate over dict and create a frequency
    # dict by dividing the count with total count.
    freq_dict = {}
    for key in d.keys():
        freq_dict[key] = float(d[key])/total_letters
    return freq_dict


if __name__ == '__main__':
    print(" === Test 1 ===")
    d1 = {'BU': 5, 'BC': 3, 'Harvard': 4, 'Northeastern': 1}  # alpha keys
    print_dict(d1)
    print("\n=== Test 2 ===")
    d2 = {8: 5, 2: 7, 3: 4, 9: 2, 5: 13}  # numeric keys
    print_dict(d2)
    print("\n\n=== Test 3 ===")
    d = letter_counts('testing 1 2 3!')
    print(d)  # show the contents of this dictionary
    print("\n\n==== Test 4 ====")
    d = letter_frequencies('hello, world')
    print(d)  # show the contents of this dictionary
