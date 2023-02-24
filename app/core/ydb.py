import ydb
import asyncio
from app.core.config import settings

async def describe_database():
    endpoint = settings.ydb_endpoint
    database = settings.ydb_database
    driver = ydb.aio.Driver(
        endpoint=endpoint, database=database
    )  # Creating new database driver to execute queries

    await driver.wait(timeout=10)  # Wait until driver can execute calls

    try:
        res = await driver.scheme_client.describe_path(database)
        print(" name: ", res.name, "\n", "owner: ", res.owner, "\n", "type: ", res.type)
    except ydb.Error as e:
        print("Cannot execute query. Reason: %s" % e)

    await driver.stop()  # Stops driver and close all connections


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(describe_database())
