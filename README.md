# GramSnap

Async Python client for the GramSnap Instagram viewer API.

## Requirements

```
pip install curl-cffi fake-useragent
```

## Usage

```python
import asyncio
from gramsnap import GramSnap, MediaType

async def main():
    async with GramSnap() as gs:
        posts = await gs.posts("username")
        for p in posts:
            print(f"[{p.typename.name}] {p.url} likes={p.likes}")

asyncio.run(main())
```

## Output fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `str` | Post ID |
| `shortcode` | `str` | Post shortcode |
| `typename` | `MediaType` | `IMAGE`, `VIDEO`, or `SIDECAR` |
| `is_video` | `bool` | Whether the post is a video |
| `display_url` | `str` | Main image/thumbnail URL |
| `width` / `height` | `int` | Dimensions |
| `caption` | `str` | Post caption |
| `likes` | `int` | Like count |
| `comments` | `int` | Comment count |
| `timestamp` | `int` | Unix timestamp |
| `video_url` | `str \| None` | Video URL (videos only) |
| `video_views` | `int \| None` | View count (videos only) |
| `children` | `list[Media]` | Child media (sidecars only) |
| `url` | `str` | Instagram post URL (property) |
