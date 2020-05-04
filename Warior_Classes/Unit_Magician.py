from .Unit import Unit

class Unit_Magician (Unit):
    buy_cost = 400
    name = "Magician"

    health_default = 3500
    _general_health_default_with_equip = 0
    health_in_fight = health_default
    _health_in_fight_with_equip = 0

    power_default = 700
    _power_with_equip = 0
    _power_for_fight = 0

    status = "Alive"
    level = 0
    experiance = 0
    abilyty_recharger_moves = 3  # Сколько ходов до перезерядки способности(ходов объекта)
    poison_longness = 0
    chance_critical_hit = 0.1
    stuned = 0
    super = "Poison all enemy's units"

    helmet_name = "Helmet"
    helmet_value = 0

    boots_name = "Boots"
    boots_value = 0

    shield_name = "Shield"
    shield_value = 0

    bodyarmor_name = "Bodyarmor"
    bodyarmor_value = 0

    weapon_name = "Stick"
    weapon_value = 0

    ability_item_name = "Poison all enemy's units"
    ability_item_value = 0.05