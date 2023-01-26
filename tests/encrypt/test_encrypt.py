import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    POTATO = "potato"
    assert encrypt_message(POTATO, 2) == "otat_op"
    assert encrypt_message(POTATO, 4) == "ot_atop"
    assert encrypt_message(POTATO, 10) == "otatop"
    assert encrypt_message(POTATO, 3) == "top_ota"

    with pytest.raises(TypeError, match=r"tipo inválido para key"):
        encrypt_message(POTATO, "kiko?")

    with pytest.raises(TypeError, match=r"tipo inválido para message"):
        encrypt_message(55, 4)
