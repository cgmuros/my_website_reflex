import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Cristian Munoz", 
            size="xl"),
        rx.text("@cgmuros"),
        rx.text("HOLA, MI NOMBRE ES CRISTIAN MUNOZ"),
        rx.text("I have been working on data for 14 years with experience on BI and Bog data projects on Cloud and on Premise."
                "Here You will find my interest links")
    )