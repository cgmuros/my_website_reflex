import reflex as rx
import personal_website.api.api as api


class PageState(rx.State):
    is_live : bool

    async def check_live(self):
        self.is_live = await api.live()
