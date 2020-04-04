# Example 1
A set of comments about your company's products is available. All of them are positive comments about the products.
Your manager has requested you to prepare a solution that can meet the following requirements:
* Store the texts and extract 15 keywords that are most cited by customers;
* Your company has 4 million customers and there is an interaction with these customers at least once a month;
* For each month, there must be an update in the words;
* On average, a customer interacts with a company once a month; Each interaction generates a text file from the information source system that stores this data;
* Some words should be discarded: 'by', 'above', 'all', 'none', 'nobody', etc.

Your mission is to do a proof of concept for your manager. He heard of parallel processing and read an article in Computer Magazine' talking about the movement NoSQL: wants to understand how it can work in the company scenario. He already requested an extraction of 1000 files on customer comments. In a meeting it was defined that you must deliver an example working tomorrow.
You must, then:
* Use a simple and fast implementation;
* Allow this to be performed on 50 machines in the company;
* Do not generate a final file with a word count.


# How to run
When running `python main.py`, you will have a server.
With `python mincemeat.py -p changeme localhost`, you will have a client. Create as many clients you want :)
A csv file called `Results.csv` will be created with the results.