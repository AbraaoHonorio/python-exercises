# python-exercises

# Solution 01 

## 📦 Problem Description

Your task is to write a function that sorts packages into stacks based on their **volume**, **dimensions**, and **mass**:

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³ **or**
  - Any dimension ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

### Sorting Rules

- `REJECTED`: if the package is **both bulky and heavy**
- `SPECIAL`: if the package is **either bulky or heavy**
- `STANDARD`: if the package is **neither bulky nor heavy**

---

## ✅ How to Test

1. Make sure you have Python installed.
2. Run the file using:

```bash
python main.py
