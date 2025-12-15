import random
from abc import ABC, abstractmethod
from enum import Enum


class ImmunityLevel(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Symptom(Enum):
    NONE = "Không triệu chứng"
    MILD = "Triệu chứng nhẹ"
    SEVERE = "Triệu chứng nặng"
    DEATH = "Tử vong"


class Virus(ABC):
    def __init__(self, name, avg_death_rate):
        self.name = name
        self.avg_death_rate = avg_death_rate

    @abstractmethod
    def get_symptom(self, symptom: Symptom) -> str:
        pass


class Covid19(Virus):
    def __init__(self):
        super().__init__("Covid-19", (0.03 + 0.05) / 2)  # tỉ lệ tử vong từ 3 tới 5

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
            return "Mệt mỏi, sưng hạch, lở loét"
        return ""


class Host:
    def __init__(self, host_id: str, immunity: ImmunityLevel):
        self.host_id = host_id
        self.immunity = immunity
        self.is_vaccinated = False
        self.infected_results: dict[Virus, Symptom] = {}

    def is_dead(self) -> bool:
        return Symptom.DEATH in self.infected_results.values()

    def __str__(self) -> str:  # có return
        lines = []
        lines.append(f"Host ID: {self.host_id}")
        lines.append(f"Immunity Level: {self.immunity.name}")
        lines.append(f"Vaccinated: {'Yes' if self.is_vaccinated else 'No'}")
        for virus, symptom in self.infected_results.items():
            lines.append(f"  - {virus.name}: {symptom.value}")
            description = virus.get_symptom(symptom)
            lines.append(f"      + {description}")

        lines.append(f"Status: {'Dead' if self.is_dead() else 'Alive'}")
        return "\n".join(lines)


# theo thứ tự
# không triệu chứng -> nhẹ -> nặng -> tử vong
PROB_NO_VACCINE = {
    ImmunityLevel.HIGH: (0.5, 0.35, 0.15, 0.5),
    ImmunityLevel.MEDIUM: (0.1, 0.4, 0.5, 0.7),
    ImmunityLevel.LOW: (0.05, 0.15, 0.8, 0.100),
}

PROB_VACCINE = {
    ImmunityLevel.HIGH: (0.7, 0.25, 0.05, 0.4),
    ImmunityLevel.MEDIUM: (0.2, 0.5, 0.3, 0.6),
    ImmunityLevel.LOW: (0.1, 0.4, 0.5, 0.8),
}


def infect(host: Host, virus: Virus) -> Symptom:
    probs = (
        PROB_VACCINE[host.immunity]
        if host.is_vaccinated
        else PROB_NO_VACCINE[host.immunity]
    )
    # cho nhiễm bệnh thì phải có infected_results
    r = random.random()
    if 0 <= r < probs[0]:
        return Symptom.NONE
    elif probs[0] <= r < probs[0] + probs[1]:
        return Symptom.MILD
    elif probs[0] + probs[1] <= r < probs[0] + probs[1] + probs[2]:
        return Symptom.SEVERE
    else:
        death_rate = probs[3] * virus.avg_death_rate
        return Symptom.DEATH if random.random() < death_rate else Symptom.SEVERE


if __name__ == "__main__":
    vrs = [Covid19(), Ebola(), HIV()]
    # Câu 2
    n = int(input("Nhập số người vào: "))
    hosts: list[Host] = []
    for i in range(n):
        host_id = f"H000{i}"
        immunity = random.choice(list(ImmunityLevel))
        hosts.append(Host(host_id, immunity))
    # Câu 3
    for h in hosts:
        for v in vrs:
            sym = infect(h, v)
            h.infected_results[v] = sym
    for h in hosts:
        print(h)
    # Câu 4
    m = int(input("Test lại khi đã tiêm vaccine: "))
    assert m == n
    hosts_: list[Host] = []
    for j in range(m):
        host_id = f"K000{j}"
        immunity = random.choice(list(ImmunityLevel))
        h = Host(host_id, immunity)
        h.is_vaccinated = True
        hosts_.append(h)
    for h_ in hosts_:
        for v in vrs:
            sym = infect(h_, v)
            h_.infected_results[v] = sym
    severe_cases = 0
    death_cases = 0
    for host in hosts_:
        if host.is_dead():
            death_cases += 1
    for host in hosts_:
        for virus, symptom in host.infected_results.items():
            if symptom == Symptom.SEVERE:
                severe_cases += 1
                break
    print(f"số ca nặng: {severe_cases}")
    print(f"số ca tử vong: {death_cases}")
