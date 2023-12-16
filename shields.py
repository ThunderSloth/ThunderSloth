# This class constructs a url for the shields.io api that creates a
# custom mark-down badge given text, color, logo and style parameters.
# Eli Bell
# 2023-10-11
from urllib.parse import urlencode, quote


def shields(text1, color1, text2, color2, logo, style):
    args = {}
    args["title"] = logo.upper()
    args["base_url"] = "https://img.shields.io/badge/"
    args["message"] = quote("-".join(["", text2, color1])) + "?"
    args["query_params"] = {
        "style": style,
        "logo": logo,
        "logoColor": "white",
    }
    if text1 and color2:
        args["query_params"]["label"] = text1
        args["query_params"]["color"] = color2
        args["query_params"]["labelColor"] = color1

    args["query_string"] = urlencode(args.get("query_params"))
    args["full_url"] = (
        args.get("base_url") + args.get("message") + args.get("query_string")
    )

    return "![{}]({})".format(args.get("title"), args.get("full_url"))
