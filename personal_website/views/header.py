import reflex as rx
from personal_website.components.link_icon import link_icon
from personal_website.components.info_text import info_text
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
from personal_website.styles.colors import Color as Color
import personal_website.styles.styles as styles
from personal_website.components.message import message
import personal_website.constants as const
import personal_website.common.common as common




def header(type: str = "", title: str = "", live=False) -> rx.Component:
    return rx.vstack( 
        rx.hstack(
            rx.link(
                rx.avatar(
                    rx.cond(
                        live,
                        rx.avatar_badge(
                            rx.image(src="/icons/power.svg"),
                            box_size=Size.MEDIUM.value,
                            bg=Color.GREEN.value,
                            border_color=Color.GREEN.value,
                        ),
                        rx.avatar_badge(
                            rx.image(src="/icons/power.svg"),
                            box_size=Size.MEDIUM.value,
                            bg=Color.RED_OFFLINE.value,
                            border_color=Color.RED_OFFLINE.value,
                        ),
                    ),
                    name="Cristian Munoz", 
                    size="xl",
                    src="/me_128.png",
                    padding="2px",
                    color=TextColor.BODY.value,
                    border="4px",
                    border_color=Color.PRIMARY.value,
                    bg=Color.CONTENT.value
                    ),
                href="/",
            ),
            
            rx.vstack(
                rx.heading("Cristian Munoz", size="lg"),
                rx.text("cgmuros@gmail.com", margin_top=Size.ZERO.value, color=TextColor.BODY.value),
                rx.hstack(
                    link_icon("/icons/linkedin.svg", const.MY_LINKEDIN, "Linkedin"),
                    link_icon("/icons/square-github.svg", const.MY_GITHUB, "Github"),
                    link_icon("/icons/twitter_logo.svg", const.MY_TWITTER, "Twitter/X"),
                    link_icon("/icons/strava_logo.svg", const.MY_STRAVA, "Strava"),
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value
        ),

        rx.flex(
            info_text("+15", "Profesional Experience"),
            rx.spacer(),
            info_text("+10", "Data Engineer"),
            rx.spacer(),
            info_text("+6", "Data Architect"),
            width="100%"
        ),
        rx.text(title, color=TextColor.HEADER.value, font_size=Size.LARGE.value),
        message(type=type),
        spacing=Size.BIG.value,
        align_items="start",
        max_width=styles.MAX_WIDTH,
        width="100%",
    )