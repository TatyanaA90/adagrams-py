import pytest

from adagrams.game import  get_highest_word_score

def test_check_if_tuple_has_returned():
    # Arrange
    words = ["WWW"]

    # Act
    result = get_highest_word_score(words)

    # Assert
    assert type(result) == tuple
   # assert best_word[1] == 18
