from typing import Literal

# Which rapidfuzz scorer to use?
# https://rapidfuzz.github.io/RapidFuzz/Usage/fuzz.html
# Have only tested "token_sort_ratio" for my use cases.
# Others are likely viable, just need to be able to explain use cases clearly.
FuzzScorer = Literal["token_sort_ratio"]

# What happens if a matching entity is not found for key?
# By default, 'raise' is set in FuzzType.
# raise: raises an exception if no matching entity found
# none: sets value to None if no matching entity found
# allow: passes through key
NotFoundMode = Literal["raise", "none", "allow"]

# What happens if there is a tie?
# By default, 'raise' is set in FuzzStr.
# raise: raise an exception if two elements are tied without Entity.priority
# alphabetical: use Entity.name if Entity.priority not set to select item
TiebreakerMode = Literal["raise", "alphabetical"]

# Which Pydantic validator mode?
# https://docs.pydantic.dev/latest/concepts/validators/
# Only 'before' has been tested, 'plain' may work with no changes.
# Refactoring probably required for 'after' and 'wrap'.
ValidatorMode = Literal["before"]  # ... , "after", "plain", "wrap"]
