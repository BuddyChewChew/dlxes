import re
import certifi
import os
import requests
import datetime

# Add the channel logo constant
CHANNEL_LOGO = "https://github.com/BuddyChewChew/gen-playlist/blob/main/docs/ch.png?raw=true"

# --- Utility Functions ---

def create_nojekyll():
    # Create a .nojekyll file to prevent GitHub from processing our files
    # Only necessary if 'docs' is the GitHub Pages publishing source
    try:
        if not os.path.exists("docs"):
            os.makedirs("docs")
        with open("docs/.nojekyll", "w") as f:
            pass
    except Exception as e:
        print(f"Error creating .nojekyll: {e}")

def runServers():
    create_nojekyll()  # Ensure .nojekyll exists

    # Create a single combined playlist file with EPG URL
    # Using 'a' mode to ensure we start fresh if the file exists, or create it.
    with open("docs/combined_playlist.m3u", "w", encoding='utf-8-sig') as file:
        file.write("#EXTM3U x-tvg-url=\"https://epgshare01.online/epgshare01/epg_ripper_DUMMY_CHANNELS.xml.gz\"\n")
        file.write(f"# Playlist Generated: {datetime.datetime.now().isoformat()}\n")

    # Process each server and append to the combined playlist
    print("\n--- Running Server 1 Channels ---")
    for i in range(len(lis)):
        print(f"{i+1}. {lis[i]}")
        server1(i + 1, lis[i])

    print("\n--- Running Server 2 Channels ---")
    for i in range(len(hashCode)):
        print(f"{i+1}. {channels[i]}")
        server2(hashCode[i], channels[i])

    print("\n--- Running Server 3 Channels ---")
    for i in range(len(hashcode_3)):
        print(f"{i+1}. {channels_3[i]}")
        server3(hashcode_3[i], channels_3[i])

# --- Server Functions ---

