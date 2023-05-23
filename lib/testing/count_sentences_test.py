#!/usr/bin/env python3
import pytest
import io
import sys
from count_sentences import MyString

class TestMyString:
    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString("test value")
        assert isinstance(string, MyString)

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString("123")
        sys.stdout = sys.__stdout__
        expected_error = "The value must be a string."
        assert string.is_string() == expected_error

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        empty_string = MyString("")
        assert simple_string.count_sentences() == 3
        assert empty_string.count_sentences() == 0

if __name__ == '__main__':
    pytest.main()
