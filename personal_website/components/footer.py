import reflex as rx
import datetime
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
import personal_website.constants as const




def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo_128.png",
            height=Size.VERY_BIG.value
            ),
        rx.link(
            f"2023-{datetime.date.today().year} cgmuros By Cristian Munoz V1",
            href=const.MY_LINKEDIN,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "Building software from Chile to the World",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
            ),
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,

    )