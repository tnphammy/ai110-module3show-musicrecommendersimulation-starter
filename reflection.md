# Reflection: How Different Users Got Different Results

## Profile 1 vs. Profile 4 — The clearest contrast

**Profile 1 (r&b, chill, energy 0.70, non-acoustic)** got results that made sense right away. The top song was the only r&b track in the catalog, and the rest of the list was filled with songs that felt smooth and mid-energy — soul, indie pop, synthwave. Nothing jarring. The preferences pointed in the same direction, so the algorithm had an easy job.

**Profile 4 (metal, romantic, energy 0.25, acoustic)** was almost the opposite. The only metal song in the catalog — Iron Curtain — is angry, slams at near-maximum energy, and is barely acoustic at all. Every single one of the user's preferences contradicted it. So even though the algorithm gave it a genre bonus, low-energy acoustic songs like Rainy Window and Spacewalk Thoughts scored higher overall by stacking up points everywhere else. The metal fan ended up with a playlist full of classical and ambient music — technically correct by the math, but probably not what they wanted to hear.

**What this tells us:** when a user's preferences all point in the same direction, the system works well. When the genre they love sounds nothing like how they described themselves (energy, mood, acoustic), the system gets confused and the genre bonus isn't always enough to save it.

---

## Profile 2 vs. Profile 3 — The mid-range cases

**Profile 2 (blues, sad, energy 0.90, non-acoustic)** wanted sad blues at high energy — but the only blues/sad song (Empty Streets) is quiet and acoustic. The genre+mood double match still pulled it into the top 3, but high-energy non-acoustic songs from other genres kept competing for the #1 spot. The right song was there, just not always winning.

**Profile 3 (hip-hop, chill, energy 0.30, acoustic)** is almost a personality contradiction — hip-hop listeners who want something chill, quiet, and acoustic. The one hip-hop song (Basement Cypher) is the opposite of all that. Lofi and ambient songs dominated the list because they matched mood, energy, and acousticness — even with zero genre overlap. The system basically gave up on genre and optimised for vibe instead.
