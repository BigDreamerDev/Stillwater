








from __future__ import annotations

import getpass
import hashlib
import hmac

from stillwater._internal.ranks import RANKS
from stillwater.handbook import RESTRICTED_RANK_INDEX




_REQUIRED_RANK = RANKS[RESTRICTED_RANK_INDEX]




_COMSHELL_PASSWORD_SALT = "stillwater-comshell-v1:476936445d08bda7"
_COMSHELL_PASSWORD_ITERATIONS = 210000
_COMSHELL_PASSWORD_HASH = "b73ccefad193e50173cc43f5f01d18620a68e341ddef3d72e59ddec5099863ba"


def _derive_comshell_hash(submitted: str) -> str:

    normalized = (submitted or "").strip().encode("utf-8")
    salt = _COMSHELL_PASSWORD_SALT.encode("utf-8")
    return hashlib.pbkdf2_hmac(
        "sha256",
        normalized,
        salt,
        _COMSHELL_PASSWORD_ITERATIONS,
    ).hex()


def verify_comshell_password(submitted: str) -> bool:

    if not submitted:
        return False
    return hmac.compare_digest(_derive_comshell_hash(submitted), _COMSHELL_PASSWORD_HASH)


def require_comshell_password(max_attempts: int = 3) -> bool:

    print("comShell access requires operator verification.")

    for attempt in range(1, max_attempts + 1):
        try:
            submitted = getpass.getpass("operator phrase: ")
        except Exception:
            
            submitted = input("operator phrase: ")

        if verify_comshell_password(submitted):
            print("verification accepted.")
            return True

        remaining = max_attempts - attempt
        if remaining:
            print(f"verification failed. {remaining} attempt(s) remaining.")
        else:
            print("verification failed.")

    print("comShell access denied.")
    return False


def verify(submitted: str) -> bool:




    if not submitted:
        return False
    return submitted.strip().lower() == _REQUIRED_RANK.lower()


def required_rank() -> str:

    return _REQUIRED_RANK
