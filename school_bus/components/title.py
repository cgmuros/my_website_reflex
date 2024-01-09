import reflex as rx
import school_bus.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text, 
        size="lg",
        style=styles.title_style
        )