
# Poems Generator

The poem generator code uses a website to retrieve poems from a given writer and then saves them into a CSV file. After that, the code cleans up the text by removing unwanted elements and converts them into sentences, which are then saved into another CSV file. The program uses the BeautifulSoup library for web scraping and the Pandas library for data manipulation. Additionally, the argparse library is used to take input from the user about the writer whose poems they want to generate.

![](https://penwings.com/wp-content/uploads/elementor/thumbs/maxresdefault-p491laulshwjpa4a12k7ast1l83p5crhlqygimh6dk.jpg)

### Example

> Love is a feeling that cannot be tamed,
A passion that burns and cannot be named,
It flows like a river, wild and untamed,
And it's what we all seek, a love that's unclaimed.

### Features

-   Download Poems from a specific writer
-   Generate poems from a single word
-   Simple and easy to use commands
-   Lightweight and fast

### Clone

    git clone https://github.com/brunofinger/Poems-Generator
    cd Poems-Generator
### Download Poems
This code is a Python script that scrapes poems written by a given author from the MyPoeticSide website. It saves the titles and texts of the poems in a CSV file and also extracts individual sentences from the poems and saves them in another CSV file.

To use the script, the user needs to pass the name of the author to be scraped as a command-line argument when running the script.

    python downloader.py --writer "edgar-allan-poe-poems"
### Generate Poems
This code generates a poem given a file with a collection of sentences and a starting word. It uses Spacy, a natural language processing library, to load an English model and calculate the similarity between sentences. The function `format_poem()` formats the generated poem by capitalizing the first letter and adding a period at the end. The `poem_generator()` function reads sentences from the file, shuffles them, and selects the most similar sentence to the initial string for each line of the poem. The selected sentence is added to the poem and used to update the initial string for the next line. The number of lines in the poem can be specified with the `n_lines` parameter, which defaults to 4. 
To use this code, you need to provide a file path with a collection of sentences, a starting word, and optionally, the number of lines in the poem. 
You can run the code in the command line by providing these arguments with flags `-f`, `-w`, and `-n`.

    python poem_generator.py\
	    --file allan_poems_sentences.csv\
		--word love\
		--n_lines 4

