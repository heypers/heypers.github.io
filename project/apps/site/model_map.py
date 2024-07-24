from .models import Information, Character, Object, Protocol, Location, Lore, Plot, Department, Document, Organization, Group, Technology

MODEL_MAP = {
    'information': Information,
    'character': Character,
    'object': Object,
    'protocol': Protocol,
    'lore': Lore,
    'plot': Plot,
    'location': Location,
    'department': Department,
    'organization': Organization,
    'group': Group,
    'technology': Technology,
    'document': Document
}
