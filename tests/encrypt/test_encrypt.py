from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Test", "Bad Call")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 5)

    assert encrypt_message("protect", 10) == "tcetorp"
    assert encrypt_message("protect", 2) == "tceto_rp"
    assert encrypt_message("protect", 3) == "orp_tcet"
