Plagiarism Detection

This program uses the scikit library for python. We first convert our textual data into an array of numbers in a process known as "word embedding". It follows some algorithms built into scikit and it ends up with words being represented as positions in space, like vectors. We then check their cosine dot product similarity to get a score of similarity between 0 and 1. 

To run the file, install scikit from pip using "pip install scikit-learn", keep the .txt files in the same folder as the python code and simply run it on a terminal using "python3 .\plag.py".