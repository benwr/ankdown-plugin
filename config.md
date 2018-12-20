# Ankdown Configuration

There are two configuration options.

`Markdown Deck Library Path` describes the location of a directory containing 
your flashcard decks. This defaults to `~/Flashcard Decks`. Any `.md` files
in this directory will be added to decks with names based on the directory
those `.md` files are in. So if I have `~/Flashcard Decks/Physics/laws.md`,
I'll end up with a Physics deck containing the cards as shown in `laws.md`.

`Ankdown Location` describes the location of the ankdown executable. In order
to use this add-on, you need to have also installed the `ankdown` python package,
which includes a script called `ankdown`. This will typically go somewhere in
your `$PATH`. To find it, it may work to run `which ankdown` after installing
the package.
