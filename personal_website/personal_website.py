import reflex as rx
from personal_website.components.navbar import navbar
from personal_website.styles.colors import Color
from personal_website.views.header.header import header
from personal_website.views.links.links import links
from personal_website.components.footer import footer
import personal_website.styles.styles as styles
from personal_website.styles.styles import Size as Size
from personal_website.components.link_button import link_button




def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value
            )
        ),
        footer(),
        background_color=Color.BACKGROUND.value
    )


@rx.page()
def about():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(type="about", title="About Me"),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value
            )
        ),
        footer(),
        background_color=Color.BACKGROUND.value
    )

@rx.page()
def skills():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(type="skills", title="My Skills"),

                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value
            )
        ),
        footer(),
        background_color=Color.BACKGROUND.value
    )

@rx.page()
def mycv():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(type="cv", title="My CV"),
                
                rx.box(
                    element="iframe",
                    src="/docs/cv_english_detail.pdf",
                    width="100%",
                    max_width=styles.MAX_WIDTH,
                    border_radius="lg",
                    height="600px",
                
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value,
                
            )
        ),
        footer(),
        background_color=Color.BACKGROUND.value
    )


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
app.add_page(
    index,
    title="CgmurosDev. Software Engineering and Data",
    image="me.png")
app.add_page(about, title="About")
app.add_page(skills, title="My Skills")
app.add_page(mycv, title="My CV")
