from wfrp.character.data.careers.academics import ACADEMIC_CLASS_DATA
from wfrp.character.data.careers.burghers import BURGHERS_CLASS_DATA
from wfrp.character.data.careers.courtiers import COURTIERS_CLASS_DATA
from wfrp.character.data.careers.peasants import PEASANTS_CLASS_DATA
from wfrp.character.data.careers.rangers import RANGERS_CLASS_DATA
from wfrp.character.data.careers.riverfolk import RIVERFOLK_CLASS_DATA
from wfrp.character.data.careers.rogues import ROGUES_CLASS_DATA
from wfrp.character.data.careers.warriors import WARRIORS_CLASS_DATA

CAREER_DATA = {
    **ACADEMIC_CLASS_DATA,
    **BURGHERS_CLASS_DATA,
    **COURTIERS_CLASS_DATA,
    **PEASANTS_CLASS_DATA,
    **RANGERS_CLASS_DATA,
    **RIVERFOLK_CLASS_DATA,
    **ROGUES_CLASS_DATA,
    **WARRIORS_CLASS_DATA,
}
