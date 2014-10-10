django-lexicon
==============

django-lexicon defines an abstract class named `Lexicon`. It is a common practice when normalizing a data model to _break out_ repeated finite sets of terms within a column into their own table. This is quite obvious for entities such as _books_ and _authors_, but less so for commonly used or enumerable terms.

```
id | name | birth_month
---+------+------------
 1   Sue    May
 2   Joe    Jun
 3   Bo     Jan
 4   Jane   Apr
...
```

The above shows a table with three columns `id`, `name` and `birth_month`.
There are some inherent issues with `birth_month`:

1. Months have an arbitrary order which makes it very difficult to order the rows by `birth_month` since they are ordered lexicographically by default.
2. As the table grows (think millions) the few bytes of disk space each repeated string takes up starts having a significant impact.
3. The cost of querying for the distinct months within the population gets increasingly more expensive as the table grows.
4. As the table grows, the cost of table scans increases since queries are acting on strings rather than an integer (e.g. a foreign key).

Although the above example is somewhat contrived, the reasons behind this type of normalization are apparent.

To implement, subclass and define the `value` and `label` fields.

```python
from lexicon.models import Lexicon

class Month(Lexicon):
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
```

A few of the advantages include:

- Define an arbitrary `order` of the items in the lexicon
- Define an integer `code` which is useful for downstream clients that prefer working with a enumerable set of values such as SAS or R
- Define a verbose/more readable label for each item
    - For example map _Jan_ to _January_

## Manager Methods

### `reorder`

The `Lexicon` class also comes with an extra method on it's manager called `reorder` which reorders the items in the lexicon and updates the `order` value of each item with the new sort index. This is generally only necessary if items are added to the set and the ordering needs to be updated. The method takes the same arguments as `list.sort()`, but `key` can also be a string corresponding to a built-in key function.

```python
>> SomeLexicon.objects.reorder(key='coerce_float')
```

_**Performance Note:** The entire lexicon is loaded into memory, sorted, and each item is saved. This should rarely be an issue assuming your the lexicon is not millions of items in size._

#### Built-in Key Functions

- `coerce_float`
    - This relies on the `value` field for each object and attempts to coerce it to a float (in case numbers are represented as strings..) and falls back to itself if a `TypeError` or `ValueError` is raised.
