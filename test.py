from dotenv import load_dotenv
from role import run
import asyncio

if __name__ == "__main__":
    print(load_dotenv())
    role = "fund" #fund, pilot or science
    path = ""
    df = asyncio.run(run(path, role))