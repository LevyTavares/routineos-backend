import hashlib
import bcrypt


def _normalize_password(password: str) -> str:
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def hash_password(password: str) -> str:

    normalized_password = (
        _normalize_password(password)
        .encode("utf-8")
    )

    return bcrypt.hashpw(
        normalized_password,
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(
    password: str,
    hashed_password: str
) -> bool:

    hashed_bytes = (
        hashed_password.encode("utf-8")
    )

    for candidate_password in (
        _normalize_password(password),
        password
    ):

        try:

            if bcrypt.checkpw(
                candidate_password.encode("utf-8"),
                hashed_bytes
            ):

                return True

        except (TypeError, ValueError):

            continue

    return False