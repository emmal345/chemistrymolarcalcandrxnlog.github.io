from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

set_website_titel("chemisty molar calc & reaction checke")
set_site_information(author="Emma Lewis", description="Molarity calculator and logged reaction finder",
    sources=["Periodic table (for atomic masses and element symbols)","Drafter docs"], 
    planning=["Emma Lewis - CS1 Final Project0_Pick a Problem.pdf", 
              "Emma Lewis - CS1 Final Project1_Design (1)(1)(1).pdf"],
    links=["https://github.com/emmal345/chemisty_molar_calc_rxn_checker_site"],)
hide_debug_information()

#### list logged reactions ####
REACTIONS: list[list] = [
    ["HCl + NaOH -> NaCl + H2O", True],
    ["HCl + NaHCO3 -> NaCl + H2O + CO2", True],
    ["AgNO3 + NaCl -> AgCl + NaNO3", True],
    ["HCl + Zn -> ZnCl2 + H2", True],
    ["CaCl2 + Na2CO3 -> CaCO3 + NaCl", True],
    ["CuSO4 + Zn -> ZnSO4 + Cu", True],
    ["CH3COOH + NaHCO3 -> NaCH3COO + H2O + CO2", True],
    ["KCl + NaNO3 -> No reaction", False],
]

#### list of elements ####
ELEMENT_SYMBOLS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co",
                "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh",
                "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
                "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu",
                "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
                "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
                "Tl", "Pb", "Bi", "Po", "At", "Rn",
                "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am",
                "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No",
                "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",]

#### list of atomic masses, in respective order to element symbols (g/mol). ####
ATOMIC_MASSES = [1.00794, 4.003, 6.941, 9.012182, 10.811,
                12.0107, 14.00674, 15.9994, 18.9984032, 20.1797,
                22.989770, 24.3050, 26.981538, 28.0855, 30.973761,
                32.066, 35.4527, 39.948, 39.0983, 40.078,
                44.955910, 47.867, 50.9415, 51.9961, 54.938049,
                55.845, 58.933200, 58.6934, 63.546, 65.39,
                69.723, 72.61, 74.92160, 78.96, 79.904, 83.80,
                85.4678, 87.62, 88.90585, 91.224, 92.90638,
                95.94, 98, 101.07, 102.90550, 106.42, 107.8682,
                112.411, 114.818, 118.710, 121.760, 127.60, 126.90447,
                131.29, 132.90545, 137.327, 138.9055, 140.116,
                140.90765, 144.24, 145, 150.36, 151.964, 157.25,
                158.92534, 162.50, 164.9302, 167.26, 168.93421,
                173.04, 174.967, 178.49, 180.9479, 183.84, 186.207,
                190.23, 192.217, 195.078, 196.96655, 200.59,
                204.3833, 207.2, 208.98038, 209., 210., 222.,
                223., 226., 227., 232.0381, 231.03588, 238.0289,
                237., 244., 243., 247., 247., 251., 252., 257.,
                258., 259., 262., 261., 262., 263., 262., 265., 266.,]
    
COMMON_FORMULAS: list[str] = ["KOH", "NaOH", "LiOH", "NaCl", "KCl", "HCl", "HNO3", "H2SO4",
                              "NaHCO3", "CaCl2", "CaCO3", "MgSO4", "KNO3", "AgNO3", "CuSO4",]
TOOL_CHOICES: list[str] = ["Calculate Molarity", "Search Reactions"]
MAX_VOLUME_ML: int = 1000  # the top of the volume Meter's scale
CALCULATION_HEADER: list[str] = ["Compound", "Molarity (M)", "Volume (mL)", "Grams needed",]
REACTION_HEADER: list[str] = ["Reactants", "Products", "Result"]

#### Sizes and colors (SVG pixels) for the before/after picture of a solution ####
SVG_WIDTH: int = 480
SVG_HEIGHT: int = 260
BEAKER_WIDTH: int = 100
BEAKER_HEIGHT: int = 140
BEAKER_BOTTOM: int = 210
BEFORE_LEFT: int = 170  # left edge of the "before" beaker (water)
AFTER_LEFT: int = 360  # left edge of the "after" beaker (solution)
MIN_WATER_HEIGHT: float = 14.0  # tiny volumes still show a visible layer
WATER_COLOR: str = "#8fd3f4"
SOLUTION_COLOR: str = "#b7e3f7"
DOT_COLOR: str = "#1f6fa8"
# Pile of solid solute: top-left corner of each small crystal
CRYSTAL_X: list[int] = [28, 42, 56, 70, 84, 35, 49, 63, 77, 49, 63]
CRYSTAL_Y: list[int] = [180, 180, 180, 180, 180, 170, 170, 170, 170, 160, 160]
# Dissolved particles: how far across and down the liquid each one floats
DOT_ACROSS: list[float] = [0.2, 0.5, 0.8, 0.35, 0.65, 0.15, 0.5, 0.85, 0.3, 0.7]
DOT_DOWN: list[float] = [0.25, 0.15, 0.3, 0.5, 0.55, 0.75, 0.8, 0.7, 0.88, 0.9]

