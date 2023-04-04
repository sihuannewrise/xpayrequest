# command to run this script from root dir:  python -m app.services.dadata

import asyncio
from dadata import DadataAsync
from app.core.config import settings


async def dadata_find_bank(id: str):
    async with DadataAsync(settings.dd_token, settings.dd_secret,) as dadata:
        result = await dadata.find_by_id(name='bank', query=id)
        return result


async def dadata_suggest_bank(name: str):
    async with DadataAsync(settings.dd_token, settings.dd_secret,) as dadata:
        result = await dadata.suggest(name='bank', query=name)
        return result


if __name__ == "__main__":
    print(asyncio.run(dadata_find_bank('007182108')))
