$(document).ready(function(){

    $("button#recurve_women").click(function() {
      var table1_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/menseason?api_key=keygwX4DioRe1fgA2";
      var table1_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table1_items = [];
                     table1_items.push(value.fields.Ranking);
                     table1_items.push(value.fields.Name);
                     table1_items.push(value.fields.Nation);
                     table1_items.push(value.fields.Season_1516);
                     table1_items.push(value.fields.Season_1617);
                     table1_items.push(value.fields.Season_1718);
                     table1_items.push(value.fields.Season_1819);
                     table1_items.push(value.fields.Season_1920);
                     table1_dataSet.push(table1_items);
                     console.log(table1_items);
              }); // end .each
              console.log(table1_dataSet);

           $('#table1').DataTable( {
               data: table1_dataSet,
               retrieve: true,
               columns: [
                   { title: "Ranking",
                     defaultContent:""},
                   { title: "Name",
                       defaultContent:"" },
                   { title: "Nation",
                       defaultContent:"" },                       
                   { title: "Season_15/16",
                     defaultContent:""},
                   { title: "Season_16/17",
                     defaultContent:""},
                   { title: "Season_17/18",
                     defaultContent:""},
                   { title: "Season_18/19",
                     defaultContent:""},
                   { title: "Season_19/20",
                     defaultContent:""},   
               ]
           });
           }); // end .getJSON

           var table5_items = [];
           var i = 0;
           var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/menseason?api_key=keygwX4DioRe1fgA2";
           var table5_dataSet = [];
           $.getJSON(airtable_read_endpoint, function(result) {
                  $.each(result.records, function(key,value) {
                      table5_items = [];
                          table5_items.push(value.fields.Name);
                          table5_items.push(value.fields.Season_1516);
                          table5_items.push(value.fields.Season_1617);
                          table5_items.push(value.fields.Season_1718);
                          table5_items.push(value.fields.Season_1819);
                          table5_items.push(value.fields.Season_1920);
                          table5_dataSet.push(table5_items);
                          console.log(table5_items);
                   }); // end .each
                   console.log(table5_dataSet);

                $('#table5').DataTable( {
                    data: table5_dataSet,
                    retrieve: true,
                    columns: [
                        { title: "Name",
                          defaultContent:""},
                        { title: "Season_1516",
                          defaultContent:"" },
                        { title: "Season_1617",
                          defaultContent:""},
                        { title: "Season_1718",
                          defaultContent:""},
                        { title: "Season_1819",
                          defaultContent:""},
                        { title: "Season_1920",
                          defaultContent:""},                          
                    ]
                });

           var contents = document.getElementById('title1').innerHTML="The Best Scores in Recent Five Seasons";

           var chart = c3.generate({
                    bindto: '#chart_rw',
                    data: {
                        columns: table5_dataSet,
                        type : 'line'
                      },
                      axis: {
                        x: {label: 'Season'},
                        y: {label: 'Score'}
                      },
                      bar: {
                        title: "The Best Scores in Recent Five Seasons",
                      }
                    });
                  });
                }); // end .button

      $("button#recurve_men").click(function() {
        var table2_items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/ladiesseason?api_key=keygwX4DioRe1fgA2";
        var table2_dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   table2_items = [];
                       table2_items.push(value.fields.Ranking);
                       table2_items.push(value.fields.Name);
                       table2_items.push(value.fields.Nation);
                       table2_items.push(value.fields.Season_1516);
                       table2_items.push(value.fields.Season_1617);
                       table2_items.push(value.fields.Season_1718);
                       table2_items.push(value.fields.Season_1819);
                       table2_items.push(value.fields.Season_1920);
                       table2_dataSet.push(table2_items);
                       console.log(table2_items);
                }); // end .each
                console.log(table2_dataSet);

             $('#table2').DataTable( {
                 data: table2_dataSet,
                 retrieve: true,
                 columns: [
                      { title: "Ranking",
                          defaultContent:""},
                      { title: "Name",
                          defaultContent:"" },
                      { title: "Nation",
                          defaultContent:"" },                       
                      { title: "Season_15/16",
                          defaultContent:""},
                      { title: "Season_16/17",
                          defaultContent:""},
                      { title: "Season_17/18",
                          defaultContent:""},
                      { title: "Season_18/19",
                          defaultContent:""},
                      { title: "Season_19/20",
                          defaultContent:""},   
                 ]
             } );
        }); // end .getJSON

        var table6_items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/ladiesseason?api_key=keygwX4DioRe1fgA2";
        var table6_dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   table6_items = [];
                       table6_items.push(value.fields.Name);
                       table6_items.push(value.fields.Season_1516);
                       table6_items.push(value.fields.Season_1617);
                       table6_items.push(value.fields.Season_1718);
                       table6_items.push(value.fields.Season_1819);
                       table6_items.push(value.fields.Season_1920);
                       table6_dataSet.push(table6_items);
                       console.log(table6_items);
                }); // end .each
                console.log(table6_dataSet);

             $('#table6').DataTable( {
                 data: table6_dataSet,
                 retrieve: true,
                 columns: [
                      { title: "Name",
                        defaultContent:""},
                      { title: "Season_1516",
                        defaultContent:"" },
                      { title: "Season_1617",
                        defaultContent:""},
                      { title: "Season_1718",
                        defaultContent:""},
                      { title: "Season_1819",
                        defaultContent:""},
                      { title: "Season_1920",
                        defaultContent:""},   
                 ]
             });

        var contents = document.getElementById('title2').innerHTML="The Best Scores in Recent Five Seasons";

        var chart = c3.generate({
                 bindto: '#chart_rm',
                 data: {
                     columns: table6_dataSet,
                     type : 'line'
                   },
                   axis: {
                     x: {label: 'Season'},
                     y: {label: 'Score'}
                   },
                   bar: {
                     title: "The Best Scores in Recent Five Seasons",
                   }
                 });
               });
             }); // end .button


    $("button#compound_women").click(function() {
      var table3_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/pairsseason?api_key=keygwX4DioRe1fgA2";
      var table3_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table3_items = [];
                     table3_items.push(value.fields.Ranking);
                     table3_items.push(value.fields.Name);
                     table3_items.push(value.fields.Nation);
                     table3_items.push(value.fields.Season_1516);
                     table3_items.push(value.fields.Season_1617);
                     table3_items.push(value.fields.Season_1718);
                     table3_items.push(value.fields.Season_1819);
                     table3_items.push(value.fields.Season_1920);
                     table3_dataSet.push(table3_items);
                     console.log(table3_items);
              }); // end .each
              console.log(table3_dataSet);

           $('#table3').DataTable( {
               data: table3_dataSet,
               retrieve: true,
               columns: [
                    { title: "Ranking",
                        defaultContent:""},
                    { title: "Name",
                        defaultContent:"" },
                    { title: "Nation",
                        defaultContent:"" },                       
                    { title: "Season_15/16",
                        defaultContent:""},
                    { title: "Season_16/17",
                        defaultContent:""},
                    { title: "Season_17/18",
                        defaultContent:""},
                    { title: "Season_18/19",
                        defaultContent:""},
                    { title: "Season_19/20",
                        defaultContent:""},   
               ]
           });
      }); // end .getJSON

      var table7_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/pairsseason?api_key=keygwX4DioRe1fgA2";
      var table7_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table7_items = [];
                      table7_items.push(value.fields.Name);
                      table7_items.push(value.fields.Season_1516);
                      table7_items.push(value.fields.Season_1617);
                      table7_items.push(value.fields.Season_1718);
                      table7_items.push(value.fields.Season_1819);
                      table7_items.push(value.fields.Season_1920);
                      table7_dataSet.push(table7_items);
                     console.log(table7_items);
              }); // end .each
              console.log(table7_dataSet);

           $('#table7').DataTable( {
               data: table7_dataSet,
               retrieve: true,
               columns: [
                    { title: "Name",
                      defaultContent:""},
                    { title: "Season_1516",
                      defaultContent:"" },
                    { title: "Season_1617",
                      defaultContent:""},
                    { title: "Season_1718",
                      defaultContent:""},
                    { title: "Season_1819",
                      defaultContent:""},
                    { title: "Season_1920",
                      defaultContent:""}, 
               ]
           });

      var contents = document.getElementById('title3').innerHTML="The Best Scores in Recent Five Seasons";

      var chart = c3.generate({
               bindto: '#chart_cw',
               data: {
                   columns: table7_dataSet,
                   type : 'line'
                 },
                 axis: {
                   x: {label: 'Season'},
                   y: {label: 'Score'}
                 },
                 bar: {
                   title: "The Best Scores in Recent Five Seasons",
                 }
               });
             });
           }); // end .button

    $("button#compound_men").click(function() {
      var table4_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/danceseason?api_key=keygwX4DioRe1fgA2";
      var table4_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table4_items = [];
                      table4_items.push(value.fields.Ranking);
                      table4_items.push(value.fields.Name);
                      table4_items.push(value.fields.Nation);
                      table4_items.push(value.fields.Season_1516);
                      table4_items.push(value.fields.Season_1617);
                      table4_items.push(value.fields.Season_1718);
                      table4_items.push(value.fields.Season_1819);
                      table4_items.push(value.fields.Season_1920);
                      table4_dataSet.push(table4_items);
                     console.log(table4_items);
              }); // end .each
              console.log(table4_dataSet);

           $('#table4').DataTable( {
               data: table4_dataSet,
               retrieve: true,
               columns: [
                    { title: "Ranking",
                        defaultContent:""},
                    { title: "Name",
                        defaultContent:"" },
                    { title: "Nation",
                        defaultContent:"" },                       
                    { title: "Season_15/16",
                        defaultContent:""},
                    { title: "Season_16/17",
                        defaultContent:""},
                    { title: "Season_17/18",
                        defaultContent:""},
                    { title: "Season_18/19",
                        defaultContent:""},
                    { title: "Season_19/20",
                        defaultContent:""},   
               ]
           });
      }); // end .getJSON

      var table8_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/danceseason?api_key=keygwX4DioRe1fgA2";
      var table8_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table8_items = [];
                      table8_items.push(value.fields.Name);
                      table8_items.push(value.fields.Season_1516);
                      table8_items.push(value.fields.Season_1617);
                      table8_items.push(value.fields.Season_1718);
                      table8_items.push(value.fields.Season_1819);
                      table8_items.push(value.fields.Season_1920);
                      table8_dataSet.push(table8_items);
                      console.log(table8_items);
              }); // end .each
              console.log(table8_dataSet);

           $('#table8').DataTable( {
               data: table8_dataSet,
               retrieve: true,
               columns: [
                    { title: "Name",
                      defaultContent:""},
                    { title: "Season_1516",
                      defaultContent:"" },
                    { title: "Season_1617",
                      defaultContent:""},
                    { title: "Season_1718",
                      defaultContent:""},
                    { title: "Season_1819",
                      defaultContent:""},
                    { title: "Season_1920",
                      defaultContent:""}, 
               ]
           });

      var contents = document.getElementById('title4').innerHTML="The Best Scores in Recent Five Seasons";

      var chart = c3.generate({
               bindto: '#chart_cm',
               data: {
                   columns: table8_dataSet,
                   type : 'line'
                 },
                 axis: {
                   x: {label: 'Season'},
                   y: {label: 'Score'}
                 },
                 bar: {
                   title: "The Best Scores in Recent Five Seasons",
                 }
               });
             });
           }); // end .button

   $("button#recurve_women").click(function(){
       $("#rw").slideToggle(1000);
   });

   $("button#recurve_men").click(function(){
       $("#rm").slideToggle(1000);
   });

   $("button#compound_women").click(function(){
       $("#cw").slideToggle(1000);
   });

   $("button#compound_men").click(function(){
       $("#cm").slideToggle(1000);
   });

       // $.getJSON('http://localhost/d756a/data_export.json/Computer+TV', function(obj) {
}); // document ready