const newsContainer = document.getElementById("newsContainer")

news.articles.map(function(newsArticle) {
    let item = `
    <div id = "box1">
        <h2>${newsArticle.title}</h3>
        <img class="images" src="${newsArticle.urlToImage}" alt="">
        <p>${newsArticle.description}</p>
        <p><a href="${newsArticle.url}">Click here for more.</a></p>
        <p>${newsArticle.author}</p>
        <p>${newsArticle.publishedAt}</p>
    </div>
    `
        newsContainer.insertAdjacentHTML('beforeend', item)
}

)
