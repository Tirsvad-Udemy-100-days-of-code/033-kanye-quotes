from kanye_quotes import constants


def test_api_url_uses_https() -> None:
    assert constants.API_URL.startswith("https://")


def test_request_timeout_is_positive() -> None:
    assert constants.REQUEST_TIMEOUT_SECONDS > 0


def test_canvas_matches_background_image_size() -> None:
    assert (constants.CANVAS_WIDTH, constants.CANVAS_HEIGHT) == (300, 414)
