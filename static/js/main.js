

function render_book_list(response)
{
    let search_results_div =  document.querySelector(".book-list")

    search_results_div.innerHTML = "";

    let book_list = document.createElement("ul");

    for(let book in response.list)
    {
        console.log(response.list[book])
        //response.list[book][book_details]
        let li = document.createElement("li");

        li.innerHTML = `<h2> <a href="/books/isbn_number/${response.list[book].isbn_number}"> ${response.list[book].title} </a>  </h2>`

        book_list.appendChild(li);
    }

    document.querySelector(".book-list").appendChild(book_list);
}


function render_message(response)
{
    
}

function ajax_search(event)
{
    event.preventDefault();

    $.ajax({
        url: '/search',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            render_book_list(response)
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
        document.querySelector("#search_form").addEventListener("submit", ajax_search)
    }
});