def server1(i, name):
    print("Running Server 1")
    url = f"https://adult-tv-channels.com/tv/{name}.php"
    headers = {
        # Using a current, common User-Agent
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://adult-tv-channels.com",
        # Removed "X-Requested-With" to avoid unnecessary blocking
    }

    try:
        response = requests.get(url, headers=headers, verify=certifi.where(), timeout=15)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # *** MODIFIED REGEX (The Fix) ***
        # Searches for: (file or source): followed by (" or ') followed by a URL that contains .m3u8 or .ts
        # Captures the URL in group 2
        match = re.search(r'(file|source):\s*["\']([^"\']+\.(m3u8|ts)[^"\']*)["\']', response.text)
        
        if match:
            stream_url = match.group(2)
            with open("docs/combined_playlist.m3u", "a", encoding='utf-8-sig') as file:
                file.write(f'#EXTINF:-1 tvg-id="Adult.Programming.Dummy.us" tvg-name="{name}" tvg-logo="{CHANNEL_LOGO}" group-title="Adult 1",{name}\n')
                file.write(f"{stream_url}\n")
            print(f"✅ Found stream for {name}")
        else:
            print(f"😡 No URL found for {name}. Content length: {len(response.text)}")

    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error for {name}: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error for {name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {name}: {e}")


def server2(hash, name):
    print("Running Server 2")
    try:
        res = requests.post(
            f"https://adult-tv-channels.click/C1Ep6maUdBIeKDQypo7a/{hash}",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=10
        )
        res.raise_for_status()
        data = res.json()
        token = data["fileUrl"]
        stream_url = f"https://moonlight.wideiptv.top/{name}/index.fmp4.m3u8?token={token}"
        with open("docs/combined_playlist.m3u", "a", encoding='utf-8-sig') as file:
            file.write(f'#EXTINF:-1 tvg-id="Adult.Programming.Dummy.us" tvg-name="{name}" tvg-logo="{CHANNEL_LOGO}" group-title="Adult 2",{name}\n')
            file.write(f"{stream_url}\n")
        print(f"✅ Found stream for {name}")
    except Exception as e:
        print(f"Error processing {name}: {str(e)}")

def server3(hash, name):
    print("Running Server 3")
    try:
        url = f"https://fuckflix.click/8RLxsc2AW1q8pvyvjqIQ"
        res = requests.post(
            f"{url}/{hash}",  
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=10
        )
        res.raise_for_status()
        data = res.json()
        token = data["fileUrl"]
        stream_url = f"https://moonlight.wideiptv.top/{name}/index.fmp4.m3u8?token={token}"
        with open("docs/combined_playlist.m3u", "a", encoding='utf-8-sig') as file:
            file.write(f'#EXTINF:-1 tvg-id="Adult.Programming.Dummy.us" tvg-name="{name}" tvg-logo="{CHANNEL_LOGO}" group-title="Adult 3",{name}\n')
            file.write(f"{stream_url}\n")
        print(f"✅ Found stream for {name}")
    except Exception as e:
        print(f"Error processing {name}: {str(e)}")

# --- Channel Lists (Unchanged) ---

lis = [
    "brazzerstv",
    "hustlerhd",
    "hustlertv",
    "penthouse",
    "redlight",
    "penthousepassion",
    "vivid",
    "dorcel",
    "superone",
    "oxax",
    "passie",
    "eroxxx",
    "playboy",
    "pinko",
    "extasy",
    "penthousereality",
    "kinoxxx",
    "pinkerotic",
    "pinkerotic7",
    "pinkerotic8",
    "evilangel",
    "private",
    "beate",
    "meiden",
    "centoxcento",
    "barelylegal",
    "venus",
    "freextv",
    "erox",
    "passion",
    "satisfaction",
    "jasmin",
    "fap",
    "olala",
    "miamitv",
]

# for Server 2
hashCode = [
    "Sdw0p0xE3E",
    "yoni9C8jfd",
    "ZS40W182Zq",
    "czS16artgz",
    "xBFRYv6yXh",
    "hghdvp9Z03",
    "ByYpxFkJZe",
    "5LvPjA7oms",
    "HdcCGPssEy",
    "sI8DBZkklJ",
    "sSEWMS7slF",
    "dRTbLz32p7",
    "Sd6GJ5uMmj",
    "IDLur5k1x2",
    "4FVedsyYlB",
    "S8XdeQ0R1t",
    "svpUwVLRR8",
    "A2PZR5jdH8",
    "3uGUuSP7HX",
    "oEd93JisZ3",
    "E3WyHBCn6j",
    "5QeEhtMv0v",
    "ZQgSJJmzAx",
    "JTzDFcBdgp",
    "58Nyzda2hb",
    "ZvBCE7cpgP",
    "V2D4lPbasF",
    "t6VXUhiBYF",
    "JiA1DWNWJc",
]

channels = [
    "ExxxoticaTV",
    "LeoTV",
    "LeoGoldTV",
    "EvilAngel",
    "VIXEN",
    "Extasy4K",
    "PinkoClubTV",
    "BrazzersTVEU",
    "HustlerHD",
    "RedlightHD",
    "SecretCircleTV",
    "PenthouseGold",
    "Television-X",
    "Private",
    "HOT-HD",
    "BODYSEX",
    "DorcelTV",
    "TransAngels",
    "SuperONE",
    "SextremeTV",
    "SeXation",
    "PassionXXX",
    "HustlerTV",
    "EroX-XxX",
    "EroLuxeShemales",
    "DesireTV",
    "CentoXCento",
    "Barely-Legal-TV",
    "Venus",
]

hashcode_3 = [
    "5LvPjA7oms",
    "CudzGm9xm6",
    "T3PIyktDDU",
    "9itOC3AHqJ",
    "OWMDBFfu89",
    "QOOfbBqT4v",
    "2x7HptDKuX",
    "esdMCy0VGM",
    "6s6dIMWGXi",
    "Sdw0p0xE3E",
    "ZS40W182Zq",
    "yoni9C8jfd",
    "czS16artgz",
    "hghdvp9Z03",
    "xBFRYv6yXh",
    "E3WyHBCn6j",
    "HdcCGPssEy",
    "ByYpxFkJZe",
    "Sd6GJ5uMmj",
    "t6VXUhiBYF",
    "58Nyzda2hb",
    "sSEWMS7slF",
    "s4URaZHdvZ",
    "sI8DBZkklJ",
    "YC81XHWeHu",
    "v3UeIcgWXa",
    "dRTbLz32p7",
    "IDLur5k1x2",
    "JAZlXsiLni",
    "R4ol8r2lki",
    "kpTVK5NF1w",
    "m6Elk7hY4x",
    "S8XdeQ0R1t",
    "4FVedsyYlB",
    "svpUwVLRR8",
    "A2PZR5jdH8",
    "3uGUuSP7HX",
    "oEd93JisZ3",
    "5QeEhtMv0v",
    "ZQgSJJmzAx",
    "JTzDFcBdgp",
    "ZvBCE7cpgP",
    "V2D4lPbasF",
    "JiA1DWNWJc",
    "jK2r6H1Dlj",
]

channels_3 = [
    "BrazzersTVEU",
    "Tiny4k1",
    "Tiny4k2",
    "Tiny4k3",
    "PenthouseBLACK",
    "Penthouse",
    "NuartTV",
    "Mofos",
    "cum4k",
    "ExxxoticaTV",
    "LeoGoldTV",
    "LeoTV",
    "EvilAngel",
    "Extasy4K",
    "VIXEN",
    "SeXation",
    "HustlerHD",
    "PinkoClubTV",
    "Television-X",
    "Barely-Legal-TV",
    "EroLuxeShemales",
    "SecretCircleTV",
    "Beate-Uhse",
    "RedlightHD",
    "DorcelTVAfrica",
    "PlayboyTV",
    "PenthouseGold",
    "Private",
    "HOTMan",
    "SexyHOT",
    "TransErotica",
    "HOTXXL",
    "BODYSEX",
    "HOT-HD",
    "DorcelTV",
    "TransAngels",
    "SuperONE",
    "SextremeTV",
    "PassionXXX",
    "HustlerTV",
    "EroX-XxX",
    "DesireTV",
    "CentoXCento",
    "Venus",
    "XXL",
]

# --- Main Execution ---

if __name__ == "__main__":
    runServers()
