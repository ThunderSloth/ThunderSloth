# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11
import lichess
lichess_stats = Lichess()
lichess_badge = "![LICHESS BADGE](https://img.shields.io/badge/-{}%3A%20{}-gray?style=plastic&logo=lichess&label={}&labelColor=black&color=gray)".format(lichess_stats.user, lichess_stats.format, lichess_stats.rating)
print(lichess_badge)
