"""Basic tests for the LLM subpackage."""

import pytest

from ditlab.llm.client_base import LLMClientBase


class TestClient(LLMClientBase):
    def __call__(self, prompt: str) -> str:
        return "{}"


def test_llm_client_base_instantiation() -> None:
    client = TestClient()
    assert callable(client)
    assert client("test") == "{}"


def test_llm_abstract_base() -> None:
    class Dummy(LLMClientBase):
        pass

    with pytest.raises(TypeError):
        Dummy()