#### DATACLASSES ####

@dataclass
class PartsIn:
    """
    element and how many atoms appear in formula.

    Parameters(fields):symbol (str): element symbol
                       amount (int): how many atoms of that element
    """
    symbol: str
    amount: int


@dataclass
class MolarCalculator:
    """
    Finished molarity calculation
    Parameters(fields):solute (str): the formula of the compound
                       molarity (float): the desired molarity in M
                       volume_mL (float): the final volume in mL
                       grams_solute (float): the grams of solute needed
    """
    solute: str
    molarity: float
    volume_mL: float
    grams_solute: float

@dataclass
class Reaction:
    """
    Reaction that someone has already tested.
    Parameters (fields):reactants (list[str]): reactant names, lowercase and sorted
                        product (str): the products
                        effective (bool): True if  reaction increased efficiency
    """
    reactants: list[str]
    product: str
    effective: bool

@dataclass
class State:
    """
    Way for website to store, update, remember
    Parameters (fields): calculations (list[MolarCalculator]): past molarity calculations
                         reactions (list[Reaction]): log of tested reactions
                         lastGrams (float): grams from the most recent calculation
                         lastMessage (str): the message shown at the top of a page
    """
    calculations: list[MolarCalculator]
    reactions: list[Reaction]
    lastGrams: float
    lastMessage: str

def sort_names(names: list[str]) -> list[str]:
    """
    Returns new list of names in alphabetical order, finds the smallest name in the unsorted part and swaps
    into the next open spot
    Parameters:names (list[str])
    Returns:list[str]
    """
    sorted_names: list[str] = []
    for name in names:
        sorted_names.append(name)  # copy, so the caller's list stays the same
    for first in range(len(sorted_names)):
        smallest = first  # position of the smallest name seen so far
        next_one = first + 1
        for current in range(next_one, len(sorted_names)):
            if sorted_names[current] < sorted_names[smallest]:
                smallest = current
        saved = sorted_names[first]  # swap using a temporary variable
        sorted_names[first] = sorted_names[smallest]
        sorted_names[smallest] = saved
    return sorted_names

def convert_reactant(reactants: str) -> list[str]:
    """
    Turns typed reactants into lowercase, sorted names with no blanks.
    Parameters: reactants (str)
    Returns:list[str]
    """
    converted_reactants: list[str] = []
    for reactant in reactants.split(","):
        name = reactant.strip().lower()
        if name != "":
            converted_reactants.append(name)
    return sort_names(converted_reactants)

def split_reaction(entry: str) -> list[str]:
    """
    Splits reaction text at the "->" arrow into reactants and products, Returns an empty list if the text has no arrow.
    Parameters:entry (str)
    Returns:list[str]
    """
    if "->" not in entry:
        return []
    parts_reaction = entry.split("->")
    reactants = parts_reaction[0].strip()
    products = parts_reaction[1].strip()
    return [reactants, products]

def find_reactions(reactions: list[Reaction], want: list[str]) -> list[Reaction]:
    """
    Finds logged reaction whose reactants equal the wanted list.
    Parameters:reactions (list[Reaction]), want (list[str])
    Returns:list[Reaction]
    """
    match: list[Reaction] = []
    for reaction in reactions:
        if reaction.reactants == want:
            match.append(reaction)
    return match

def efficiency_label(effective: bool) -> str:
    """
    Turns reaction's True/False result into a word.
    Parameters:effective (bool)
    Returns:str
    """
    if effective:
        return "efficient"
    return "not efficient"

def reaction_description(reaction: Reaction) -> str:
    """
    Writes readable line describing a logged reaction.
    Parameters:reaction (Reaction)
    Returns:str
    """
    reactants = " + ".join(reaction.reactants)
    label = efficiency_label(reaction.effective)
    return reactants + " -> " + reaction.product + " (" + label + ")"

def calculation_rows(calculations: list[MolarCalculator]) -> list[list]:
    """
    Builds one table row per past molarity calculation.
    Parameters:calculations (list[MolarCalculator])
    Returns: list[list]
    """
    rows: list[list] = []
    for calculation in calculations:
        rows.append([
            calculation.solute,
            calculation.molarity,
            calculation.volume_mL,
            calculation.grams_solute,
        ])
    return rows
