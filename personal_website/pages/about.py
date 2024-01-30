import reflex as rx
from personal_website.components.navbar import navbar
from personal_website.styles.colors import Color
from personal_website.views.header import header
from personal_website.views.index_links import index_links
from personal_website.components.footer import footer
import personal_website.styles.styles as styles
from personal_website.styles.styles import Size as Size
import personal_website.utils as utils
from personal_website.routes import Route



@rx.page(
        route=Route.ABOUT.value,
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.meta)
def about() -> rx.Component:
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
    )