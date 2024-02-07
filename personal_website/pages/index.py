import reflex as rx
import personal_website.utils as utils
import personal_website.styles.styles as styles
from personal_website.components.navbar import navbar
from personal_website.styles.colors import Color
from personal_website.views.header import header
from personal_website.views.index_links import index_links
from personal_website.components.footer import footer
from personal_website.styles.styles import Size as Size
from personal_website.state.PageState import PageState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.meta,
    on_load=PageState.check_live
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    live=PageState.is_live
                ),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value
            )
        ),
        footer(),
    )


