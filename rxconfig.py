import reflex as rx

config = rx.Config(
    app_name="personal_website",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://cmuros.reflex.run",
        "https://my-website-reflex.vercel.app"
    ],
)