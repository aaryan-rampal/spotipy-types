"""Spotipy Types - Pydantic models for the Spotify Web API.

This package provides complete Python type hints for the Spotify Web API
by auto-generating Pydantic v2 models from the official OpenAPI schema.

Example:
    >>> from spotipy_types import TrackObject, AlbumObject
    >>> import spotipy
    >>> sp = spotipy.Spotify(auth=token)
    >>> track: TrackObject = sp.track("track_id")
    >>> print(track.name)
    >>> print(track.artists[0].name)
"""

from spotipy_types._version import __version__, __schema_version__, __schema_source__
from spotipy_types.models import (
    # Core Objects
    TrackObject,
    AlbumObject,
    ArtistObject,
    PlaylistObject,
    EpisodeObject,
    ShowObject,
    UserObject,
    DeviceObject,
    # Response Types
    SearchResponse,
    PagingObject,
    CursorPagingObject,
    # Audio Features
    AudioFeaturesObject,
    # Simplified Objects
    SimplifiedTrackObject,
    SimplifiedAlbumObject,
    SimplifiedArtistObject,
    SimplifiedPlaylistObject,
    SimplifiedEpisodeObject,
    SimplifiedShowObject,
    # Other Common Types
    ImageObject,
    FollowersObject,
    ExternalUrlObject,
    ExternalIdObject,
    RestrictionsObject,
    # Error Handling
    ErrorObject,
    # Context
    ContextObject,
    CurrentlyPlayingObject,
    PlaybackStateObject,
    # All models (re-export everything)
    *
)

__all__ = [
    "__version__",
    "__schema_version__",
    "__schema_source__",
    # Core Objects
    "TrackObject",
    "AlbumObject",
    "ArtistObject",
    "PlaylistObject",
    "EpisodeObject",
    "ShowObject",
    "UserObject",
    "DeviceObject",
    # Response Types
    "SearchResponse",
    "PagingObject",
    "CursorPagingObject",
    # Audio Features
    "AudioFeaturesObject",
    # Simplified Objects
    "SimplifiedTrackObject",
    "SimplifiedAlbumObject",
    "SimplifiedArtistObject",
    "SimplifiedPlaylistObject",
    "SimplifiedEpisodeObject",
    "SimplifiedShowObject",
    # Other Common Types
    "ImageObject",
    "FollowersObject",
    "ExternalUrlObject",
    "ExternalIdObject",
    "RestrictionsObject",
    # Error Handling
    "ErrorObject",
    # Context
    "ContextObject",
    "CurrentlyPlayingObject",
    "PlaybackStateObject",
]
