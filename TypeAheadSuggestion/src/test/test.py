from TypeAheadSuggestion.src.main.trie import TypeAhead

if __name__ == '__main__':
    type_ahead = TypeAhead(10)
    type_ahead.add_word("The")
    type_ahead.add_word("The family", 5)
    type_ahead.add_word("The family man show")
    type_ahead.add_word("The family")
    type_ahead.add_word("The family man show")
    type_ahead.add_word("The Red")
    type_ahead.add_word("The Red Skull", 4)
    print(type_ahead.get_top_suggestion("T"))
    print(type_ahead.get_top_suggestion("The R"))
    print(type_ahead.get_top_suggestion("WW2"))