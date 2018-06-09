(function($){
  $(function(){

    $('select').material_select();
    $('.collapsible').collapsible();
    $('.materialboxed').materialbox();
  }); // end of document ready
})(jQuery); // end of jQuery name space



(function($){
  $(function(){
  $('.dropdown-button').dropdown({
		inDuration: 300,
		outDuration: 225,
		constrainWidth: false,
		hover: true, // Activate on hover
		gutter: 0, // Spacing from edge
		belowOrigin: true, // Displays dropdown below the button
    stopPropogation: true
		}
	);
}); // end of document ready
})(jQuery); // end of jQuery name space

 $('.button-collapse').sideNav({
      menuWidth: 300, 
      edge: 'right', 
      closeOnClick: true,
      draggable: true, 
      onOpen: function(el) { },
      onClose: function(el) { }
 }
);
