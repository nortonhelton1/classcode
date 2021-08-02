const moviesUL = document.getElementById("moviesUL")
const emptyDiv = document.getElementById("emptyDiv")
const titleBtns = document.getElementsByClassName("movieBtns")

let request = new XMLHttpRequest()

request.addEventListener('load', function(){
    console.log(this.responseText)

    const movies = JSON.parse(this.responseText)
    console.log(movies)
    const movieItems = movies.Search.map(function(movie) {
        const movieItem = `
        <li class = "lists">
            <div>
                <img  class="posters" src="${movie.Poster}" alt="">
            </div>
            <a href="#emptyDiv"><button onClick= showMovieDetails("${movie.imdbID}) class="movieBtns">${movie.Title}</button></a>
        </li>
        `
        return movieItem

    }) 
    moviesUL.innerHTML = movieItems.join("")
    

})
request.open("GET", MoviesURL)
request.send()
