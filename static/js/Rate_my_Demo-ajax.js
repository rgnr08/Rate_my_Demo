/**
 * Created by 2108535R on 17/03/14.
 */
$(".likes").click(function() {

     var demoid = $(this).attr("data-demoid");
     $.get('/Rate_my_Demo/like_demo/', {demo_id: demoid}, function(data){
              $("#like_count" + demoid).html(data);
              $(this).hide();
           });

});

$(".unlikes").click(function() {

     var demoid2 = $(this).attr("data-demoid2");
    console.log("demoid2 is " + demoid2 )
     $.get('/Rate_my_Demo/unlike_demo/', {demo_id2: demoid2}, function(data){
              $("#unlike_count" + demoid2).html(data);
              $(this).hide();
              console.log("D");
              console.log(data);
           });

});