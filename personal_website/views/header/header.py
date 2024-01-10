import reflex as rx
from personal_website.components.link_icon import link_icon
from personal_website.components.info_text import info_text
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
from personal_website.styles.colors import Color as Color
from datetime import datetime
import personal_website.constants as const


def experience():
    # Obtén la fecha actual
    fecha_actual = datetime.now()
    fecha_referencia = datetime(2009, 1, 1)
    diferencia_anos = fecha_actual.year - fecha_referencia.year
    resultado_string = str(diferencia_anos)
    return resultado_string

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Cristian Munoz", 
                size="xl",
                src="me.png",
                padding="2px",
                color=TextColor.BODY.value,
                border="4px",
                border_color=Color.PRIMARY.value,
                bg=Color.CONTENT.value),
            rx.vstack(
                rx.heading("Cristian Munoz", size="lg"),
                rx.text("@cgmuros", margin_top=Size.ZERO.value, color=TextColor.BODY.value),
                rx.hstack(
                    link_icon("icons/linkedin.svg", const.MY_LINKEDIN, "Linkedin"),
                    link_icon("icons/square-github.svg", const.MY_GITHUB, "Github"),
                    link_icon("icons/twitter_logo.svg", const.MY_TWITTER, "Twitter/X"),
                    link_icon("icons/strava_logo.svg", "https://www.strava.com/athletes/49921501", "Strava")
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),

        rx.flex(
            info_text("+15", "Profesional Experience"),
            rx.spacer(),
            info_text("+10", "Data Engineer"),
            rx.spacer(),
            info_text("+6", "Data Architect"),
            width="100%"
        ),

        rx.text(
            f"""I have been working for the last {experience()} years 
            on data-related projects. Various Companies and Projects 
            have allowed me to gain experience and meet great teams 
            in which I have been able to be a contribution. I built 
            this site mainly so that you can get to know me and contact 
            me if you need it.""",
            color=TextColor.BODY.value
            ),
        spacing=Size.BIG.value,
        align_items="start"
        
    )