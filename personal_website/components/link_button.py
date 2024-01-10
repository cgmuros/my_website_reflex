import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.styles import Size as Size


def link_button(tittle: str, body: str, url: str, image: str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=Size.LARGE.value,
                        height=Size.LARGE.value,
                        margin=Size.MEDIUM.value
                    ),
                    rx.vstack(
                        rx.text(tittle, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        align_items="start",
                        spacing=Size.SMALL.value,
                        padding_y=Size.SMALL.value,
                        padding_right=Size.SMALL.value

                    ),
                    widht="100%"
                )
            ),
            href=url,
            is_external=True,
            width="100%"
        )
    