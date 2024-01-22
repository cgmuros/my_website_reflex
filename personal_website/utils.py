import reflex as rx

# Common
index_title = "CgmurosDev. Software Engineering and Data"
index_description = "Building software from Chile to the World"
preview = "me_128.png"
meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": index_title},
        {"name": "og:description", "content": index_description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@cmurosdev"}
    ]

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'en'")

