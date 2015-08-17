# -*- encoding: utf-8 -*-

CHAR = {
    'max_length': 255,
    'default': '',
}

NULL = {
    'blank': True,
    'null': True
}

CHARN = {
    'blank': True,
    'null': True,
    'max_length': 255
}

# Determina o default para campos decimais
DECIMAL = {
    'max_digits': 12,
    'decimal_places': 2,
    'default': 0.00,
}