def reaction_rows(reactions: list[Reaction]) -> list[list]:
    """
    Builds one table row per logged reaction.Parameters: reactions (list[Reaction])
    Returns:list[list]: one row per reaction.
    """
    rows: list[list] = []
    for reaction in reactions:
        rows.append([
            " + ".join(reaction.reactants),
            reaction.product,
            efficiency_label(reaction.effective),
        ])
    return rows

def show_table(rows: list[list], header: list[str], empty_text: str) -> list:
    """
    Shows Table for the rows, short message if there are none.
    Advanced technique :Drafter's Table component draws a grid from a list of rows and a list of column names.
    Parameters:
        rows (list[list]): the table rows.
        header (list[str]): the column names.
        empty_text (str): the message to show when there are no rows.
    Returns:
        list: a list holding one Table, or holding only empty_text.
    """
    if len(rows) == 0:
        return [empty_text]
    return [Table(rows, header)]

def clamp_volume(volume_ml: float) -> float:
    """
    Caps volume at MAX_VOLUME_ML so the Meter and picture stay in range.
    Parameters:volume_ml (float)
    Returns:float
    """
    if volume_ml > MAX_VOLUME_ML:
        return float(MAX_VOLUME_ML)
    return volume_ml


def water_height(volume_ml: float) -> float:
    """
    Description:
        Work out how tall (in pixels) the liquid is drawn for a volume.
    Parameters:
        volume_ml (float): the volume of liquid in milliliters.
            Argument example: 500.0
    Returns:
        float: the liquid height in pixels, from MIN_WATER_HEIGHT (14.0)
            up to BEAKER_HEIGHT (140). Example result: 70.0
    """
    scaled = BEAKER_HEIGHT * clamp_volume(volume_ml) / MAX_VOLUME_ML
    if scaled < MIN_WATER_HEIGHT:
        return MIN_WATER_HEIGHT
    return round(scaled, 1)

def svg_text(x: int, y: int, words: str, size: int) -> str:
    """
    Description:
        Build one line of SVG text centered on x, drawn in the page's text
        color.
    Parameters:
        x (int): the horizontal center of the text. Argument example: 145
        y (int): the vertical position of the text. Argument example: 30
        words (str): the text to show. Argument example: "Before"
        size (int): the font size in pixels. Argument example: 20
    Returns:
        str: one SVG <text> tag.
    """
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" ' f'fill="currentColor">{words}</text>')


def make_beaker(left_x: int, level: float, liquid_color: str) -> str:
    """
    Description:
        Build an open beaker filled with liquid to the given height.
    Parameters:
        left_x (int): the left edge of the beaker. Argument example: 170
        level (float): the liquid height in pixels. Argument example: 70.0
        liquid_color (str): the liquid's color as a hex code.
            Argument example: "#8fd3f4"
    Returns:
        str: SVG tags for the liquid and the beaker outline.
    """
    top_y = round(BEAKER_BOTTOM - level, 1)
    right_x = left_x + BEAKER_WIDTH
    rim_y = BEAKER_BOTTOM - BEAKER_HEIGHT
    liquid = (
        f'<rect x="{left_x + 2}" y="{top_y}" width="{BEAKER_WIDTH - 4}" '
        f'height="{round(level - 2, 1)}" fill="{liquid_color}"/>'
    )
    outline = (
        f'<path d="M{left_x} {rim_y} L{left_x} {BEAKER_BOTTOM} '
        f'L{right_x} {BEAKER_BOTTOM} L{right_x} {rim_y}" '
        'fill="none" stroke="currentColor" stroke-width="3"/>'
    )
    return liquid + outline

def make_crystals() -> str:
    """
    Description:
        Build a dish holding a pile of solid solute, using CRYSTAL_X and
        CRYSTAL_Y for the position of each crystal.
    Parameters:
        none. Argument example: make_crystals()
    Returns:
        str: SVG tags for the dish and every crystal.
    """
    dish = (
        '<rect x="20" y="190" width="100" height="20" '
        'fill="none" stroke="currentColor" stroke-width="3"/>'
    )
    crystals = ""
    for position in range(len(CRYSTAL_X)):
        crystals = crystals + (
            f'<rect x="{CRYSTAL_X[position]}" y="{CRYSTAL_Y[position]}" '
            'width="12" height="10" fill="white" stroke="gray"/>'
        )
    return dish + crystals


