"""Tests for cipi.py text utilities."""

from collections import Counter

from cipi import char_count, sentence_count, summarise, word_count, word_frequency


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("  leading and trailing  ") == 3
    assert word_count("") == 0


def test_char_count():
    assert char_count("hello") == 5
    assert char_count("hi there", include_spaces=False) == 7
    assert char_count("hi there", include_spaces=True) == 8


def test_sentence_count():
    assert sentence_count("Hello. World!") == 2
    assert sentence_count("One sentence") == 1
    assert sentence_count("A? B! C.") == 3


def test_word_frequency_basic():
    freq = word_frequency("the cat sat on the mat")
    assert isinstance(freq, Counter)
    assert freq["the"] == 2
    assert freq["cat"] == 1


def test_word_frequency_ignores_punctuation():
    freq = word_frequency("Hello, hello! HELLO.")
    assert freq["hello"] == 3


def test_word_frequency_empty():
    assert word_frequency("") == Counter()


def test_summarise_keys():
    stats = summarise("The quick brown fox.")
    assert "words" in stats
    assert "unique_words" in stats
    assert "top_5_words" in stats


def test_summarise_top_words():
    stats = summarise("a a a b b c")
    top = dict(stats["top_5_words"])
    assert top["a"] == 3
    assert top["b"] == 2
