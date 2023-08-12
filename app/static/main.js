

 document.addEventListener("DOMContentLoaded", function() {

    var currentPage = 1;
    var numOfPages = $(".page").length;
    console.log(numOfPages)
    var animationTime = 1000;
    var scrolling = false;
    // the page class in the html file
    var pagePrefix = ".page";

    function pageScroll() {
      scrolling = true;
      // scrolling mechanism that adds a class to the html tag to determine what page your on and what content to show
      $(pagePrefix + currentPage).removeClass("inactive").addClass("active");
      $(pagePrefix + (currentPage - 1)).addClass("inactive");
      $(pagePrefix + (currentPage + 1)).removeClass("active");

  // function for the scroll animation to be delayed for the duration of the animation 
      setTimeout(function() {
        scrolling = false;
      }, animationTime);
    };
  
    function navigateUp() {
      if (currentPage === 1) return;
      currentPage--;
      pageScroll();
    };
  
    function navigateDown() {
      if (currentPage === numOfPages) return;
      currentPage++;
      pageScroll();
    };
  
    $(document).on("mousewheel DOMMouseScroll", function(v) {
      if (scrolling){
        return;
      } 
      // checks to see if the user is scrolling up or down
      if (v.originalEvent.wheelDelta > 0 || v.originalEvent.detail < 0) {
        navigateUp();
      } else { 
        navigateDown();
      }
    });
  

    // for up and down arrow keys on the keyboard, 38 corresponds to the up arrow and 40 corresponds to the down arrow
    $(document).on("keydown", function(e) {
      if (scrolling) return;
      if (v.key === 38) {
        navigateUp();
      } else if (v.key=== 40) {
        navigateDown();
      }
    });
  
  });






