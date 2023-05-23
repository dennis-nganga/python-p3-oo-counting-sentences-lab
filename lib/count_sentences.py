#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        sentences = self.value.split(".")
        return len(sentences)

    def is_string(self):
        if not isinstance(self.value, str):
            return "The value must be a string."
        return ""

