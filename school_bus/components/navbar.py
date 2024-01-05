import reflex as rx



def navbar() -> rx.Component:
    return rx.hstack(
                rx.text(
                    "cgmuros dev",
                    height="40px"
                ),
                position="sticky",
                bg="blue",
                padding_x="16px",
                padding_y="16px",
                z_index="999"
            )  