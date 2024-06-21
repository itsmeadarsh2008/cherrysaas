"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# from reflex import chakra
# from rxconfig import config
from reflex_motion import motion

# class State(rx.State):
#     """The app state."""


#     ...
def feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=rx.color("grass", 9)),
        rx.text(text, size="4"),
    )


def pricing_card(
    title: str,
    description: str,
    price: str,
    price_unit: str,
    features_list: list[str],
    button_text: str = "Get started",
) -> rx.Component:
    return motion(
        rx.vstack(
            rx.vstack(
                rx.text(title, weight="bold", size="6"),
                rx.text(
                    description,
                    size="4",
                    opacity=0.8,
                    align="center",
                ),
                rx.hstack(
                    rx.text(
                        price,
                        weight="bold",
                        font_size="3rem",
                        trim="both",
                    ),
                    rx.text(
                        price_unit,
                        size="4",
                        opacity=0.8,
                        trim="both",
                    ),
                    width="100%",
                    align_items="end",
                    justify="center",
                ),
                width="100%",
                align="center",
                spacing="6",
            ),
            rx.vstack(
                *[feature_item(feature) for feature in features_list],
                width="100%",
                align_items="start",
            ),
            rx.button(
                button_text,
                size="3",
                variant="solid",
                width="100%",
                color_scheme="blue",
            ),
            spacing="6",
            border=f"1.5px solid {rx.color('gray', 5)}",
            background=rx.color("gray", 1),
            padding="28px",
            width="100%",
            max_width="400px",
            justify="center",
            border_radius="0.5rem",
        ),
        initial={"scale": 1},
        while_hover={"scale": 1.2},
        transition={"type": "spring", "stiffness": 400, "damping": 17}
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


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
                    spacing="4",
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
        rx.heading("PRODUCTS", size="4", weight="bold", as_="h3"),
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
        rx.heading("RESOURCES", size="4", weight="bold", as_="h3"),
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


# Example usage
beginner_features = [
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support",
]
pro_features = [
    "Unlimited users",
    "Unlimited projects",
    "Unlimited team members",
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support",
]
enterprise_features = [
    "Unlimited users",
    "Unlimited projects",
    "Unlimited team members",
    "24/7 customer support",
    "Daily backups",
    "Advanced analytics",
    "Customizable templates",
    "Priority email support",
]
faq_items = [
    (
        "What is CherrySaaS?",
        f"CherrySaaS is a 100% open-source Reflex template for building SaaS applications.",
    ),
    (
        "How do I get started with CherrySaaS?",
        "You can get started by visiting the CherrySaaS documentation.",
    ),
    ("Is CherrySaaS free to use?", "CherrySaaS offers both free and premium plans."),
    (
        "What payment options do I have?",
        "CherrySaaS has Stripe and LemonSqueezy as payment options. UPI is not available.",
    ),
    (
        "How fast I can build SaaS?",
        "Make SaaS within a day if you're a mediocre. CherrySaaS is built with Reflex in mind.",
    ),
    (
        "How do I contribute?",
        "If you're interested in contributing, please visit our GitHub repository. cherryblossom-inspired perfection. 🌸",
    ),
]


def faq_section() -> rx.Component:
    # Create an accordion for the FAQ section
    return rx.chakra.accordion(
        # Generate an accordion item for each FAQ item
        *[
            rx.chakra.accordion_item(
                rx.chakra.accordion_button(
                    rx.chakra.heading(question, size="md"),
                    rx.chakra.accordion_icon(),
                ),
                rx.chakra.accordion_panel(rx.chakra.text(answer)),
            )
            for question, answer in faq_items
        ],
        allow_toggle=True,  # Allow opening multiple items at once
        width="100%",
        top_padding="20px",
        bottom_padding="20px",
        margin="30px",
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.hstack(rx.logo(), rx.color_mode.button()),
        navbar_buttons(),
        rx.container(
            motion(
                rx.heading(
                    "BUILD YOUR SAAS TODAY. SHIP IT NEXT DAY.",
                    trim="normal",
                    size="9",
                    as_="h1",
                    align="center",
                    letter_spacing="2.5px",
                    style={
                        "backgroundColor": "#ffb399",
                        "backgroundImage": "radial-gradient(at 33% 70%, hsla(3,75%,61%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 89% 84%, hsla(261,86%,61%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 21% 98%, hsla(339,99%,75%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 10% 52%, hsla(275,87%,77%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 82% 53%, hsla(172,64%,74%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 98% 6%, hsla(174,90%,64%,1) 0px, transparent 50%),\r\n                     radial-gradient(at 48% 12%, hsla(330,70%,71%,1) 0px, transparent 50%)",
                        "backgroundClip": "text",
                        "-webkitBackgroundClip": "text",
                        "color": "transparent",
                        "animation": "gradient-animation 1s ease infinite",
                    },
                ),
                initial={"scale": 1},
                while_hover={"scale": 1.2},
                transition={"type": "spring", "stiffness": 400, "damping": 17}
            ),
            padding="100px",
        ),
        rx.text(
            "CherrySaaS is an open-source SaaS template built on Reflex and performant technologies 🐲",
            align="center",
            size="4",
            variant="surface",
        ),
        rx.hstack(
            pricing_card(
                title="Beginner",
                description="Ideal choice for personal use & for your next project.",
                price="$39",
                price_unit="/month",
                features_list=beginner_features,
            ),
            pricing_card(
                title="Pro",
                description="Everything in Beginner, plus all premium features.",
                price="$59",
                price_unit="/month",
                features_list=pro_features,
            ),
            pricing_card(
                title="Enterprise",
                description="Everything in Pro, plus all enterprise features.",
                price="$399",
                price_unit="/month",
                features_list=enterprise_features,
            ),
            spacing="4",
            padding="20px",
            flex_direction=["column", "column", "row"],
            width="100%",
            align_items="center",
        ),
        rx.heading(
            "FAQ", trim="normal", size="7", as_="h1", weight="bold", align="center"
        ),
        faq_section(),
        footer_newsletter(),
    )


app = rx.App(
    style={
        "@keyframes gradient-animation": {
            "0%": {"background_position": "0% 50%"},
            "50%": {"background_position": "100% 50%"},
            "100%": {"background_position": "0% 50%"},
        }
    }
)
app.add_page(index)
