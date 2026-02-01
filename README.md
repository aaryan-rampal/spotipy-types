# Spotipy Types

Complete Python type hints for the Spotify Web API using Pydantic v2 models.

## Installation

```bash
pip install spotipy-types
```

## Usage

```python
from spotipy_types import TrackObject, AlbumObject
import spotipy

# Get typed results from spotipy
sp = spotipy.Spotify(auth=token)
track: TrackObject = sp.track("track_id")

# IDE autocomplete works!
print(track.name)
print(track.artists[0].name)
```

## Features

- 100+ Pydantic v2 models auto-generated from official OpenAPI schema
- Full IDE autocomplete support
- Runtime validation of API responses
- JSON serialization/deserialization
- Python 3.11+ with union operator syntax

## License

MIT License
