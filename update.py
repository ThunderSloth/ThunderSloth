# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11
import lichess
lichess_stats = lichess.Lichess()
lichess_badge = "![LICHESS BADGE](https://img.shields.io/badge/-{}%3A%20{}-gray?style=plastic&logo=lichess&label={}&labelColor=black&color=gray)".format(lichess_stats.time_format, lichess_stats.rating, lichess_stats.username)
print(lichess_badge)
