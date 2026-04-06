import asyncio
from gramsnap import GramSnap, MediaType

async def main():
    async with GramSnap() as gs:
        posts = await gs.posts("ksmartboi")

        print(f"Total posts: {len(posts)}")
        print("=" * 60)

        for i, p in enumerate(posts, 1):
            print(f"Post #{i}")
            print(f"  Type     : {p.typename.name}")
            print(f"  URL      : {p.url}")
            print(f"  Likes    : {p.likes:,}")
            print(f"  Comments : {p.comments:,}")
            if p.is_video:
                print(f"  Views    : {p.video_views:,}" if p.video_views else "  Views    : N/A")
            if p.caption:
                caption_preview = p.caption[:80] + ("..." if len(p.caption) > 80 else "")
                print(f"  Caption  : {caption_preview}")
            print("-" * 60)

asyncio.run(main())