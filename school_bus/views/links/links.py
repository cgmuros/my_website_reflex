import reflex as rx
from school_bus.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("LikedIn", "https://www.linkedin.com/cgmuros"),
        link_button("Github", "https://www.github.com"),
        link_button("YouTube", "https://www.youtube.com"),
        width="100%"
    )