def make_dots(left_x: int, level: float) -> str:
    """
    Description:
        Build the dissolved particles floating inside the liquid, using
        DOT_ACROSS and DOT_DOWN for where each one sits.
    Parameters:
        left_x (int): the left edge of the beaker. Argument example: 360
        level (float): the liquid height in pixels. Argument example: 70.0
    Returns:
        str: SVG <circle> tags, one per particle.
    """
    top_y = BEAKER_BOTTOM - level
    dots = ""
    for position in range(len(DOT_ACROSS)):
        dot_x = left_x + 2 + DOT_ACROSS[position] * (BEAKER_WIDTH - 4)
        dot_y = top_y + DOT_DOWN[position] * level
        dots = dots + (
            f'<circle cx="{round(dot_x, 1)}" cy="{round(dot_y, 1)}" r="3" '
            f'fill="{DOT_COLOR}"/>'
        )
    return dots

def make_arrow() -> str:
    """
    Description:
        Build the arrow between the before and after pictures.
    Parameters:
        none. Argument example: make_arrow()
    Returns:
        str: SVG tags for the arrow's line and head.
    """
    return ( '<line x1="290" y1="140" x2="322" y2="140" ''stroke="currentColor" stroke-width="3"/>'
        '<polygon points="322,131 338,140 322,149" fill="currentColor"/>')


def make_before_side(formula: str, grams: float, volume_ml: float) -> str:
    """
    Description:
        Build the "before" side: the solid solute plus a beaker of water.
    Parameters:
        formula (str): the compound's formula. Argument example: "KOH"
        grams (float): the grams of solute. Argument example: 2.805
        volume_ml (float): the final volume in mL. Argument example: 500.0
    Returns:
        str: SVG tags for the whole "before" side.
    """
    level = water_height(volume_ml)
    return (svg_text(145, 30, "Before", 20)+ make_crystals() + svg_text(145, 160, "+", 28)+ 
        make_beaker(BEFORE_LEFT, level, WATER_COLOR)+ svg_text(70, 232, str(grams) + " g " + formula, 13)
        + svg_text(70, 250, "(solid)", 12)+ svg_text(220, 232, "Water", 13)+ 
        svg_text(220, 250, "(to " + str(volume_ml) + " mL)", 12))

def make_after_side(formula: str, molarity: float, volume_ml: float) -> str:
    """
    Description:
        Build the "after" side: one beaker of dissolved solution.
    Parameters:
        formula (str): the compound's formula. Argument example: "KOH"
        molarity (float): the molarity in M. Argument example: 0.1
        volume_ml (float): the final volume in mL. Argument example: 500.0
    Returns:
        str: SVG tags for the whole "after" side.
    """
    level = water_height(volume_ml)
    return (svg_text(410, 30, "After", 20)+ make_beaker(AFTER_LEFT, level,SOLUTION_COLOR)+ make_dots(AFTER_LEFT, level)
        +svg_text(410, 232, str(molarity) + " M " + formula, 13)+ svg_text(410, 250,str(volume_ml)+" mL solution", 12))


def make_solution_svg(formula: str, grams: float, molarity: float, volume_ml: float) -> str:
    """
    Description:
        Build the full before/after picture as SVG text. The formula has
        already passed molar_mass(), so it only holds valid element symbols
        and digits and is safe to place inside the SVG text.
    Parameters:
        formula (str): the compound's formula. Argument example: "KOH"
        grams (float): the grams of solute. Argument example: 2.805
        molarity (float): the molarity in M. Argument example: 0.1
        volume_ml (float): the final volume in mL. Argument example: 500.0
    Returns:
        str: SVG tags for the before side, the arrow, and the after side.
    """
    return (make_before_side(formula, grams, volume_ml)+ make_arrow()+ make_after_side(formula, molarity, volume_ml))

def make_solution_picture(formula: str, grams: float, molarity: float, volume_ml: float) -> SVG:
    """
    Description:
        Wrap the before/after picture in a Drafter SVG component so it can
        go on a page.
    Advanced technique (not covered in class):
        Drafter's SVG component draws shapes (rect, path, circle, text)
        from a string of SVG tags.
    Parameters:
        formula (str): the compound's formula. Argument example: "KOH"
        grams (float): the grams of solute. Argument example: 2.805
        molarity (float): the molarity in M. Argument example: 0.1
        volume_ml (float): the final volume in mL. Argument example: 500.0
    Returns: SVG: the picture, ready to place in a Page's content list.
    """
    return SVG(
        make_solution_svg(formula, grams, molarity, volume_ml),
        width=SVG_WIDTH,
        height=SVG_HEIGHT,
        viewBox=f"0 0 {SVG_WIDTH} {SVG_HEIGHT}",)

