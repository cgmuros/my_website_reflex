import reflex as rx
from personal_website.components.navbar import navbar
from personal_website.styles.colors import Color
from personal_website.views.header import header
from personal_website.views.index_links import index_links
from personal_website.components.footer import footer
import personal_website.styles.styles as styles
from personal_website.styles.styles import Size as Size
from personal_website.pages.index import index
from personal_website.pages.about import about
from personal_website.pages.skills import skills
from personal_website.pages.mycv import mycv



app = rx.App(
    stylesheets=styles.STYLESCHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-HTB3V4RS0N"),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', "G-HTB3V4RS0N");
            """
        )
    ]
)

