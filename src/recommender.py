from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    print(f"Loading songs from {csv_path}...")

    # Step 1: Open the CSV file so Python can read it line by line
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:

        # Step 2: Use DictReader so each row becomes a dictionary
        # where the keys are the column headers (id, title, genre, etc.)
        reader = csv.DictReader(f)

        for row in reader:
            # Step 3: Convert numeric fields from strings to numbers
            # so we can do math on them later (e.g. subtract energy values)
            row["id"]           = int(row["id"])
            row["energy"]       = float(row["energy"])
            row["tempo_bpm"]    = float(row["tempo_bpm"])
            row["valence"]      = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            # Step 4: Add the cleaned-up song dictionary to our list
            songs.append(row)

    # Step 5: Return the full list — each item is one song as a dictionary
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # Start with a blank slate — no points, no reasons yet
    score = 0.0
    reasons = []

    # --- TIER 1: Genre match (+4) ---
    # Genre is the most important signal — a genre match alone outweighs
    # any other single feature.
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 4.0
        reasons.append(f"genre match (+4.0)")

    # --- TIER 2: Mood match (+2) ---
    # Mood is the second most important signal. A song that fits the user's
    # current vibe gets a solid bonus, just slightly below genre.
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 2.0
        reasons.append(f"mood match (+2.0)")

    # --- TIER 3: Energy proximity (up to +2) ---
    # Energy is the third priority — a perfect match gives +2, which is
    # less than both genre and mood so it never overrides them.
    energy_diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = round((1 - energy_diff) * 2, 2)
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score})")

    # --- TIER 4: Acousticness match (+2 or +1) ---
    # We check whether the song's acoustic quality matches the user's preference.
    # Acoustic lovers get a bigger reward (+2) than non-acoustic users (+1)
    # because acousticness is a stronger differentiator in our catalog.
    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.6:
        score += 2.0
        reasons.append("acousticness match (+2.0)")
    elif not user_prefs["likes_acoustic"] and song["acousticness"] < 0.4:
        score += 1.0
        reasons.append("low acousticness match (+1.0)")

    # --- TIER 5: Valence bonus (optional, up to +0.5) ---
    # A small bonus for songs with a positive, uplifting feel (valence > 0.7).
    # This is a tiebreaker — it nudges scores slightly without dominating.
    if song["valence"] > 0.7:
        score += 0.5
        reasons.append("positive valence (+0.5)")

    # Return the final score and the list of reasons that explain it
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Step 1: Score every song in the catalog against the user's profile.
    # We use a list comprehension — the most Pythonic way to transform a list
    # into a new list. For each song, score_song() returns (score, reasons),
    # and we immediately join the reasons into a single explanation string.
    scored = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    # Step 2: Sort all scored songs from highest to lowest score.
    # key=lambda x: x[1] tells Python to sort by the score (index 1 of each tuple).
    # reverse=True flips the default ascending order to descending.
    scored.sort(key=lambda x: x[1], reverse=True)

    # Step 3: Slice the top K results and return them.
    # This is what the user will actually see as their recommendations.
    return scored[:k]
