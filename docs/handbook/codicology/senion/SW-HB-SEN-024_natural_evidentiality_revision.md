# SW-HB-SEN-024 — Natural Evidentiality in Senionsoln

**Status:** Revision replacing the expanded ARG-instruction set  
**Purpose:** Make Senion feel like a real language later adopted by Stillwater  
**Instruction:** Keep the original four familiar particles, but reinterpret the system naturalistically.

---

## 1. Design change

The earlier expanded list made evidentials behave too much like puzzle instructions.

This revision makes Senion feel more like an inherited language: evidentials are normal grammar, used in everyday statements to mark how the speaker knows something.

Stillwater did not invent this system.

Stillwater adopted the language because the language already cared about source, witness, report, assumption, and record.

That is why the Foundation liked it.

---

## 2. Naturalistic evidential set

Senion now has seven normal evidentials.

| Particle | Class | Meaning |
|---|---|---|
| `-nai` | direct visual / witnessed | speaker saw or directly witnessed it |
| `-nal` | non-visual sensory | speaker heard, felt, smelled, or otherwise sensed it |
| `-thur` | inferential | speaker inferred it from evidence |
| `-mar` | assumptive | speaker assumes it from habit, expectation, or general knowledge |
| `-kel` | reportative / hearsay | someone told the speaker, or it was generally reported |
| `-sai` | quotative | speaker preserves someone’s exact wording |
| `-seln` | written / recorded source | speaker knows it from writing, inscription, register, or record |

This is the full normal-language system.

Do not add particles for file paths, mirrors, loops, indexes, etc. Those are Stillwater interpretations, not native grammar.

---

## 3. Why this feels like a real language

Many natural evidential systems distinguish direct evidence from indirect evidence; typological surveys also distinguish categories such as visual, non-visual sensory, inferential, assumptive, reportative/hearsay, and quotative evidence.

Senion’s system fits that kind of natural pattern:

```txt
direct evidence:
    -nai   seen/witnessed
    -nal   heard/felt/sensed

reasoned evidence:
    -thur  inferred from evidence
    -mar   assumed from expectation/general knowledge

social evidence:
    -kel   reported/hearsay
    -sai   directly quoted

textual evidence:
    -seln  written/recorded source
```

The only slightly unusual part is `-seln`, the written-source evidential. That is the one Stillwater bureaucratises.

---

## 4. Stillwater adoption

Native Senion:

```txt
Kor morh-ren-seln.
The door opened, according to the record.
```

Stillwater usage:

```txt
Kor morh-ren-seln.
The door opened, according to authorised documentation.
```

Over time, Stillwater staff begin treating `-seln` as more trustworthy than `-nai`, even though the original language only marks source, not truth.

That distinction matters:

```txt
Kor morh-ren-nai.
The door opened. I saw it.

Kor morh-ren-seln.
The door opened. The record says so.
```

Both can be true.

Both can be false.

The evidential only says where the claim came from.

---

## 5. Examples

### Visual / witnessed: `-nai`

```txt
Ya osh-ren kor-nai.
I saw the door.
```

Literal:

```txt
I witness-past door-[seen].
```

### Non-visual sensory: `-nal`

```txt
Ya nal-ren sūn-nal.
I heard the sound.
```

Literal:

```txt
I hear-past sound-[heard].
```

### Inferred: `-thur`

```txt
Kor morh-ren-thur.
The door opened, apparently.
```

Use this when the speaker sees marks, consequences, or traces but not the event itself.

### Assumed: `-mar`

```txt
Torhul morh-thel-mar.
The office will open, as usual.
```

Use this for expectation or ordinary routine.

### Reported / hearsay: `-kel`

```txt
Kor morh-ren-kel.
The door opened, I’m told.
```

Use this when the speaker heard it from another person or general report.

### Quotative: `-sai`

```txt
“Kor morh-ren,” ye kelh-ren-sai.
“The door opened,” they said.
```

Use this in interviews where exact wording matters.

### Written / recorded: `-seln`

```txt
Kor morh-ren-seln.
The door opened, according to the record.
```

Use this for registers, forms, inscriptions, handbooks, logs, and archive notes.

---

## 6. Interaction with `-vor`

Keep `-vor` as mood, not an evidential.

It means the clause is sealed/restricted.

Pattern:

```txt
verb + tense + -vor + evidential
```

Examples:

```txt
Kor morh-ren-vor-seln.
The door opened. [sealed; according to the record]
```

```txt
Sūn han-vor-nal.
There is a sound. [sealed; directly heard]
```

Do not use `-vor` as a final source marker.

Correct:

```txt
Kor han-vor-seln.
```

Wrong:

```txt
Kor han-vor.
```

---

## 7. Natural everyday usage

Senion speakers use evidentials constantly, not only for strange events.

```txt
Dā han-nai.
It is day. I see it.

Nold han-nal.
It is night. I sense/hear it.

Kar par-ren-kel.
The person left, I’m told.

Kar par-ren-thur.
The person left, apparently.

Kar par-thel-mar.
The person will leave, as expected.

Kar par-ren-sai.
“The person left,” someone said.

Kar par-ren-seln.
The person left, according to the record.
```

This makes Senion feel lived-in.

Stillwater’s horror comes from the bureaucracy misusing normal grammar.

---

## 8. Updated writer rule

Use only these seven evidentials in normal Senion:

```txt
-nai
-nal
-thur
-mar
-kel
-sai
-seln
```

Use `-vor` only as sealed mood.

Avoid these older expanded evidentials unless you deliberately want them as later Foundation jargon:

```txt
-dakel
-ven
-tar
-mir
-ring
-un
```

Those are no longer native Senion. If kept, mark them as Stillwater bureaucratic slang or post-adoption technical extensions.

---

## 9. Best ARG use

For ordinary Senion texts, use natural evidentials.

For Stillwater documents, let staff overinterpret them.

Example native sentence:

```txt
Roseta han-seln.
Rosetta exists, according to a written source.
```

Stillwater note beside it:

```txt
-seln indicates admissible archival authority under Codicology handling rule 7.
```

That makes the Foundation feel like it adopted a real language, then made it worse.
