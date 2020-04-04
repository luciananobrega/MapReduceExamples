# Example 3

Each line of each file on `data` folder is:
* Bibliographic information;
* Authors separated by '::';
* Title of the work.

`paper-id:::author1::author2::…. ::authorN:::title`

The task is to calculate how many times each term (in the title of the work) happens per author.
For example: for the author 'Alberto Pettorossi' the following terms happen (consideringall documents): program: 3, transformation: 2, transforming: 2, using: 2, programs: 2, and logic: 2.
* Observe the following items:
    * The field separator is “:::” and the author separator is “::”;
    * Each author can have written multiple works, which in turn can be in several files;
    * There is a list of words that will not be considered (stopwords);
    * Exclude scores as well
    * Objective: To answer which are the two words that happen the most for the following authors:
        * Grzegorz Rozenberg
        * Philip S. Yu