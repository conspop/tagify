import pandas as pd

def merge_tracks_and_features(tracks, features):
    tracks_df = pd.DataFrame(tracks)
    features_df = pd.DataFrame(features)

    df = tracks_df.merge(features_df, on="id")

    album = pd.json_normalize(df.album)
    df["album_name"] = album.name
    df["release_date"] = album.release_date

    album_images = pd.json_normalize(album.images)
    df["album_image"] = pd.json_normalize(album_images[0]).url

    artists = pd.json_normalize(df.artists)
    df["artist"] = pd.json_normalize(artists[0]).name

    return df[
        [
            "id",
            "album_image",
            "name",
            "album_name",
            "artist",
            "popularity",
            "danceability",
            "energy",
            "key",
            "loudness",
            "mode",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            "tempo",
            "duration_ms_y",
            "time_signature",
        ]
    ].to_dict(orient="records")
    
