import os
import subprocess
import sys
import traceback

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.importing.apkg import AnkiPackageImporter

DECK_DIR = os.path.expanduser(
        mw.addonManager.getConfig(__name__).get(
            "Markdown Deck Library Path", "~/Flashcard Decks"))

ANKDOWN = os.path.expanduser(
        mw.addonManager.getConfig(__name__).get(
            "Ankdown Location", "~/.local/bin/ankdown))

PACKAGE_NAME = "ankdown.apkg"

def importDecks():
    if not os.path.isdir(DECK_DIR):
        raise(ValueError("{} is not a directory".format(DECK_DIR)))

    os.chdir(os.path.join(os.path.split(__file__)[0], "user_files"))

    subprocess.run([ANKDOWN, "-r", DECK_DIR, "-p", PACKAGE_NAME, "-D"])

    AnkiPackageImporter(mw.col, PACKAGE_NAME).run()


def wrapImportDecks():
    try:
        importDecks()
    except:
        showInfo("Failed to import; received error: {}".format(traceback.format_exc()))

action = QAction("Reload Markdown Decks", mw, shortcut=QKeySequence(QKeySequence.Refresh))
action.triggered.connect(wrapImportDecks)
mw.form.menuTools.addAction(action)
