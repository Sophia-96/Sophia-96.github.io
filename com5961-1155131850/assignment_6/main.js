$(document).ready(function(){

    $("button#hide_h2").click(function() {
        $("h2").hide(500);
    });

    $("button#show_h2").click(function() {
        $("h2").show(300);
        $("h2").css("color","blue");
        $("h2").html("You clicked me hard.");
    });

    $("button#clear_screen").click(function() {
        var $x = $("container");
        $x.empty();
    });

    $("button#get_data").click(function() {
        var items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appTnH4OwE42YrYVi/Table%201?api_key=YOUR_API_KEY";
        var dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   items = [];
                       items.push(value.fields.Name);
                       items.push(value.fields.Director);
                       items.push(value.fields.Poster);
                       items.push(value.fields.Genre);
                       items.push(value.fields.Genre_type);
                       items.push(value.fields.Region);
                       items.push(value.fields.Release_Date);
                       items.push(value.fields.Length);
                       items.push(value.fields.Score);
                       dataSet.push(items);
                       console.log(items);
                }); // end .each
                console.log(dataSet);

             $('#table1').DataTable( {
                 data: dataSet,
                 retrieve: true,
                 columns: [
                     { title: "Name",
                       defaultContent:""},
                     { title: "Director",
                         defaultContent:"" },
                     { title: "Poster",
                       defaultContent:"" },
                     { title: "Genre",
                       defaultContent:""},
                     { title: "Genre_type",
                         defaultContent:""},
                     { title: "Region",
                       defaultContent:""},
                     { title: "Release_Date",
                       defaultContent:""},
                     { title: "Length",
                     defaultContent:""},
                     { title: "Score",
                     defaultContent:""},
                 ]
             } );
        }); // end .getJSON
     }); // end button

}); // document ready
