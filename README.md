# Apalabrados



## Introduction

This training project consists in analyzing the input written by the user and store it in on of the three tables (Characters, numbers and text).


## General Info

The code and the flow chart shows the logic procedure to create a database with three tables:

 * Numbers. Columns: number - acumulate
 * Text. Columns: text - start - end
 * Characters. Columns: character

Then, there is an input tha should be analized by the algorithm to store it in on of the tables above. It depends on:

 * If it is a number, it should be stored in the numbers table. In the "number" column it will store the number. In the "acumulate" column it will store the value taking into account the previous ones stored in the same table.
  
 * If it is a text, it should store the input in the text table. The input will be stored in the "text" column. The first and last letters will be stored in the "start" and "end" columns respectively.
  
 * If there is an special character in the input, it should be stored in the "characters" table and the rest of the input is not taking into account.
 

### Flowchart
  
![](/Nuevo.drawio.png)

## General Info

To run this project, install locally the libraries shown below:

 * Pandas
 * Numpy

Then, you can copy and paste the code atached to the file apalabrados.py in a text editor of your preference. Finally, you will be able to run the program and test it.
