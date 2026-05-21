#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import random
import re
import zlib
from typing import Any

_KEY = [83, 87, 45, 67, 79, 68, 73, 67, 79, 76, 79, 71, 89, 45, 86, 69, 75, 45, 49, 52]
_PAYLOAD = 'D~+HPgf^0UU$EM4#0azVOmc&U7m)FrE6(k%0(D_f9dC4#UyU?$Y<;-wha;sdqq3N>+4-HyZ#p>e(7(j0rlp<&Ciqz5MloB7DU5qvMIHK)Wou&ORpkV(Cvy0~A?uWFUePX;fxFuxFfJpKQE&$_WSEviynnhGR;dNxrc&UCvZ;|ls>zF`4Yie#k=}@sx-8X+yF@J0HPwBi0ztBeoDEpyMgi#pB{Vl8QO%)k1M4gYHp{_mWZ<9aumjGgNs(@&9GBfRgg?2(#yUWi%l|^GE{<(^{yB*-t1kcuu4zUvzC|~wRo?(Q71&M3neki=rfFsXgH_}`_@9F=fYO8KI$HQNgs+ZDN`6$_sP)4f5`R=V*;tQt0)uec94HYIpXW;*CYQ_$uc%W}y`dZw@c&{XvT1}w>)|PqN1C32oZlwyO}8pq_K7ypID}W(1VZ}Wpc2|)TqW~;f~MV8nRgw?FK=7-O&0#sz2HX*Jyeu(I-cTMysUL@6-V{o9Nprtqnkq=Ki{z0bC5_JbbrowxQzOLr|dY<@8eFXm@=_C_8S$aXgyR@^dpVN-qZbkCAaBnd;+b)SPi%x5Xr4k3p2iFaNk{$o?FsSE1wtN+@L^SCpf`NfMxDz9KG}dit${y&m_GJ1j6iF$F%Z>i+nd!&sH+V&_ePl^S^TzM-jlq(<LH4*$T)20z9rr^|cw{bNPYgUeN&c)_f4wFKa-hfG!ydt)NOn$m~l_A_C3SzZe6WEM2sexMV*;j(&j=Do(gPEGA%-HOGQD3A4#^rLTX>Qos(xMU2HE;9L)C?Wh`6T8y`rS+FR>n);kc+NN770{=hTpi2mlj;_-!*NOWqNY^!s={wQL<yVnQ_9~Rqey-F7mvI0IVq8zfw+l-1d`mb>36*oum$FPsmx-(HS87Aqw~bLtD+nAm`I|?#=>!+fD^u-J@<X;RU~pV6RqP<80ggG_sI_qa_5aOm-y?U3x(*Q#PVOIpk;&Ka_;Je%LAR7;9aa*kNO832wWa%%&}hGf;;yj`NT;K7Y#g@EW_R*i85duyxK>}kqAfC>yKn@sXQVRSKXg)tk~tJOw9p0oC!nt@6qi38;TUZP1lXaef}?XFHEWIPtj~NvUOmOb`0N26>mtP1=y_*}mF(u5Lsp&ef5EP|I$ROiI!qa_)(yBj>Huh-7Ur$NIZs1rziGy!tMA&snxT-E7#F&y+qJPJJ|v`RVcutmhAJ2pJ(&Z7P2xjG_A0S?G4<`jBM_3+vydUv=toqG0nUhx2E6SFO<}eqbCe}HdkQoV@>DOkXrA(R>~rw-6}SCTyeQ<*xIv?V3e6j!^am?F3&N<MS<_zw!cYMX_FX?}!b*xd+jnc)ehPMcPuPq`X9FjY`V59AYz?Eky8}ZHm`~NJT06W%ZX^7wms*ZnSJ?AJI_ed>)!Y;&MOo(-gDt7Pd(JBgi;b+OW70agk|;$lZr!}$pl{*=xxao3bM)*i2o?dH{ed6pBvuf(cI))R(&y^I-?AZ?HeUS8s1Uxrxc^j2l-^m=J93jgH2i02>vh$o6LPP@bWeS6C7=h6ly^}1nc|$@Q#da4ddR=~dI`HP#Y6GyaId8}(K+vI_H=LoY9mS(tFZb+OYL4H`?bZ6qkrp5q>I>kH2oEG`)+R+dLW25%49$+w(19aDbI#<;khnR(v%D<N0A$tlCG=K9f0Toi&S>5(6d9IR=DOCalqXj2zY}bR1C8Q+gi3l+=ZrN65=mY-Qcj(n>P{V&@llojbfQ)!6gkFF@F7TEtxuX5z3%0n*5*So|v+qtb)SfLJEkQBQUY>s5G~n>RD?1h2UpKmr7Jer33Vf$&tJ9Fp}i+cAwY~z2YEjSu<o|GgiA;TJC77&|vOb?W!V|XFBx'


