# Python Cheat Sheet: Operators, Lists, and Sets

## 1. Arithmetic Operators

### Floor Division (`//`)
* **Behavior:** Divides the first number by the second number and rounds the result **down** to the nearest whole number.
* **Return Type:** Returns an **integer** if both inputs are integers.

---

## 2. List Methods

* `pop(idx)`
  * Removes and returns the element at the specified index.
  * *Note:* If no index is passed, it deletes and returns the **last element**.
* `remove(val)`
  * Removes the **first occurrence** of the specified value.
  * *Warning:* Raises a `ValueError` if the value is not found.
* `clear()`
  * Removes **all elements** from the list.

---

## 3. Set Methods & Operations

### Basic Methods
* `add(item)`
  * Adds an element to the set if it doesn't already exist.
* `discard(item)`
  * Removes an item if present. 
  * *Note:* Does **not** raise an error if the item is missing.
* `remove(item)`
  * Removes an item from the set. 
  * *Warning:* Raises a `KeyError` if the item is not found.
* `pop()`
  * Removes and returns an **arbitrary element**. 
  * *Warning:* Raises a `KeyError` if the set is empty.
* `copy()`
  * Returns a shallow copy of the set.
* `clear()`
  * Removes all elements, leaving an empty set.

### Set Operations

| Method | Operator | Description |
| :--- | :--- | :--- |
| `difference()` | `-` | Returns elements present in the first set but not in the others. |
| `intersection()` | `&` | Returns only the elements common to all sets. |
| `symmetric_difference()` | `^` | Returns elements unique to each set (excludes duplicates). |
| `union()` | `\|` | Combines elements from all sets into a new set of all unique values. |
