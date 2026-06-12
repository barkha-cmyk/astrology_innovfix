# astrology_innovfix

Astrology chart generation and interpretation toolkit.

## Features

- Sun sign calculation for any date of birth
- Handles year-boundary signs (Capricorn: Dec 22 – Jan 19)

## Usage

```python
from datetime import date
from natal_chart import sun_sign

print(sun_sign(date(1990, 7, 15)))  # Cancer
print(sun_sign(date(1985, 1, 5)))   # Capricorn
```