def _decode_payload() -> dict[str, Any]:
    key = bytes(_KEY)
    blob = base64.b85decode(_PAYLOAD.encode("ascii"))
    clear = bytes(value ^ key[index % len(key)] for index, value in enumerate(blob))
    return json.loads(zlib.decompress(clear).decode("utf-8"))


def _normalise(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _has_all(answer: str, terms: list[str]) -> bool:
    normal = _normalise(answer)
    return all(_normalise(term) in normal for term in terms)


def _has_any(answer: str, terms: list[str]) -> bool:
    normal = _normalise(answer)
    return any(_normalise(term) in normal for term in terms)


def _check(answer: str, gate: dict[str, Any]) -> bool:
    mode = gate.get("mode")
    normal = _normalise(answer)

    if mode == "any":
        return _has_any(answer, gate["any"])

    if mode == "all_any":
        return _has_all(answer, gate["all"]) and _has_any(answer, gate["any"])

    if mode == "all_any_groups":
        return all(_has_any(answer, group) for group in gate["groups"])

    if mode == "choice_or_all":
        return normal in gate["choices"] or _has_all(answer, gate["all"])

    if mode == "choice_or_any":
        return normal in gate["choices"] or _has_any(answer, gate["any"])

    if mode == "code_or_all":
        code = normal.replace(" ", "-")
        return code in gate["codes"] or _has_all(answer, gate["all"])

    return False


def _pass_gate(number: int) -> None:
    print(random.choice([
        f"Gate {number:02d} accepted. The register does not object.",
        f"Gate {number:02d} accepted. Ink comparison stable.",
        f"Gate {number:02d} accepted. Codicology witness retained.",
    ]))


def _fail_gate(number: int) -> None:
    print()
    print(f"GATE {number:02d} REFUSED.")
    print(random.choice([
        "The register closes before the translation is complete.",
        "Codicology cannot certify that reading.",
        "The answer is close enough to be dangerous, but not close enough to file.",
        "The archive records effort. The archive does not record clearance.",
    ]))
    print("Verification terminated. Restart with `verify.senion` when ready.")


def run(args: list[str], session: dict[str, Any]) -> None:
    if args and args[0].lower() not in {"rosetta", "senion", "language", "register"}:
        print("usage: verify.senion")
        print("aliases: senion.verify, rosetta.verify, verify rosetta")
        return

    data = _decode_payload()

    for line in data["intro"]:
        print(line)
    print()

    for idx, gate in enumerate(data["gates"], start=1):
        print()
        print(f"GATE {idx:02d} // {gate['title']}")
        print("-" * 64)
        print(gate["prompt"])
        answer = input("translation> ")

        if not _check(answer, gate):
            _fail_gate(idx)
            return

        _pass_gate(idx)

    session["rank"] = "Codicology-Provisional"
    session["auth_level"] = max(session.get("auth_level", 0), 1)

    print()
    print("=" * 78)
    print(data["success"][0])
    print(data["success"][1])
    print(data["success"][2])
    print()
    print(data["success"][3])
    print(data["success"][4])
    print()
    print(f"    {data['contact']}")
    print()
    print(data["success"][5])
    print()
    print(f"    {data['subject']}")
    print()
    print(data["success"][6])
    print(data["success"][7])
    print("=" * 78)