def make_reactions() -> list[Reaction]:
    """
    Builds starter Reaction list from the REACTIONS file
    Returns:list[Reaction]
    """
    list_reactions: list[Reaction] = []
    for entry in REACTIONS:
        parts_reaction = split_reaction(entry[0])  # [reactants, products]
        if len(parts_reaction) == 2:
            reaction_text = parts_reaction[0].replace("+", ",")
            list_reactions.append(Reaction(convert_reactant(reaction_text), parts_reaction[1], entry[1], ))
    return list_reactions

def start_state() -> State:
    """
    Builds State the site starts with.
    Parameters:None
    Returns:State
    """
    return State([], make_reactions(), 0.0, "")

def fix_formula_case(text: str) -> str:
    """
    Fixs capitalization of a common formula koh -> KOH
    Compares the typed text to COMMON_FORMULAS, if nothingmatchesthe typed text returned unchanged
    Parameters:text (str)
    Returns: str
    """
    cleaned = text.strip()
    for formula in COMMON_FORMULAS:
        if formula.lower() == cleaned.lower():
            return formula
    return cleaned

def sort_formula(formula: str) -> list[PartsIn]:
    """
    Breaks formula into parts, e.g. "CaCl2" -> Ca x1, Cl x2.
    Parameters:formula (str)
    Returns:list[PartsIn]
    """
    parts: list[PartsIn] = []
    index = 0
    while index < len(formula):
        symbol = formula[index]  # first letter of the element symbol
        index = index + 1
        while index < len(formula) and formula[index].islower():
            symbol = symbol + formula[index]  # second letter, like the "l" in "Cl"
            index = index + 1
        digits = ""
        while index < len(formula) and formula[index].isdigit():
            digits = digits + formula[index]
            index = index + 1
        default_amount = 1  # no number after a symbol means one atom
        if digits != "":
            default_amount = int(digits)
        parts.append(PartsIn(symbol, default_amount))
    return parts

def molar_mass(formula: str) -> float:
    """
    Adds the atomic masses of every atom in a formula.
    Parameters:formula (str)
    Returns:float
    """
    parts = sort_formula(formula)
    if len(parts) == 0:
        return 0.0  # empty text is not a formula
    total = 0.0
    for part in parts:
        if part.symbol not in ELEMENT_SYMBOLS:
            return 0.0  # unknown symbol; the route checks for this
        position = ELEMENT_SYMBOLS.index(part.symbol)
        total = total + ATOMIC_MASSES[position] * part.amount
    return total

def grams_needed(molarity: float, volume_ml: float, mass_per_mole: float) -> float:
    """
    Find the grams of solute for a solution: M x liters x molar mass.
    Parameters: molarity (float), volume_ml (float), mass_per_mole (float)
    Returns: float
    """
    return molarity * (volume_ml / 1000) * mass_per_mole


def is_positive(text: str) -> bool:
    """
    Checks if text is number greater than zero.
    Parameters:text (str)
    Returns:bool
    """
    cleaned = text.strip()
    digits_only = cleaned.replace(".", "", 1)
    if not digits_only.isdigit():
        return False
    return float(cleaned) > 0
    
#### ROUTE FUNCTIONS ####

@route
def index(state: State) -> Page:
    """
    Home page - clears old message and lets user pick tool.
    Parameters:state (State)
    Returns:Page
    """
    state.lastMessage = ""
    return Page(state, [
        Header("Lab Helper"),
        "Quick molarity math and a check for reactions already tested.",
        HorizontalRule(),
        "What do you need?",
        LineBreak(),
        SelectBox("tool", TOOL_CHOICES, TOOL_CHOICES[0]),
        LineBreak(),
        Button("Go", choose_tool),
        Button("See all logged reactions", reaction_list), ])

@route
def choose_tool(state: State, tool: str) -> Page:
    """
    Sends user to the form that matches their menu choice.
    Parameters:state (State), tool (str)
    Returns: Page
    """
    if tool == TOOL_CHOICES[0]:
        return molarity_form(state)
    return search_form(state)

@route
def molarity_form(state: State) -> Page:
    """
    for the compound formula, desired molarity, and volume.
    Parameters:state (State)
    Returns:Page
    """
    return Page(state, [
        Header("Molarity Calculator"),
        state.lastMessage,
        LineBreak(),
        "Formula (e.g. KOH or CaCl2, capitals matter): ",
        TextBox("formula", "KOH"),
        LineBreak(),
        "Desired molarity (M): ",
        TextBox("molarity", "0.1"),
        LineBreak(),
        "Desired volume (mL): ",
        TextBox("volume_ml", "500"),
        LineBreak(),
        LineBreak(),
        Button("Calculate", calculate_molarity),
        Button("Home", index),])

