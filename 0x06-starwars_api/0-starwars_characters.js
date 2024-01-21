#!/usr/bin/node
// Print starwars characters

const request = require('request');


function getCast(movieId) {

    const Url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    request(Url, (error, response, body) => {

        if (error) {
            console.error(`Error fetching movie data: ${error.message}`);
            return;
        }

        if (response.statusCode !== 200) {
            console.error(`Error fetching movie data. Status Code: ${response.statusCode}`);
            return;
        }

        const charactersUrls = JSON.parse(body).characters;

        // Fetch character names for each URL
        charactersUrls.forEach(characterUrl => {

            request(characterUrl, (characterError, characterResponse, characterBody) => {

                if (characterError) {
                    console.error(`Error fetching character data: ${characterError.message}`);
                    return;
                }

                if (characterResponse.statusCode === 200) {

                    const characterName = JSON.parse(characterBody).name;
                    console.log(characterName);
                } else {
                    console.error(`Error fetching character data. Status Code: ${characterResponse.statusCode}`);
                }
            });
        });
    });
}

// Check if Movie ID is provided as a command-line argument
const movieId = process.argv[2];
if (!movieId) {
    console.error("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

// getCast(movieId);
