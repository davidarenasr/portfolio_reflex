"""The home page of the app."""

from portfolio_r import styles
from portfolio_r.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.chakra.vstack(
        rx.chakra.heading("David Arenas", font_size="4em"),
        rx.chakra.text("Portfolio", font_size="2em"),
        rx.chakra.text("davidarenasr@gmail.com "),
        rx.chakra.text("team@eventeducation.org"), 
        rx.chakra.image(
            src="/logo.svg", width="200px", height="auto"
    ), 
        rx.chakra.divider(border_color="black"),
        rx.chakra.text("Projectos", font_size="3em"),
        rx.chakra.text("¡Participa junto a tu equipo de trabajo en el desarrollo de proyectos Steam!"),
        rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.button("Click Me"),
            bg="Silver",
            border_radius="10px",
            border_color="black",
            border_width="thick",
            padding=5,
            ),
        rx.chakra.box(  
        rx.chakra.button("Click Me"),
            bg="Silver",
            border_radius="10px",
            border_color="black",
            border_width="thick",
            padding=5,
            ),
        rx.chakra.box(  
        rx.chakra.button("Click Me"),
            bg="Silver",
            border_radius="10px",
            border_color="black",
            border_width="thick",
            padding=5,
            ),
        )
    )
