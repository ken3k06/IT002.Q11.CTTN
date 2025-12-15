import random
from abc import ABC, abstractmethod
from enum import Enum


class ImmunityLevel(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Symptom(Enum):
    NONE = "Không triệu chứung"
    MILD = "Triệu chứng nhẹ"
    SEVERE = "Triệu chứng nặng"
    DEATH = "Tử vong"


class Virus(ABC):
    def __init__(self, name, avg_death_rate):
        self.name = name
        self.avg_deatg_rate = avg_death_rate

    @abstractmethod
    def get_symptom(self, symptom: Symptom) -> str:
        pass


class Covid19(Virus):
    def __init__(self):
        super().__init__("Covid-19", 0.04)

    def get_symptom(self, symptom: Symptom) -> str:
        if symptom == Symptom.MILD:
            return "Sốt, ho, mất vị giác"
        elif symptom == Symptom.SEVERE:
            return "Sốt cao, ho khan, khó thở"
        return ""


class Ebola(Virus):
    def __init__(self):
        super().__init__("Ebola", 0.5)

    def get_symptom(self, symptom: Symptom) -> str:
        if symptom == Symptom.MILD:
            return "Sốt, đau họng, đau cơ"
        elif symptom == Symptom.SEVERE:
            return "Nôn mửa, tiêu chảy, xuất huyết"
        return ""


class HIV(Virus):
    def __init__(self):
        super().__init__("HIV", 0.9)

    def get_symptom(self, symptom: Symptom) -> str:
        if symptom == Symptom.MILD:
            return "Cảm sốt"
        elif symptom == Symptom.SEVERE:
            return "Mệt mỏi cực độ, sưng hạch kéo dài, lở loét"
        return ""


class Host:
    def __init__(self, hostId: str, immunity_level: ImmunityLevel):
        self.hostId = hostId
        self.immunity_level = immunity_level
        self.is_vaccinated = False
        self.infection_results = {}


PROB_NO_VACCINE = {
    ImmunityLevel.HIGH: (0.5, 0.35, 0.15, 0.5),
    ImmunityLevel.MEDIUM: (0.1, 0.4, 0.5, 0.7),
    ImmunityLevel.LOW: (0.05, 0.15, 0.8, 1.0),
}

PROB_VACCINE = {
    ImmunityLevel.HIGH: (0.7, 0.25, 0.05, 0.4),
    ImmunityLevel.MEDIUM: (0.2, 0.5, 0.3, 0.6),
    ImmunityLevel.LOW: (0.1, 0.4, 0.5, 0.8),
}


def infect(host: Host, virus: Virus) -> Symptom:
    probs = PROB_VACCINE if host.is_vaccinated else PROB_NO_VACCINE
    p_none, p_mild, p_severe, p_death_factor = probs[host.immunity_level]
    r = random.random()
    if r < p_none:
        return Symptom.NONE
    elif r < p_none + p_mild:
        return Symptom.MILD
    elif r < p_none + p_mild + p_severe:
        return Symptom.SEVERE
    else:
        death_prob = p_death_factor * virus.avg_deatg_rate
        return Symptom.DEATH if random.random() < death_prob else Symptom.SEVERE


if __name__ == "__main__":
    viruses = [Covid19(), Ebola(), HIV()]
    host = Host("H001", ImmunityLevel.MEDIUM)
    for v in viruses:
        result = infect(host, v)
        print(f"{v.name}: {result.value}")
