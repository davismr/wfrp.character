from wfrp.character.data.careers.academics import ACADEMIC_CLASS_DATA
from wfrp.character.data.careers.burghers import BURGHERS_CLASS_DATA
from wfrp.character.data.careers.courtiers import COURTIERS_CLASS_DATA
from wfrp.character.data.careers.peasants import PEASANTS_CLASS_DATA
from wfrp.character.data.careers.rangers import RANGERS_CLASS_DATA
from wfrp.character.data.careers.riverfolk import RIVERFOLK_CLASS_DATA
from wfrp.character.data.careers.rogues import ROGUES_CLASS_DATA
from wfrp.character.data.careers.seafarer import SEAFARER_CLASS_DATA
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CAREER_BY_CLASS
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CLASS_DATA
from wfrp.character.data.careers.warriors import WARRIORS_CLASS_DATA

CAREER_DATA = (
    ACADEMIC_CLASS_DATA
    | BURGHERS_CLASS_DATA
    | COURTIERS_CLASS_DATA
    | PEASANTS_CLASS_DATA
    | RANGERS_CLASS_DATA
    | RIVERFOLK_CLASS_DATA
    | ROGUES_CLASS_DATA
    | WARRIORS_CLASS_DATA
)

ALL_CAREER_DATA = CAREER_DATA | UP_IN_ARMS_CLASS_DATA

CAREER_DATA_WITH_SEAFARER = (
    ACADEMIC_CLASS_DATA
    | BURGHERS_CLASS_DATA
    | COURTIERS_CLASS_DATA
    | PEASANTS_CLASS_DATA
    | RANGERS_CLASS_DATA
    | SEAFARER_CLASS_DATA
    | ROGUES_CLASS_DATA
    | WARRIORS_CLASS_DATA
)

ALL_CAREER_DATA_WITH_SEAFARER = CAREER_DATA_WITH_SEAFARER | UP_IN_ARMS_CLASS_DATA

CAREER_BY_CLASS = (
    {career: "Academics" for career in ACADEMIC_CLASS_DATA}
    | {career: "Burghers" for career in BURGHERS_CLASS_DATA}
    | {career: "Courtiers" for career in COURTIERS_CLASS_DATA}
    | {career: "Peasants" for career in PEASANTS_CLASS_DATA}
    | {career: "Rangers" for career in RANGERS_CLASS_DATA}
    | {career: "Riverfolk" for career in RIVERFOLK_CLASS_DATA}
    | {career: "Rogues" for career in ROGUES_CLASS_DATA}
    | {career: "Warriors" for career in WARRIORS_CLASS_DATA}
    | UP_IN_ARMS_CAREER_BY_CLASS
)

CAREER_BY_CLASS_WITH_SEAFARER = (
    {career: "Academics" for career in ACADEMIC_CLASS_DATA}
    | {career: "Burghers" for career in BURGHERS_CLASS_DATA}
    | {career: "Courtiers" for career in COURTIERS_CLASS_DATA}
    | {career: "Peasants" for career in PEASANTS_CLASS_DATA}
    | {career: "Rangers" for career in RANGERS_CLASS_DATA}
    | {career: "Seafarer" for career in SEAFARER_CLASS_DATA}
    | {career: "Rogues" for career in ROGUES_CLASS_DATA}
    | {career: "Warriors" for career in WARRIORS_CLASS_DATA}
    | UP_IN_ARMS_CAREER_BY_CLASS
)
