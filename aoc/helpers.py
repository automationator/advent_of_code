import os


def split_text_on_blank_lines(text: str) -> list[str]:
    """
    Split a string on blank lines.
    """
    return text.split(os.linesep + os.linesep)
