# command to run this script from root dir:  python -m app.services.dadata

import asyncio
from dadata import DadataAsync
from app.core.config import settings


async def dd_find_by_id(subject: str, id: str):
    async with DadataAsync(settings.dd_token, settings.dd_secret,) as dadata:
        result = await dadata.find_by_id(name=subject, query=id)
        return result


async def dd_suggest(subject: str, name: str):
    async with DadataAsync(settings.dd_token, settings.dd_secret,) as dadata:
        result = await dadata.suggest(name=subject, query=name)
        return result


if __name__ == "__main__":
    print(asyncio.run(dd_find_by_id('bank', '007182108')))
