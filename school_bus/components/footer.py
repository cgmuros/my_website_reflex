import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2023-{datetime.date.today().year} cgmuros By Cristian Munoz V1",
            href="https://cgmuros.com",
            is_external=True
        ),
        rx.text("Building software from Chile to the World")
    )