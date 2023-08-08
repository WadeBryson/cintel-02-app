# Purpose: Provide user interaction options for the Nuclear Explostions Dataset.

from shiny import ui
from datetime import date

def get_NUKE_inputs():
    return ui.panel_sidebar(
        ui.h2("Nuclear Explosions Interactions"),
        ui.tags.hr(),
        ui.input_date_range(
            "NUCLEAR_EXPLOSIONS_YEAR_RANGE",
            "Enter Year Range",
            start=date(1949),
            end=date(2000),
        ),
    )
