# YUNYUN

A library to help people make decisions.

## Install

```
pip install yunyun
```

## Usage

```
yunyun
```

Enter as prompted, for example:

```
Start yunyun.
What's the theme of this discussion: Cat or Dog
Creating new record.
What's the objects to compare (separated by comma): cat,dog
What's the features to compare (separated by comma): cute,useful
For cute, how much weight do you think? Choose from -2, -1, 0, 1, 2: 2
For useful, how much weight do you think? Choose from -2, -1, 0, 1, 2: 1
For cute, what's the score of cat? Choose from 0, 1, 2: 2
For cute, what's the score of dog? Choose from 0, 1, 2: 1
For useful, what's the score of cat? Choose from 0, 1, 2: 0
For useful, what's the score of dog? Choose from 0, 1, 2: 1
Save complete. Start processing data...
Processing complete. Please see the results.

Theme: Cat or Dog

Options      cute(2)    useful(1)    Final score(Sorted)
---------  ---------  -----------  ---------------------
cat                2            0                      4
dog                1            1                      3
```
