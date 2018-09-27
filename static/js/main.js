console.log("EPale")

var L;

function render_results(response)
{
    let book_list = document.createElement("ul");

    for(let book in response.list)
    {
        console.log(response.list[book])
        //response.list[book][book_details]
        let li = document.createElement("li");

        li.innerHTML = `<h1> ${response.list[book].title} - ${response.list[book].publication_year} </h1>
                             <h3> ${response.list[book].author} ${response.list[book].isbn_number} </h3>`

        book_list.appendChild(li);
    }

    document.querySelector(".book-list").innerHTML = book_list;
}

function Ajax_search(event)
{
    event.preventDefault();

    $.ajax({
        url: '/search',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            render_results(response)
        },
        error: function(error) {
            console.log(error);
        }
    });
}




document.addEventListener("DOMContentLoaded", function(event) 
{
    if(window.location.pathname === "/search")
    {
        document.querySelector("#search_form").addEventListener("submit", Ajax_search)
    }
});
