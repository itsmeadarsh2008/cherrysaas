"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""

    ...

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="3", weight="medium"), href=url)


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("CherrySaaS", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home 🏠", "/#"),
                    navbar_link("About 📗", "/#"),
                    navbar_link("Pricing 💰", "/#"),
                    navbar_link("Contact 📞", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Signup 🌩",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Login ⚡", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.svg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("CherrySaaS", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home 🏠"),
                        rx.menu.item("About 📗"),
                        rx.menu.item("Pricing 💰"),
                        rx.menu.item("Contact 📞"),
                        rx.menu.separator(),
                        rx.menu.item("Log in ⚡"),
                        rx.menu.item("Sign up 🌩"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="transparent",
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer_newsletter() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                rx.vstack(
                    rx.text(
                        "JOIN OUR NEWSLETTER",
                        size="4",
                        weight="bold",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Your email address",
                            type="email",
                            size="3",
                        ),
                        rx.icon_button(
                            rx.icon(
                                "arrow-right",
                                padding="0.15em",
                            ),
                            size="3",
                        ),
                        spacing="1",
                        justify="center",
                        width="100%",
                    ),
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                    justify="center",
                    height="100%",
                ),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.svg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024 CherrySaaS, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        width="100%",
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.hstack(rx.logo(), rx.color_mode.button()),
        navbar_buttons(),
        rx.container(
            rx.heading(
                "BUILD YOUR SAAS TODAY. SHIP IT NEXT DAY.",
                trim="normal",
                size="9",
                align="center",
                letter_spacing="2.5px",
                style={
  "backgroundColor": "#ffb399",
  "backgroundImage": "radial-gradient(at 33% 70%, hsla(3,75%,61%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 89% 84%, hsla(261,86%,61%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 21% 98%, hsla(339,99%,75%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 10% 52%, hsla(275,87%,77%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 82% 53%, hsla(172,64%,74%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 98% 6%, hsla(174,90%,64%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 48% 12%, hsla(330,70%,71%,1) 0px, transparent 50%)",
  "backgroundClip": "text",
  "-webkitBackgroundClip": "text",
  "color": "transparent",
  "animation": "gradient-animation 1s ease infinite"
}
            ),
            rx.text("CherrySaaS is an open-source SaaS template that aims to release its product in Pure-Python, powered by Reflex. A paid subscription is required for creating plans over $150.",align="center", color="gray"),
            padding="100px",
        ),
        footer_newsletter(),
    )


app = rx.App(style={
"@keyframes gradient-animation": {
  "0%": {
    "backgroundPosition": "0% 50%"
  },
  "50%": {
    "backgroundPosition": "100% 50%"
  },
  "100%": {
    "backgroundPosition": "0% 50%"
  }
}})
app.add_page(index)
