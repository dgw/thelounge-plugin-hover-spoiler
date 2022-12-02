# coding = utf-8

import textwrap

DARK_REVEAL = [
    0, 3, 7, 8, 9, 10, 11, 14, 15,
]

LIGHT_REVEAL = [
    1, 2, 4, 5, 6, 12, 13,
]

LIGHT_REVEAL.extend(list(range(16,42)))
DARK_REVEAL.extend(list(range(42,47)))
LIGHT_REVEAL.extend(list(range(47,53)))
DARK_REVEAL.extend(list(range(53,59)))
LIGHT_REVEAL.extend(list(range(59,65)))
DARK_REVEAL.extend(list(range(65,72)))
LIGHT_REVEAL.extend(list(range(72,74)))
DARK_REVEAL.extend(list(range(74,88)))
LIGHT_REVEAL.extend(list(range(88,95)))
DARK_REVEAL.extend(list(range(95,99)))

SELECTOR_TEMPLATE = '.content:hover .irc-fg{0}.irc-bg{0}'

dark_selectors = [SELECTOR_TEMPLATE.format(i) for i in DARK_REVEAL]
light_selectors = [SELECTOR_TEMPLATE.format(i) for i in LIGHT_REVEAL]

dark_selectors = ', '.join(dark_selectors)
light_selectors = ', '.join(light_selectors)

dark_selectors = '\n'.join(textwrap.wrap(dark_selectors, 72))
light_selectors = '\n'.join(textwrap.wrap(light_selectors, 72))

print(dark_selectors + ' {\n  color: #000;\n}')
print(light_selectors + ' {\n  color: #fff;\n}')
