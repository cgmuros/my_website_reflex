import reflex as rx
from school_bus.components.link_icon import link_icon
from school_bus.components.info_text import info_text
from school_bus.styles.styles import Size as Size
from school_bus.styles.colors import TextColor as TextColor
from school_bus.styles.colors import Color as Color
from datetime import datetime
import school_bus.constants as const


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
            f"""I have been working on data for {experience()} years with experience 
            on BI and Big data projects on Cloud and on Premise.
            Here You will find my interest links""",
            color=TextColor.BODY.value
            ),
        spacing=Size.BIG.value,
        align_items="start"
        
    )