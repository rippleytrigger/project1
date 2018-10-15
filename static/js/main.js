

function render_book_list(response)
{
    let search_results_div =  document.querySelector(".book-list")

    search_results_div.innerHTML = "";

    let book_list = document.createElement("ul");

    for(let book in response.list)
    {
        // Iterate though every element of the list and convert it to html
        
        let li = document.createElement("li");

        li.innerHTML = `<h2> <a href="/books/${response.list[book].isbn_number}"> ${response.list[book].title} </a>  </h2>`

        book_list.appendChild(li);
    }

    document.querySelector(".book-list").appendChild(book_list);
}


function render_new_review(response)
{
    let search_results_div =  document.querySelector(".book-list")

    search_results_div.innerHTML = "";

    let book_list = document.createElement("ul");

    for(let book in response.list)
    {
        // Iterate though every element of the list and convert it to html
        
        let li = document.createElement("li");

        li.innerHTML = `<h2> <a href="/books/${response.list[book].isbn_number}"> ${response.list[book].title} </a>  </h2>`

        book_list.appendChild(li);
    }

    document.querySelector(".book-list").appendChild(book_list);
}

function render_message(error)
{
    let container =  document.querySelector(".book-list")

    container.innerHTML = error.responseJSON.message

}

function ajax_search(event)
{
    event.preventDefault();

    $.ajax({
        url: event.originalTarget.action,
        data: $('#' + event.target.id).serialize(),
        type: 'POST',
        success: function(response) {
            render_book_list(response)
        },
        error: function(response) {
            render_message(response);
        }
    });
}

// function fetch_review_form(event)
// {
//     event.preventDefault();

//     const data = new URLSearchParams();
//     for (const pair of new FormData(event.target)) {
//         data.append(pair[0], pair[1]);
//     }

//     let headers = new Headers();

//     let miInit = { method: 'POST',
//                   headers: headers,
//                   body: data,
//                   mode: 'cors',
//                   cache: 'default' };

//     fetch(event.originalTarget.action, miInit)
//     .then(result => 
//     {
//         if(result.ok)
//         {
//             console.log('success:', result)
    
//             return result
//         }
//     })
//     .then(result =>
//     {
//         console.log(result)
//     })
//     .catch(error =>
//     {
//         console.log("Error", error)
//     });
// }

function fetch_review_form(event)
{
    event.preventDefault();

    $.ajax({
        url: event.originalTarget.action,
        data: $('#' + event.target.id).serialize(),
        type: 'POST',
        success: function(response) {
            //render_book_list(response)
        },
        error: function(response) {
            render_message(response);
        }
    });
}


document.addEventListener("DOMContentLoaded", function()
{
    if(window.location.pathname === "/search")
    {
        document.querySelector("#search_form").addEventListener("submit", ajax_search)
    }

    if(window.location.pathname.indexOf("/books/") == 0 && document.querySelector("#review-form"))
    {
        document.querySelector("#review-form").addEventListener("submit", fetch_review_form)
    }
});
