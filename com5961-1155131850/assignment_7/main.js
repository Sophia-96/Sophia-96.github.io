      var items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appRqQDyaA4prczrI/Table%201?api_key=keyV7QPdbhgkDIJS6";
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

           var chart = c3.generate({
                data: {
                    columns: dataSet,
                    type : 'bar'
                },
                axis: {
                  x: {label: 'genre_type'},
                  y: {label: 'average_score'}
                },
                bar: {
                    title: "# of average score by genre_type:",
                }
            });
        })

