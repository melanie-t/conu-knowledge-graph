class TermSeasons:
    FALL = 0
    WINTER = 1
    SUMMER = 2


class Term:
    def __init__(self, term_season, year):
        self.term_season = term_season
        self.year = year