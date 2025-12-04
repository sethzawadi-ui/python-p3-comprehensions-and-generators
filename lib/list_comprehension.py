def return_evens(num_list):
    """Return a list of even numbers from num_list."""
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    """Add an exclamation mark to the end of each sentence in sentence_list."""
    return [sentence + "!" for sentence in sentence_list]
