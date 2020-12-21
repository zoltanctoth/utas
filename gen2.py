# -*- coding: utf-8 -*-
import datetime
from glob import glob
import os
from mutagen.mp3 import MP3

s = """<rss version="2.0"
    xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0"
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>Utas és Holdvilág</title>
    <googleplay:owner>tz@looper.hu</googleplay:owner>
    <googleplay:author>Szerb Antal</googleplay:author>
    <description>&quot;Ma bort iszom, holnap nem lesz.&quot;
    
Szereplők:

Erzsi - Ónodi Eszter
Mihály - Bodó Viktor
Elbeszélő - Gálffi László
Szepetneki János - Csányi Sándor
Zoltán - Hajdú István
Utas - Takátsy Péter
Ellesley - Lukáts Andor
Millicent - Pokorny Lia
Ervin - Zsótér Sándor
Sári - Kecskés Karina
Perzsa - Halász Péter
Waldheim - Mucsi Zoltán
Portás - Ternyák Zoltán
Nő - Gryllus Dorka
Vannina - Hámori Gabriella
Éva - Marozsán Erika
Apa - Szacsvay László

A felvételt készítette: Borlai Kinga és Kulcsár Péter

Dramaturg: Turay Tamás

Zenéjét összeállította és rendezte: Vajdai Vilmos

A felvételek a Kossuth adón hangzottak el, és a Magyar Rádió hangtárából származnak.
    </description>
    <link>https://www.looper.hu/utas</link>
    <googleplay:image href="http://www.looper.hu/utas/cover.jpg"/>
    <itunes:image href="http://www.looper.hu/utas/cover.jpg"/>
    <image>
        <link>http://www.looper.hu/utas/</link>
        <title>Utas és Holdvilág?</title>
        <url>http://www.looper.hu/utas/cover.jpg</url>
    </image>
    <language>hu-hu</language>
"""

i = 1
for f in sorted(glob("*.mp3"), reverse=True):
    link = f"http://looper.hu/utas/{f}"
    title = f"{i}. rész - Utas és Holdvilág"
    file_size = os.path.getsize(f)
    length_sec = MP3(f).info.length
    s += f"""    <item>
      <title>{title}</title>
      <description>{title}</description>
      <pubDate>Mon, 21 Dec 2020 00:00:{60-i} GMT</pubDate>
      <enclosure url="{link}"
                 type="audio/mpeg" length="{file_size}"/>
      <itunes:duration>{str(datetime.timedelta(seconds=round(length_sec))).removeprefix('0:')}</itunes:duration>
      <guid isPermaLink="false">{f[:-4]}</guid>
      <googleplay:explicit>false</googleplay:explicit>
      <itunes:explicit>false</itunes:explicit>
    </item>\n"""
    i += 1

s += """  </channel>
</rss>"""

with open("rss.xml", "w") as f:
    f.write(s)
