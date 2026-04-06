import asyncio
from gramsnap import GramSnap, MediaType

async def main():
    async with GramSnap() as gs:
        posts = await gs.posts("ksmartboi")
        for p in posts:
            print(f"[{p.typename.name}] {p.url} likes={p.likes}")

asyncio.run(main())