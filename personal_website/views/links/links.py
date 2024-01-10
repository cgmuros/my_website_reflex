import reflex as rx
from personal_website.components.link_button import link_button
from personal_website.components.title import title
from personal_website.styles.styles import Size as Size
import personal_website.constants as constants



def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(
            "LikedIn", 
            "Let's talk on linkedin", 
            constants.MY_LINKEDIN,
            "icons/linkedin.svg"
            ),
        link_button(
            "Github", 
            "I invite you to review my repos", 
            constants.MY_GITHUB,
            "icons/square-github.svg"
            ),
        link_button(
            "Twitter", 
            "Let's connect", 
            constants.MY_TWITTER,
            "icons/twitter_logo.svg"
            ),
        
        title("Contact"),
        link_button(
            "Email", 
            constants.MY_EMAIL, 
            f"mailto:{constants.MY_EMAIL}",
            "icons/envelope-solid.svg"
            ),


        width="100%",
        spacing=Size.MEDIUM.value
    )
    