import reflex as rx

config = rx.Config(
    app_name="personal_website",
    cors_allowed_origins=[
        "https://my-website-reflex.vercel.app/",
        "localhost:3000",
    ]
)