import reflex as rx
from school_bus.components.navbar import navbar
from school_bus.views.header.header import header
from school_bus.views.links.links import links
from school_bus.components.footer import footer
import school_bus.styles.styles as styles


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=styles.Size.BIG.value
                    )),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.compile()