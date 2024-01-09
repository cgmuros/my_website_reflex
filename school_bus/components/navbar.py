import reflex as rx
from school_bus.styles.styles import Size as Size
from school_bus.styles.colors import TextColor as TextColor
from school_bus.styles.colors import Color as Color
import school_bus.styles.styles as styles



def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("cgmuros", color=Color.PRIMARY.value),
            rx.span("dev", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )  