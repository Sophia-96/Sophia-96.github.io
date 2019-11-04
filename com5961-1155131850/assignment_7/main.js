      $("button#get_data2").click(function() {
      var items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appweDryqwYAXaKEy/Table%201?api_key=keyV7QPdbhgkDIJS6";
      var dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 items = [];
                     items.push(value.fields.genre_type);
                     items.push(value.fields.average_score);
                     dataSet.push(items);
                     console.log(items);
              }); // end .each
              console.log(dataSet);

           $('#table2').DataTable( {
               data: dataSet,
               retrieve: true,
               columns: [
                   { title: "genre_type",
                     defaultContent:""},
                   { title: "average_score",
                       defaultContent:"" },
               ]
           } );

           var chart = c3.generate({
                data: {
                    columns: dataSet,
                    type : 'bar'
                },
                axis: {
                  x: {label: 'genre_type'},
                  y: {label: '# of Items'}
                },
                bar: {
                    title: "# of Items by genre type:",
                }
            });

      }); // end .getJSON

   }); // end button

}); // document ready
