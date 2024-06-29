import reflex as rx

@rx.page('/blog')
def blog():
    return rx.container(
        rx.text("Welcome to the blog!"),
    )