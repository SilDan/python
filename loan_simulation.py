from dataclasses import dataclass

@dataclass
class MonthEntry:
    month_index: int
    label: str
    balance_start: float
    interest: float
    principal: float
    payment: float
    balance_end: float


def main():
    entry = MonthEntry(
        month_index=0,
        label="April 2026",
        balance_start=14500.0,
        interest=50.0,
        principal=100.0,
        payment=150.0,
        balance_end=14400.0,
)

    print(entry)

if __name__ == "__main__":
    main()
