import reflex as rx
from school_bus.components.navbar import navbar
from school_bus.views.header.header import header
from school_bus.views.links.links import links
from school_bus.components.footer import footer
import school_bus.styles.styles as styles
from school_bus.styles.styles import Size as Size


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
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESCHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="CgmurosDev. Software Engineering and Data",
    image="me.png")
app.compile()