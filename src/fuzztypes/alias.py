from typing import Iterable

from . import NamedEntity, EntityDict, AbstractType, MatchList, const
from .name import NameLookup


def Alias(
    source: Iterable,
    *,
    case_sensitive: bool = False,
    examples: list = None,
    notfound_mode: const.NotFoundMode = "raise",
    tiebreaker_mode: const.TiebreakerMode = "raise",
    validator_mode: const.ValidatorMode = "before",
) -> AbstractType:
    """
    Alias is a type that will match to an Entity

    :param source: Am iterable of Entities or string
    :param case_sensitive:
    :param examples:
    :param notfound_mode:
    :param tiebreaker_mode:
    :param validator_mode:
    :return:
    """
    lookup = AliasLookup(
        source,
        case_sensitive=case_sensitive,
        tiebreaker_mode=tiebreaker_mode,
    )
    return AbstractType(
        lookup,
        examples=examples,
        input_type=str,
        notfound_mode=notfound_mode,
        validator_mode=validator_mode,
    )


def AliasCasedStr(
    source: Iterable,
    *,
    examples: list = None,
    notfound_mode: const.NotFoundMode = "raise",
    tiebreaker_mode: const.TiebreakerMode = "raise",
    validator_mode: const.ValidatorMode = "before",
):
    return Alias(
        source,
        examples=examples,
        case_sensitive=True,
        notfound_mode=notfound_mode,
        tiebreaker_mode=tiebreaker_mode,
        validator_mode=validator_mode,
    )


class AliasLookup(NameLookup):
    def __init__(
        self,
        source: Iterable,
        *,
        case_sensitive: bool,
        tiebreaker_mode: const.TiebreakerMode,
    ):
        super().__init__(
            source,
            case_sensitive=case_sensitive,
            tiebreaker_mode=tiebreaker_mode,
        )
        self.alias_entity_dict = EntityDict(case_sensitive, tiebreaker_mode)

    def _add(self, entity: NamedEntity):
        super(AliasLookup, self)._add(entity)

        for alias in entity.aliases:
            self.alias_entity_dict[alias] = entity

    def _get(self, key: str) -> MatchList:
        matches = super(AliasLookup, self)._get(key)
        if not matches:
            entity = self.alias_entity_dict[key]
            if entity:
                matches.set(key=key, entity=entity, is_alias=True)
        return matches