@route
def calculate_molarity(state: State, formula: str, molarity: str, volume_ml: str) -> Page:
    """
    Checks inputs, finds grams needed, saves calculation, shows the result with the before/after picture.
    Advanced technique: Drafter's Meter draws a gauge on a scale from min to max, 
                        and HorizontalRule draws a divider line between sections.
    Parameters:state (State), formula (str), molarity (str), volume_ml (str)
    Returns: Page: the result page
    """
    if not is_positive(molarity) or not is_positive(volume_ml):
        state.lastMessage = "Error: molarity and volume must be numbers above zero."
        return molarity_form(state)
    solute = fix_formula_case(formula)
    mass_per_mole = molar_mass(solute)
    if mass_per_mole == 0.0:
        state.lastMessage = f"Error: '{solute}' is not a formula I recognize."
        return molarity_form(state)
    molarity_value = float(molarity)
    volume_value = float(volume_ml)
    grams = round(grams_needed(molarity_value, volume_value, mass_per_mole), 3)
    state.calculations.append(
        MolarCalculator(solute, molarity_value, volume_value, grams)
    )
    state.lastGrams = grams
    state.lastMessage = (
        f"Weigh {grams} g of {solute}, then add water up to {volume_value} mL."
    )
    return Page(state, [
        Header("Result"),
        state.lastMessage,
        LineBreak(),
        Header("Before and after", 2),
        make_solution_picture(solute, grams, molarity_value, volume_value),
        LineBreak(),
        "Final volume (0 to " + str(MAX_VOLUME_ML) + " mL scale): ",
        Meter(clamp_volume(volume_value), min=0, max=MAX_VOLUME_ML),
        HorizontalRule(),
        Header("Past calculations", 2),
    ] + show_table(
        calculation_rows(state.calculations),
        CALCULATION_HEADER,
        "No calculations yet.",
    ) + [
        Button("Another calculation", molarity_form),
        Button("Clear history", clear_history),
        Button("Home", index), ])

@route
def clear_history(state: State) -> Page:
    """
    Erase the saved molarity calculations and start fresh.
    Parameters: state (State)
    Returns: Page
    """
    state.calculations = []
    state.lastGrams = 0.0
    state.lastMessage = "History cleared."
    return molarity_form(state)

@route
def search_form(state: State) -> Page:
    """
    For typing comma-separated reactants.
    Parameters:state (State)
    Returns: Page - the rxn search form.
    """
    return Page(state, [
        Header("Has this reaction been tried?"),
        state.lastMessage,
        LineBreak(),
        "Reactants, separated by commas (e.g. HCl, NaOH): ",
        TextBox("reactants", ""),
        LineBreak(),
        LineBreak(),
        Button("Search", search_reactions),
        Button("Home", index), ])

@route
def search_reactions(state: State, reactants: str) -> Page:
    """
    Looks for the typed reactants in the log and show what was found.
    Advanced technique (not covered in class): BulletedList shows a list of strings as bullet points from drafter
    Parameters: state (State), reactants (str)
    Returns:Page
    """
    wanted = convert_reactant(reactants)
    if len(wanted) == 0:
        state.lastMessage = "Error: type at least one reactant."
        return search_form(state)
    matches = find_reactions(state.reactions, wanted)
    lines: list[str] = []
    if len(matches) > 0:
        state.lastMessage = "Already tested! Results:"
        for match in matches:
            lines.append(reaction_description(match))
    else:
        state.lastMessage = "Not in the log yet. You could be the first to test it!"
    results: list = []
    if len(lines) > 0:
        results = [BulletedList(lines)]
    return Page(state, [
        Header("Search result"),
        state.lastMessage,
    ] + results + [
        Button("Log a reaction", log_form),
        Button("Search again", search_form),
        Button("Home", index), ])

@route
def log_form(state: State) -> Page:
    """
    Adding a tested reaction
    Parameters:state (State)
    Returns: Page
    """
    return Page(state, [
        Header("Log a Reaction"),
        state.lastMessage,
        LineBreak(),
        "Reactants, separated by commas: ",
        TextBox("reactants", ""),
        LineBreak(),
        "Product(s): ",
        TextBox("product", ""),
        LineBreak(),
        CheckBox("was_effective", False),
        "Was it effective?",
        LineBreak(),
        LineBreak(),
        Button("Save reaction", add_reaction),
        Button("Home", index),])

