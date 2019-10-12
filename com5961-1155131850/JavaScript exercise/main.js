
var movies = [
    {
        title: 'Avengers',
        time: '12pm',
        status: 'available'
    },
    {
        title: 'Wonder Woman',
        time: '2pm',
        status: 'unavailable'
    },
    {
        title: 'The Last Jedi',
        time: '4pm',
        status: 'available'
    },
    {
        title: 'Lady Bird',
        time: '8pm',
        status: 'available'
    }
];

for (var movie of movies){
    if (movie.status === 'available'){
        console.log("The movie " + movie.title + " plays at " + movie.time);
    } else {
        console.log(`Sorry, the movie ${movie.title} is sold out`);
    }
}