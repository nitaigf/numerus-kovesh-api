import unicodedata


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    uppercase = ascii_text.upper()
    return "".join(char for char in uppercase if "A" <= char <= "Z")