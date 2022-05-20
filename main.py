try:
    import os
    import threading
    import time
    
    from pystyle import System
    from itertools import cycle
    from requests_futures.sessions import FuturesSession
except KeyboardInterrupt as e:
    os.system('cls & mode 80, 20 & title Error')
    print(f"-> ImportError!")
    time.sleep(1)
    System.Clear()
    os.system('pip install pystyle')

os.system('cls & mode 80, 20 & title Login')
token = input(f"-> Token: ")
guild = input(f"-> Guild ID: ")
System.Clear()

ss = (200, 201, 204)
ban_reason = "ysmir W"

class massban:

    def massban_worker(session, member):
        try:
            proxies = open('assets/proxies.txt').read().split('\n')
            proxy = cycle(proxies)
            headers = {
                "Authorization":
                f"Bot {token}"
            }
            fails = 0
            s = session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}?reason={ban_reason}", headers = headers, proxies = {"http": 'http://' + next(proxy)}).result()
            if s.status_code in ss:
                print(f"Banned Member: {member}")
            elif s.status_code == 429:
                print(f"RateLimited For: {s.json()['retry_after']}")
            else:
                fails += 1
                print(f"Failed To Ban: {member}")
        except KeyboardInterrupt:
            input();os._exit(0)

if __name__ == "__main__":
    os.system('title Massban')
    members = []
    amount = 0
    session = FuturesSession(max_workers = 400)
    a_file = open('assets/members.txt','r')
    for line in a_file:
        stripped_line = line.strip()
        members.append(stripped_line)
    a_file.close()
    looping = True
    while looping:
        try:
            threading.Thread(target = massban.massban_worker, args = (session, members[amount],)).start()
        except:
            looping = False
        amount += 1
        threads = []
    for member in members:
        thread = threading.Thread(target = massban.massban_worker, args = (session, member,)).start()
        threads.append(thread)
        thread.start()
    for thread in threads:
        try:
            thread.join()
        except Exception:
            pass