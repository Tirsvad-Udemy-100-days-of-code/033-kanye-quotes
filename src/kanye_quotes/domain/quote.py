"""@brief The Quote value object."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Quote:
    """@brief A sentence attributed to Kanye West.

    @param text The quote text; never blank.
    """

    text: str

    def __post_init__(self) -> None:
        """@brief Reject a blank quote.

        @throws ValueError When the text is empty or only whitespace.
        """
        if not self.text.strip():
            raise ValueError("A quote cannot be blank.")
