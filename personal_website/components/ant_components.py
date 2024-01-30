import reflex as rx
from personal_website.styles.colors import Color as Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    # icon = rx.Image(src="/icons/linkedin_blue.svg")
    icon : rx.Var[rx.Image]
    # href = "https://www.linkedin.com/in/cgmuros/"
    href : rx.Var[str]
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}

  
float_button = FloatButton.create