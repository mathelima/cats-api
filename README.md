# cats-api

Api based on `The Cat API`: https://thecatapi.com/ 

This API is responsible for store breeds information and cat images.

###Entities: 
#####Breeds
######Atributes: 
- description: Char
- id: Char
- images: Char 
- name: Char
- origin: Char
- temperament: Char
######Endpoint:
- /breeds

#####Categories
######Atributes: 
- id: Integer
- images: Char 
- name: Char
######Endpoint:
- /categories

The swagger can be accessed through the link: http://localhost:8000/docs/ and contains all the endpoints and methods for this API.