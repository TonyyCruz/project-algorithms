import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    correct_word = "potato"
    assert encrypt_message(correct_word, 2) == "otat_op"
    assert encrypt_message(correct_word, 4) == "ot_atop"
    assert encrypt_message(correct_word, 10) == "otatop"
    assert encrypt_message(correct_word, 3) == "top_ota"

    with pytest.raises(TypeError, match=r"tipo inválido para key"):
        encrypt_message(correct_word, "kiko?")

    with pytest.raises(TypeError, match=r"tipo inválido para message"):
        encrypt_message(55, 4)
