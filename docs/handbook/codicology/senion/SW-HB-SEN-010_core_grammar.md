# SW-HB-SEN-010 — Core Grammar of Senionsoln

**Language:** Senionsoln / Pre-Threshold Tongue  
**Use:** Writer-facing guide for producing consistent Senion text.

---

## 1. Fixed Canon

Do not change these unless you want players to treat the change as a clue.

| Feature | Rule |
|---|---|
| Basic word order | Subject – Verb – Object |
| Prepositions | Senion uses postpositions after the noun |
| Articles | No equivalent of “a” or “the” |
| Plural | Usually unmarked; use `-lan` only where number matters |
| Tense | Verb root = present/habitual; `-ren` = past; `-thel` = future |
| Evidentiality | Every declarative clause must end in an evidential |
| Sealed mood | `-vor` attaches after tense and before the evidential |
| Topic | `-ha` marks the fronted topic: “as for X…” |

---

## 2. Word Order

Normal sentence:

```txt
Subject Verb Object-EVIDENTIAL
```

Example:

```txt
Ya osh kor-nai.
I witness door-[witnessed].
“I saw the door.”
```

If the sentence has no object:

```txt
Kor han-seln.
Door exists-[from record].
“The door exists / is open. [from the record]”
```

---

## 3. Postpositions

Postpositions attach to the noun phrase with a hyphen.

| English | Senion Pattern | Example |
|---|---|---|
| in X | X-eth | `arvel-eth` = in the archive |
| to/toward X | X-toh | `kor-toh` = to the door |
| from X | X-aru | `vehel-aru` = from the building |
| of X | X-en | `tier-en` = of the rank |
| under X | X-bel | `besh-bel` = under the floor |
| beside X | X-tor | `mir-tor` = beside the mirror |
| through X | X-mar | `vethr-mar` = through the passage |
| with X | X-dor | `kelh-dor` = with the record |
| without X | X-vesh | `sūn-vesh` = without sound |

Senion does not say “in the archive”; it says “archive-in”.

---

## 4. Evidentials

Every declarative clause ends with one of these.

| Particle | Meaning | Use |
|---|---|---|
| `-nai` | witnessed directly | speaker saw/experienced it |
| `-kel` | reported/heard | someone said it; unsealed report |
| `-thur` | inferred | deduced from circumstance |
| `-seln` | from record | handbook, register, official record |

Examples:

```txt
Kor han-nai.    The door exists. I saw it.
Kor han-kel.    The door exists. Someone reported it.
Kor han-thur.   The door exists. I infer it.
Kor han-seln.   The door exists. The record says so.
```

This is the main ARG grammar feature. It tells players what kind of clue they should trust.

---

## 5. Tense and Sealed Mood

Tense attaches to the verb before any mood/evidential ending.

| Form | Meaning |
|---|---|
| `han` | is / exists |
| `han-ren` | was / existed |
| `han-thel` | will be / will exist |

`-vor` means the clause is restricted or sealed. It comes after tense, before evidential.

```txt
Kor han-vor-seln.
The door exists / is open. [sealed; from record]

Arvel morh-ren-vor-kel.
The archive opened. [sealed; reported]
```

Use `-vor` rarely. It should feel important.

---

## 6. Topic Marker

`-ha` means “as for / regarding”.

```txt
Kor-ha, vehel-eth han-nai.
As for the door, it is in the building. [witnessed]
```

---

## 7. Plurals

Leave number unmarked unless needed.

```txt
kor = door / doors
korlan = doors specifically
thren korlan = three doors
```

---

## 8. Derivation

| Suffix | Meaning | Example |
|---|---|---|
| `-er` | person/agent | `arveler` = archivist |
| `-ul` | place/site | `arvelul` = archive room |
| `-ith` | tool/instrument | `kelhith` = recording tool |
| `-veth` | state/condition | `selveth` = silence-condition |
| `-il` | adjective/related-to | `arvelil` = archival |
| `-om` | written item/document | `kelhom` = transcript/account document |

Avoid using `-en` as an adjective marker because it already means “of”.

---

## 9. Compounds

Senion compounds are usually head-final: the final root is the main thing.

```txt
halh + vehel = Halhvel
still-water + building = Stillwater Foundation

arvel + hand = arvelhand
archive + keeper = archive-keeper

morh + sūn + ul = morh-sūn-ul
opening + signal + place = switchboard
```

Use hyphens in long Foundation terms when clarity matters.

---

## 10. Questions and Negation

Add `ma` for questions.

```txt
Kor han ma?
Does the door exist?

Kor han-seln ma?
Does the record say the door exists?
```

Use `un-` for negation.

```txt
Kor unhan-thur.
The door does not exist. [inferred]

Unmal han-seln.
A not-room exists. [from record]
```

---

## 11. Safe Sentence Template

```txt
[Topic-ha,] Subject Verb[-tense][-vor] Object/Postpositional phrase-EVIDENTIAL.
```

If it gets too complex, split it into two shorter sentences.
