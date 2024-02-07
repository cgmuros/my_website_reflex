
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
from personal_website.state.PageState import PageState


@rx.page(
        route=Route.MYCV.value,
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.meta,
        on_load=PageState.check_live)
def mycv():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    type="cv", 
                    title="My CV",
                    live=PageState.is_live),
                
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
    )