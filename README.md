Specification

You should build a new Django Application with two API endpoints. The first endpoint allows an end user to create a new Dog model by making a POST to /api/dogs, view current dogs that have been saved to the server before by making a GET to /api/dogs, and get, modify, or delete an existing Dog record by making a GET, PUT, or DELETE request (respectively) to /api/dogs/<id> where <id> is the id of the Dog record to be retrieved, modified, or deleted. Since a Dog includes a foreign key to the breed, you also need to make the same type of endpoints for dog breed at /api/breeds/ and /api/breeds/<id>.
Dog model

A dog should contain the following fields:

    name (a character string)
    age (an integer)
    breed (a foreign key to the Breed Model)
    gender (a character string)
    color (a character string)
    favoritefood (a character string)
    favoritetoy (a character string)

Breed Model

A breed should contain the following fields:

    name (a character string)
    size (a character string) [should accept Tiny, Small, Medium, Large]
    friendliness (an integer field) [should accept values from 1-5]
    trainability (an integer field) [should accept values from 1-5]
    sheddingamount (an integer field) [should accept values from 1-5]
    exerciseneeds (an integer field) [should accept values from 1-5]

Todo List

To do this, do the following:

    track all of your changes using github. 
    create a new repository on github following these instructions: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
    Using a local file folder, call git init
    in that folder create a new django server like we did in the labs
    create a new app in your django server called dogapi
    add a Dog and Breed models to models.py
    migrate your database to include tables for Dog and Breed


Do one of the following:

    Use class-based views
        add two class-based API view controllers for handling Dog REST endpoints to controllers.py
            call one DogDetail and one DogList to conform to best practice nomenclature
            The DogDetail class should have three methods named get, put, delete
            The DogList class should have two methods named get and post
            refer to http://www.django-rest-framework.org/tutorial/3-class-based-views/ for examples
        add a two class-based API view controllers for handling Breed REST endpoints to controllers.py
            call one BreedDetail and one BreedList to conform to best practice nomenclature
            The BreedDetail class should have three methods named get, put, delete
            The BreedList class should have two methods named get and post
            refer to http://www.django-rest-framework.org/tutorial/3-class-based-views/ for examples
    use viewsets (one for breed and one for dogs)
        This is probably the best (and easiest approach)


In either case:

    add the appropriate url patterns to the urls.py file to accept all of the patterns and map them to the correct controller
    test your endpoints with POSTMAN, taking screenshots of each type of request. There should be 5 requests total for each type of model, for a total of 10 tests and screenshots.
        GET (list), POST to /api/dogs/
        GET, PUT, DELETE to /api/dogs/<id>
        GET (list), POST to /api/breeds/
        GET, PUT, DELETE to /api/breeds/<id>
    10 bonus points: Commit your code and save the version number (make sure to link to this commit in your submission below). Now rework your API to use the other type of (class based views or viewsets). Save your changes and provide an additional link to your repository state using the alternative approach.
