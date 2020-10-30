# Getting data from particular columns

I have loaded the movie data from the file into a panda data frame just as it did in the previous exercise.  In that exercise, we saw how we can recover the rows from the data file (i.e. the information on each file) by using the command:

````
prometheus = movies.loc["Prometheus"]
````

In this exercise we are going to see how we also extract the information from the columns of the data set.  Extracting the information in the columns is worthwhile because, if you think about the column containing the amount of money each film made for example, each of these numbers is a sample from the distribution of amounts of money that films make.  From the information in our data frame we can thus get information about the distributions of the following five quantities:

1. the films runtime in minutes
2. the films rating on IMDB
3. the number of votes that were cast to determine the rating
4. the amount of money the film made 
5. the metascore for the film.

To extract the information from the revenue_millions column of the data frame we run the command:

````
takings = movies_df['revenue_millions']
````

This command sets the variables called takings equal to a panda data frame that contains the titles of the films and just the information  on how much money they made.  We can thus extract the takings for the film Sing using the command you learned about in the previous exercise:

````
print( takings.loc['Sing'] )
````

Your task in this next exercise is thus to use the commands I have just explained to set the following variables equal to the descriptions of the quantities below:

1. `split_runtime` = the runtime for the film Split
2. `prometheus_metascore` = the metascore for the film prometheus
3. `arrival_rating` = the rating on IMDB for the film Arrival
4. `moana_takings` = the amount of money that was taken by the film Moana
5. `colossal_votes` = the number of votes that were cast for the film Colossal


