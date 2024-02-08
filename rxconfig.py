import reflex as rx

config = rx.Config(
    app_name="personal_website",
    api_url="https://my-website-reflex.vercel.app:8000",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://cmuros.reflex.run",
        "https://my-website-reflex.vercel.app"
    ],
)