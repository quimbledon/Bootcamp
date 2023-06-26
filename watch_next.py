#importing spaCy library for task:

import spacy

#creating string with the description of Planet Hulk to be used in function:
watched = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."


#creating function with en_core_web_md model
def recommended(watched):
    nlp = spacy.load('en_core_web_md')

#reading the text file containing the movie list from the task:
    with open('movies.txt', 'r') as file:
        movies = file.readlines()


#using spaCy with nlp to process the movie descriptions:
    doc1 = nlp(watched)

#calculating similarity scores fror all the movies in the txt so that they can be ordered accordingly:
    scores = [] #creating empty list
    for movie in movies: #iterates of each movie in the txt file
        movie_name, movie_description = movie.split(':') #the split here separates the movie name and its description so they can be stored as separate variables for use in function
        doc2 = nlp(movie_description) #using spaCy NLP model in the movie description texts
        similarity_score = doc1.similarity(doc2) #similarity method as used with previous task: compares doc1 which contains previously watched film with doc2 containing the txt movies
        scores.append((movie_name.strip(), similarity_score)) #creating list of similarity scores

#sorting the movies based on similarity scores to find the highest score, therefore the most similar movie:
#'lambda x' extracts the second element (index 1) from each 'tuple', which is the similarity score; 
#***this required a lot of research and I'd be interested to know if there's a better/quicker way to do this!
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

#reverse=True sorts by descending order thus putting the highest similarity score at the top of the list;
#experimented with 'reverse=False' which creates the result of Movie D which, therefore, would be the least similar to Planet Hulk

#creating 'similar' by retriving movie with highest similarity score from descending score list
    similar = scores[0][0]

    return similar

#passing text of 'Planet Hulk' description (hulk) to function allowing it to created similarity scores to other movies from txt file:

recommended_movie = recommended(watched)
print("Movie to watch next:", recommended_movie)

#Shows Movie C as the most similar to Planet Hulk and recommends it to the user.









