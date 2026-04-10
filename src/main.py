"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Sample user profile for testing
    user_prefs = {
        "favorite_genre": "r&b",
        "favorite_mood":  "chill",
        "target_energy":  0.70,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Print a header showing whose profile we're using
    print("\n" + "=" * 45)
    print("  Top Recommendations")
    print(f"  Genre: {user_prefs['favorite_genre']}  |  Mood: {user_prefs['favorite_mood']}  |  Energy: {user_prefs['target_energy']}")
    print("=" * 45)

    # Loop through each recommended song and print its rank, title, score, and reasons
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score : {score:.2f}")
        print(f"    Why   : {explanation}")


if __name__ == "__main__":
    main()
