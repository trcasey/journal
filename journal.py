"""
This is the journal module.
"""

import os

def load(name):
    """
    This method creates and loads a new journal.

    :param name: This is base name of the journal to load.
    :return: A new journal data structure populated with the file data
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves a new journal entry.

    :param name: This is the base name of the journal to load.
    :param journal_data: This is the actual content of the journal entry.
    :return:
    """
    filename = get_full_pathname(name)
    print("...saving to: {}".format(filename))


    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    This method gets the full pathname for the journal file.

    :param name: This is the base name of the journal to load.
    :return: The full path to the journal file.
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename

def add_entry(text, journal_data):
    """
    This method adds a new entry to the journal file.

    :param text: This is the base name of the journal to load.
    :param journal_data: This is the actual content of the journal entry to add to the file.
    :return:
    """
    journal_data.append(text)