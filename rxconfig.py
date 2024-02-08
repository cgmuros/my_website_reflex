import reflex as rx

config = rx.Config(
    app_name="personal_website",
    cors_allowed_origins=[
        "https://my-website-reflex.vercel.app/",
        "http://localhost:3000",
        "https://cmuros.reflex.run",
        "https://schoolbusbackend-production.up.railway.app/"
    ],
)