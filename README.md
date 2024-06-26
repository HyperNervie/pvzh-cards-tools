# pvzh-cards-tools
Here are two Python scripts that help you work on the cards.json you extract from the card_data_173 asset bundle of Plants vs. Zombies™ Heroes.

To run a script, simply run a command like this in your command line:

```
python <scriptname> <inputfilename> <outputfilename>
```

You may prepend a path to the file name if the file you want to work on is not in your command line's working directory. The input file must be a JSON without any syntax errors.

## Formatter
cards_formatter.py formats the JSON with an indent level of 2 spaces and replaces the annoying $type strings like `"PvZCards.Engine.Namespace.Classname, EngineLib, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"` with just `"Namespace.Classname"`. This helps you focus on what type of object is being used in your cards.json.

Example: Running `python cards_formatter.py cards.json cards_(simplified).json` generates a cards_(simplified).json with contents of cards.json indented and all $type strings simplified.

If you're using a code editor like Visual Studio Code, you can do the same task by using your code editor's formatting function (in the case of Visual Studio Code, it's pressing Shift+Alt+F) and regex-replacing `PvZCards\.Engine\.([A-Za-z]+)\.([A-Za-z]+), EngineLib, Version=1\.0\.0\.0, Culture=neutral, PublicKeyToken=null` with `\1.\2`. You don't need this script if you've learnt how to handle this with your code editor.

## Minimalizer
cards_minimalizer.py reverts all $type strings from `"Namespace.Classname"` back to `"PvZCards.Engine.Namespace.Classname, EngineLib, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"`, then minimalizes the JSON by removing all optional whitespaces and line breaks. Therefore, the input file must be a JSON that is generated by cards_formatter.py or you'll expand all `Namespace.Classname` in existing `"PvZCards.Engine.Namespace.Classname, EngineLib, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"` strings.

Example: Running `python cards_minimalizer.py cards_(simplified).json cards.json` generates a cards.json with all $type strings of cards_(simplified).json expanded and all optional whitespaces and line breaks removed. This cards.json can be imported to card_data_173 and takes less space as it is a minimalized JSON.
