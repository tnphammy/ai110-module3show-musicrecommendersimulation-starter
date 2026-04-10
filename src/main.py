"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(user_prefs: dict, songs: list, label: str) -> None:
    """Helper that runs the recommender and prints results for one user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Print a header showing whose profile we're testing
    print("\n" + "=" * 55)
    print(f"  {label}")
    print(f"  Genre: {user_prefs['favorite_genre']}  |  Mood: {user_prefs['favorite_mood']}"
          f"  |  Energy: {user_prefs['target_energy']}  |  Acoustic: {user_prefs['likes_acoustic']}")
    print("=" * 55)

    # Loop through each recommended song and print its rank, title, score, and reasons
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score : {score:.2f}")
        print(f"    Why   : {explanation}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # --- Profile 1: Baseline (easy) ---
    # Genre, mood, and energy are all consistent. The algorithm should
    # confidently surface chill r&b songs near 0.70 energy.
    user_prefs_1 = {
        "favorite_genre": "r&b",
        "favorite_mood":  "chill",
        "target_energy":  0.70,
        "likes_acoustic": False,
    }

    # --- Profile 2: Mood vs. energy conflict (medium-hard) ---
    # The user loves blues and wants sad music, but cranks the energy to 0.90
    # and dislikes acoustic. The only blues/sad song in the catalog (Empty
    # Streets) is low-energy (0.31) and acoustic — a near-total mismatch on
    # two of four signals. Does the genre+mood double-match still win, or do
    # high-energy non-acoustic songs steal the top spots?
    user_prefs_2 = {
        "favorite_genre": "blues",
        "favorite_mood":  "sad",
        "target_energy":  0.90,
        "likes_acoustic": False,
    }

    # --- Profile 3: Genre isolated vs. everything else (hard) ---
    # The only hip-hop song (Basement Cypher) is energetic (0.85), not chill,
    # and not acoustic. Every other preference points toward lofi/ambient songs
    # that have zero genre overlap. The genre +3 bonus must fight against
    # mood + energy + acoustic bonuses stacking up on completely different songs.
    user_prefs_3 = {
        "favorite_genre": "hip-hop",
        "favorite_mood":  "chill",
        "target_energy":  0.30,
        "likes_acoustic": True,
    }

    # --- Profile 4: Four-way contradiction (hardest) ---
    # The only metal song (Iron Curtain) is angry (not romantic), slams at
    # 0.97 energy (target is 0.25), and has near-zero acousticness (0.06) while
    # the user loves acoustic. Every single scoring dimension pulls away from
    # the genre match. Ambient/classical songs that are chill, low-energy, and
    # highly acoustic will likely dominate — the genre +3 may not be enough.
    user_prefs_4 = {
        "favorite_genre": "metal",
        "favorite_mood":  "romantic",
        "target_energy":  0.25,
        "likes_acoustic": True,
    }

    # Run the recommender for each profile so we can compare outputs side by side
    print_recommendations(user_prefs_1, songs, "Profile 1 — Baseline (easy)")
    print_recommendations(user_prefs_2, songs, "Profile 2 — Mood vs. energy conflict (medium-hard)")
    print_recommendations(user_prefs_3, songs, "Profile 3 — Genre isolated vs. rest (hard)")
    print_recommendations(user_prefs_4, songs, "Profile 4 — Four-way contradiction (hardest)")


if __name__ == "__main__":
    main()
