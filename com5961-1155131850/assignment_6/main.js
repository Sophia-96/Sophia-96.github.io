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
        var airtable_read_endpoint = "https://api.airtable.com/v0/appTnH4OwE42YrYVi/Foreign%20Language%20Movies?api_key=keyV7QPdbhgkDIJS6";
        var dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   items = [];
                       items.push(value.fields.name);
                       items.push(value.fields.director);
                       items.push(value.fields.genre);
                       items.push(value.fields.genre_type);
                       items.push(value.fields.region);
                       items.push(value.fields.release_date);
                       items.push(value.fields.length);
                       items.push(value.fields.score);
                       dataSet.push(items);
                       console.log(items);
                }); // end .each
                console.log(dataSet);

             $('#table1').DataTable( {
                 data: dataSet,
                 retrieve: true,
                 columns: [
                     { title: "name",
                       defaultContent:""},
                     { title: "director",
                         defaultContent:"" },
                     { title: "genre",
                       defaultContent:""},
                     { title: "genre_type",
                         defaultContent:""},
                     { title: "region",
                       defaultContent:""},
                     { title: "release_date",
                       defaultContent:""},
                     { title: "length",
                     defaultContent:""},
                     { title: "score",
                     defaultContent:""},
                 ]
             } );
        }); // end .getJSON
     }); // end button

}); // document ready
