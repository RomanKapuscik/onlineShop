price_map: dict = {'apple': 1.0,
                   'orange': 2.0,
                   'nuts': 4.0}


def get_price(item: str):
    return price_map[item]