@route
def add_reaction(state: State, reactants: str, product: str, was_effective: bool) -> Page:
    """
    Saves a new Reaction to the log.
    Parameters:state (State), reactants (str), product (str), was_effective (bool)
    Returns: Page - the reaction list, or the form again with an error message.
    """
    wanted = convert_reactant(reactants)
    if len(wanted) == 0 or product.strip() == "":
        state.lastMessage = "Error: reactants and product are required."
        return log_form(state)
    state.reactions.append(
        Reaction(wanted, product.strip(), was_effective)
    )
    state.lastMessage = "Saved! Thanks for adding to the log."
    return reaction_list(state)

@route
def reaction_list(state: State) -> Page:
    """
    Show every reaction in the log as a table.
    Parameters: state (State)
    Returns: Page
    """
    return Page(state, [
        Header("All Logged Reactions"),
        state.lastMessage,
    ] + show_table(
        reaction_rows(state.reactions),
        REACTION_HEADER,
        "No reactions logged yet.",
    ) + [
        Button("Log another", log_form),
        Button("Home", index),
    ])


#### UNIT TESTS ####

assert_equal(len(ELEMENT_SYMBOLS), 109)
assert_equal(len(ATOMIC_MASSES), 109)
assert_equal(ATOMIC_MASSES[ELEMENT_SYMBOLS.index("Be")], 9.012182)
assert_equal(ATOMIC_MASSES[ELEMENT_SYMBOLS.index("Cl")], 35.4527)
assert_equal(ATOMIC_MASSES[ELEMENT_SYMBOLS.index("Mt")], 266.0)
assert_equal(ELEMENT_SYMBOLS[0], "H")
assert_equal(ELEMENT_SYMBOLS[108], "Mt")
assert_equal(fix_formula_case("koh"), "KOH")
assert_equal(fix_formula_case("CaCl2"), "CaCl2")
assert_equal(fix_formula_case("Xx"), "Xx")
assert_equal(round(molar_mass(fix_formula_case("koh")), 2), 56.11)
assert_equal(sort_formula("CaCl2"), [PartsIn("Ca", 1), PartsIn("Cl", 2)])
assert_equal(sort_formula("H2O"), [PartsIn("H", 2), PartsIn("O", 1)])
assert_equal(sort_formula(""), [])
assert_equal(round(molar_mass("NaCl"), 2), 58.44)
assert_equal(round(molar_mass("H2O"), 3), 18.015)
assert_equal(round(molar_mass("C6H12O6"), 2), 180.16)
assert_equal(molar_mass("Xx"), 0.0)
assert_equal(molar_mass("nacl"), 0.0)
assert_equal(molar_mass(""), 0.0)
assert_equal(round(grams_needed(0.1, 500, 58.44), 3), 2.922)
assert_equal(grams_needed(1.0, 1000, 10.0), 10.0)
assert_equal(is_positive("0.5"), True)
assert_equal(is_positive("abc"), False)
assert_equal(is_positive(""), False)
assert_equal(clamp_volume(500.0), 500.0)
assert_equal(clamp_volume(5000.0), 1000.0)
assert_equal(clamp_volume(1000.0), 1000.0)
assert_equal(sort_names(["naoh", "hcl", "agno3"]), ["agno3", "hcl", "naoh"])
assert_equal(sort_names([]), [])
assert_equal(sort_names(["a"]), ["a"])
assert_equal(len(CRYSTAL_X), len(CRYSTAL_Y))
assert_equal(len(DOT_ACROSS), len(DOT_DOWN))
assert_equal(water_height(1000.0), 140.0)
assert_equal(water_height(500.0), 70.0)
assert_equal(water_height(0.5), 14.0)
assert_equal(svg_text(5, 6, "hi", 12),
            '<text x="5" y="6" text-anchor="middle" font-size="12" ''fill="currentColor">hi</text>',)
