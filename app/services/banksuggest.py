import asyncio
from app.services.dadata import dadata_suggest_bank


async def suggest_bank_names(phrase: str):
    data = asyncio.run(dadata_suggest_bank(phrase))
    for i in range(len(data)):
        print(data[i]['value'])
    return None
