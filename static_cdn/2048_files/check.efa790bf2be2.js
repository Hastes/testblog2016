/**
 * Created by hs on 20.09.16.
 */

function CheckMs(datatest) {
    $.ajax({
    type:'POST',
              url:'/games/2048/score/',
              data:{
                    score: datatest,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
              },
              success: function (data) {
                  if (data) alert(data);
              }
        })
}
