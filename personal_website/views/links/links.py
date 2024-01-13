import reflex as rx
from personal_website.components.link_button import link_button
from personal_website.components.title import title
from personal_website.styles.styles import Size as Size
import personal_website.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Links"),
        link_button(
            "About Me", 
            "A little more about me", 
            constants.LOCAL_ABOUT_ME,
            "icons/aboutme.svg",
            False
            ),
        link_button(
            "My Skills", 
            "Knowing my technical skills", 
            constants.LOCAL_SKILLS,
            "icons/skills.svg",
            False
            ),
        link_button(
            "My CV", 
            "Download my CV", 
            "docs/cv_english_detail.pdf",
            "icons/cv.svg",
            False
            ),
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
        link_button(
            "Strava", 
            "Let's connect", 
            constants.MY_STRAVA,
            "icons/strava_logo.svg"
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
    