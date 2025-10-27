
from roles.fund import run as fund_run
from roles.pilot import run as pilot_run
from roles.science import run as science_run
import asyncio
from pathlib import Path

async def run(path, role):

    if role == "fund":
        return asyncio.run(fund_run(path))
    elif role == "pilot":
        return asyncio.run(pilot_run(path))
    elif role == "science":
        return asyncio.run(science_run(path))
    else:
        print("Такой роли не существует")
        return