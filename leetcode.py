$(function(){
  /*
   TODO Create an instance of PresenceService and register a callback and then call subscribe.

       var presenceService = new PresenceService();
       presenceService.onMessage(callback);

       presenceService.subscribe();

   The callback will be called multiple times with objects that look like this:

       {person:  {id: 42, name: 'Rambo', priority: 2}, status: 'online'}

   Once you get these messages, you need to render them as shown in 'SampleScreenshot.png'.
   1. You may have one entry per line.
   2. You must stick to the markup recommendations.
   3. Never render more than 15 statuses at once.
   4. These look a lot like the chat widget on gmail. A unique person may show up only once.
   5. Sort first by status, then by priority, then alphabetically.
     i) Statuses are sorted (online, busy, offline).
     ii) Priorities are sorted (1,2,3).
   7. Every status stays within one line. If it exceeds the width of a line, it's truncated with ellipsis.
   8. The colored dots can be produced using FontAwesome. The character code is "\f111".
      The colors used are 'green', 'orange' and 'gray'
   9.
   */

  var publish = function(){
    var toprint = $('#contacts').data('users');
    $('#contacts ul').empty();
    var height = 0;
    for (var i=0; i < toprint.length; i++){
      height += 21;
      $("#contacts ul").append('<li class=\"'+toprint[i].status+'\">'+ toprint[i].person.name+'</li>');
    }
    $("#contacts").css({'height':height+'px'});
  };
  var callback = function(data){
      // console.log('got data-------------->: '+data.person.id+data.person.name);
      var dict = {"online": 1, "busy":2, "offline":3};
      var list = $("#contacts").data('users');

      for(var i=0; i<list.length; i++){
        if (list[i].person.id == data.person.id){
          list.splice(i,1);
        }
      }

      //insert the new data in the sorted list
      for (var i=0; i < list.length; i++){
        if (dict[data.status] < dict[list[i].status]) {
          list.splice(i, 0, data);
          break;
        }
        else if (dict[data.status] == dict[list[i].status]){
          if (data.person.priority <= list[i].person.priority) {
            list.splice(i, 0, data);
            break;
          }
        }
      }

      //check if we need to insert the data at the end #1 if list empty #2 status is more than last #3 status is same
      // priority is more
      var last = list.length - 1
      if (!list.length || dict[list[last].status] < dict[data.status] || (dict[list[last].status] ==  dict[data.status]
       && list[last].person.priority < data.person.priority)) list.push(data);

      //trim the array to 15 length
      if (list.length > 15){
        list.splice(15, list.length - 15);
      }
      $("#contacts").data('users', list);
      publish();
      // list.push(data);
      // list.sort(
      //   function(a,b){
      //     var dict = {"online": 1, "busy":2, "offline":3};
      //     if (a.status == b.status){
      //       return a.person.priority - b.person.priority;
      //     } else {
      //         return dict[a.status] - dict[b.status];
      //     }
      //   }
      // )
      // if (list.length > 15){
      //   list.splice(15, list.length - 15);
      // }

      // for(var i=0; i < list.length; i++){
      //   console.log(list[i].person.name, list[i].status, list[i].person.priority);
      // }

  };

  var presenceService = new PresenceService();
  presenceService.onMessage(callback);
  presenceService.subscribe();

});
