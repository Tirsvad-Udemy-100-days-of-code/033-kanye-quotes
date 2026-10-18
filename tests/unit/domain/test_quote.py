import dataclasses

import pytest

from kanye_quotes.domain.quote import Quote


@pytest.mark.parametrize("text", ["", " ", "\n\t "])
def test_quote_is_rejected_when_blank(text: str) -> None:
    with pytest.raises(ValueError):
        Quote(text)


def test_quote_keeps_text_when_valid() -> None:
    assert Quote("I am a god").text == "I am a god"


def test_quote_cannot_be_changed_after_creation() -> None:
    quote = Quote("I am a god")
    with pytest.raises(dataclasses.FrozenInstanceError):
        quote.text = "other"  # type: ignore[misc]
