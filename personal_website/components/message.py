import reflex as rx
from personal_website.styles.colors import TextColor as TextColor
import personal_website.common.common as common


MY_SKILLS: str = """Here is a list of the technologies with which I have worked on various projects"""

MY_OVERRVIEW: str = f"""I have been working for the last {common.experience()} years on data-related projects. 
            Various Companies and Projects have allowed me to gain experience and meet great teams in which I have been able to be a contribution. 
            I built this site mainly so that you can get to know me and contact me if you need it."""

MY_OVERVIEW_ABOUT: str = f"""My name is Cristian Munoz, a Computer Engineer by profession, family man, passionate about software development and lover of sports. 
            Because I am passionate about software development, I am constantly researching and learning about new technologies.
            Due to the above, I have been growing professionally and learning from the projects in which I have participated.
            I invite you to connect and talk. It is always good to generate instances of conversation with others.
            I invite you to review the experience in various technologies and if you have any interesting ideas, do not hesitate to contact me."""

MY_CV: str = f"""Here all the details of my professional experience."""


def message(type: str = "") -> rx.Component:
    text = MY_OVERRVIEW
    if type == "about":
        text = MY_OVERVIEW_ABOUT
    elif type == "cv":
        text = MY_CV
    elif type == "skills":
        text = MY_SKILLS

    paragraphs = text.split('\n')
    text_components = [rx.text(paragraph, color=TextColor.BODY.value, align="left") for paragraph in paragraphs if paragraph.strip()]

    return rx.vstack(
        *text_components,
        align_items="start",
        widht="100%"
        )