assert_equal(make_beaker(170, 70.0, "red").count('fill="red"'), 1)
assert_equal(make_crystals().count("<rect"), len(CRYSTAL_X) + 1)  # + the dish
assert_equal(make_dots(360, 70.0).count("<circle"), len(DOT_ACROSS))
assert_equal(make_arrow().count("<polygon"), 1)
# make_before_side, make_after_side, make_solution_svg
assert_equal("2.805 g KOH" in make_before_side("KOH", 2.805, 500.0), True)
assert_equal("(to 500.0 mL)" in make_before_side("KOH", 2.805, 500.0), True)
assert_equal("0.1 M KOH" in make_after_side("KOH", 0.1, 500.0), True)
assert_equal("500.0 mL solution" in make_after_side("KOH", 0.1, 500.0), True)
assert_equal(make_solution_svg("KOH", 2.805, 0.1, 500.0).count("Before"), 1)
assert_equal(make_solution_svg("KOH", 2.805, 0.1, 500.0).count("After"), 1)
assert_equal(isinstance(make_solution_picture("KOH", 2.8, 0.1, 500.0), SVG), True)
assert_equal(convert_reactant("NaOH, HCl"), ["hcl", "naoh"])
assert_equal(convert_reactant(" , "), [])
assert_equal(len(find_reactions(make_reactions(), ["hcl", "naoh"])), 1)
assert_equal(len(find_reactions(make_reactions(), ["gold"])), 0)
assert_equal(efficiency_label(True), "efficient")
assert_equal(efficiency_label(False), "not efficient")
assert_equal(reaction_description(Reaction(["a"], "b", False)),"a -> b (not efficient)",)
assert_equal(calculation_rows([MolarCalculator("NaCl", 0.1, 500.0, 2.922)]),[["NaCl", 0.1, 500.0, 2.922]],)
assert_equal(calculation_rows([]), [])
assert_equal(reaction_rows([Reaction(["hcl", "naoh"], "NaCl + H2O", True)]),[["hcl + naoh", "NaCl + H2O", "efficient"]],)
assert_equal(show_table([], ["A"], "Nothing here."), ["Nothing here."])
assert_equal(len(show_table([["x"]], ["A"], "Nothing here.")), 1)
assert_equal(split_reaction("A + B -> C"), ["A + B", "C"])
assert_equal(split_reaction("no arrow here"), [])
assert_equal(len(make_reactions()), len(REACTIONS))
assert_equal(make_reactions()[0],Reaction(["hcl", "naoh"], "NaCl + H2O", True),)
assert_equal(make_reactions()[7].effective, False)
assert_equal(len(start_state().reactions), 8)
assert_equal(index(State([], [], 0.0, "old message")).state.lastMessage, "")
assert_equal(index(start_state()).content[0], Header("Lab Helper"))
assert_equal(choose_tool(start_state(), TOOL_CHOICES[0]).content[0],Header("Molarity Calculator"),)
assert_equal(choose_tool(start_state(), TOOL_CHOICES[1]).content[0],Header("Has this reaction been tried?"),)
assert_equal(molarity_form(start_state()).content[0], Header("Molarity Calculator"))
assert_equal(search_form(start_state()).content[0], Header("Has this reaction been tried?"))
assert_equal(log_form(start_state()).content[0], Header("Log a Reaction"))
assert_equal(len(calculate_molarity(start_state(), "NaCl", "0.1", "500").state.calculations), 1)
assert_equal(calculate_molarity(start_state(), "NaCl", "0.1", "500").content[0],Header("Result"),)
assert_equal(isinstance(calculate_molarity(start_state(), "NaCl", "0.1", "500").content[4], SVG),True,)
assert_equal(calculate_molarity(start_state(), "koh", "0.1", "500").state.lastGrams, 2.805)
assert_equal("Error" in calculate_molarity(start_state(), "KOH", "abc", "500").state.lastMessage,True,)
assert_equal(len(calculate_molarity(start_state(), "KOH", "abc", "500").state.calculations), 0)
assert_equal("not a formula"in calculate_molarity(start_state(), "Xx", "0.1", "500").state.lastMessage,True,)
assert_equal(clear_history(State([MolarCalculator("NaCl", 0.1, 500.0, 2.922)], [], 2.922, "")).state.calculations,[],)
assert_equal(clear_history(State([MolarCalculator("NaCl", 0.1, 500.0, 2.922)], [], 2.922, "")).state.lastGrams,0.0,)
assert_equal(search_reactions(start_state(), "NaOH, HCl").state.lastMessage,"Already tested! Results:",)
assert_equal("Not in the log" in search_reactions(start_state(), "gold").state.lastMessage,True,)
assert_equal("Error" in search_reactions(start_state(), " , ").state.lastMessage, True)
assert_equal(len(add_reaction(start_state(), "KOH, HCl", "KCl + H2O", True).state.reactions), 9)
assert_equal(add_reaction(start_state(), "KOH, HCl", "KCl + H2O", True).state.reactions[8],Reaction(["hcl", "koh"], 
"KCl + H2O", True),)
assert_equal(len(add_reaction(start_state(), "KOH, HCl", "  ", True).state.reactions), 8)
assert_equal(reaction_list(start_state()).content[0], Header("All Logged Reactions"))
assert_equal(len(reaction_list(start_state()).state.reactions), 8)
set_website_style("simple")

start_server(start_state())
