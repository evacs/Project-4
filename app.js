// Local URL
url = 'http://127.0.0.1:5000'



// Function to dynamically generate categories
function generateCategories() {
    const select = d3.select("#category");

    // Sample categories
    const categories = [
        "Action", "Adventure", "Animation", "Children's", "Comedy",
        "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
        "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
        "Thriller", "War", "Western"
    ];

    select.selectAll("option")
        .data(categories)
        .enter()
        .append("option")
        .attr("value", category => category)
        .text(category => category);
}
// app.js

// Function to dynamically add movie options and ratings
function addMovieInputs(movies) {
    var movieInputs = $("#movie-inputs");
    movieInputs.empty(); // Clear existing inputs

    for (var i = 0; i < movies.length; i++) {
        var movieId = "movie" + (i + 1);
        var ratingId = "rating" + (i + 1);

        // Create input elements
        var movieInput = $("<input>").attr({ type: "text", id: movieId, name: movieId, placeholder: "Movie Name", value: movies[i] });
        var ratingInput = $("<div>").attr({ id: ratingId }).addClass("rating-container");

        // Append input elements to the container
        movieInputs.append(movieInput).append(ratingInput);

        // Initialize the rateYo plugin for each rating input
        $("#" + ratingId).rateYo({
            rating: 0,
            fullStar: true,
            onChange: function (rating, rateYoInstance) {
                // You can handle rating changes here
                console.log("Rating changed for " + movieId + ": " + rating);
            }
        });
    }
}


// d3.json(url + '/top_5')
//   .then(function(data) {
//     console.log(data);     
//   })
//   .catch(function (error) {
//     console.error("Error loading JSON data:", error);
//   });

// Call the function to generate categories
generateCategories();


// Updates functions based on dropdown selection
function optionChanged(selectedValue) {    
    // updateBarChart(selectedValue, data);
    // updateBubbleChart(selectedValue, data);
    // updateMetadata(selectedValue, data)
    console.log("Selected value:", selectedValue);
}

// function generateMovieInputs() {    
//         console.log(data);     
    
//     const form = d3.select("#movie-form");
//     const movieInputsContainer = d3.select("#movie-inputs");

//     topMovies = 
// }

// function generateMovieInputs() {
//     const form = d3.select("#movie-form");
//     const movieInputsContainer = d3.select("#movie-inputs");

//     // Sample movie data (replace with actual data)
//     const movieData = [
//         { title: 'Inception', rating: 0 },
//         { title: 'The Shawshank Redemption', rating: 0 },
//         { title: 'Pulp Fiction', rating: 0 },
//         { title: 'The Godfather', rating: 0 },
//         { title: 'Fight Club', rating: 0 },
//     ];

//     movieData.forEach((movie, index) => {
//         const label = form.append("label")
//             .attr("for", `movie${index + 1}`)
//             .text(`${movie.title}:`);

//         const ratingContainer = form.append("div")
//             .attr("class", "rating-container");

//         for (let i = 1; i <= 5; i++) {
//             ratingContainer.append("input")
//                 .attr("type", "radio")
//                 .attr("id", `rating${index + 1}-${i}`)
//                 .attr("name", `rating${index + 1}`)
//                 .attr("value", i);

//             ratingContainer.append("label")
//                 .text(i);
//         }
//     });
// }

// // Call the function to generate movie options and ratings
// generateMovieInputs();

// // Function to get recommendations
// function getRecommendations() {
//     // JavaScript function to send user input to Flask server and receive recommendations
//     const category = document.getElementById('category').value;
//     const ratings = [];

//     // Collect movie ratings from radio buttons
//     for (let i = 1; i <= 5; i++) {
//         const rating = document.querySelector(`input[name="rating${i}"]:checked`);
//         ratings.push(rating ? parseInt(rating.value) : 0);
//     }

//     // Sample data to send to the server (replace with actual data)
//     const requestData = {
//         category: category,
//         ratings: ratings,
//     };

//     // Simulate sending data to the server (replace with actual AJAX request)
//     console.log('Sending data to server:', requestData);

//     // Receive recommendations from the server (replace with actual logic)
//     const recommendations = [
//         'Recommended Movie 1',
//         'Recommended Movie 2',
//         'Recommended Movie 3',
//     ];

//     // Display recommendations in the UI
//     const recommendationsList = d3.select("#recommendations");
//     recommendationsList.selectAll("li").remove(); // Clear previous recommendations

//     recommendationsList.selectAll("li")
//         .data(recommendations)
//         .enter()
//         .append("li")
//         .text(d => d);
// }
