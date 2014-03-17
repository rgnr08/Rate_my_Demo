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