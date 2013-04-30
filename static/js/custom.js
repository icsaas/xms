// JavaScript Document
document.write("<script src='static/js/jquery-1.8.3.min.js'></script>");


var timeout         = 500;
var closetimer		= 0;
var ddmenuitem      = 0;

// open hidden layer
function mopen(id)
{
	// cancel close timer
	mcancelclosetime();

	// close old layer
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

	// get new layer and show it
	ddmenuitem = document.getElementById(id);
	ddmenuitem.style.visibility = 'visible';

}
// close showed layer
function mclose()
{
	if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
}

// go close timer
function mclosetime()
{
	closetimer = window.setTimeout(mclose, timeout);
}

// cancel close timer
function mcancelclosetime()
{
	if(closetimer)
	{
		window.clearTimeout(closetimer);
		closetimer = null;
	}
}

// close layer when click-out
document.onclick = mclose;
// -->
//more javascript from http://www.webjx.com

function setTab(m,n)
{
 var tli=document.getElementById("menu"+m).getElementsByTagName("li"); 
 var mli=document.getElementById("main"+m).getElementsByTagName("ul"); 
 for(i=0;i<tli.length;i++){ 
  tli[i].className=i==n?"hover":"";
  mli[i].style.display=i==n?"block":"none"; 
 } 
}
function altler(){
	var id=$(this).attr("id");
	$('#leftContent').css("display","none");
	$('#leftContent').css('display',"none");
	$('#graduatepage').css('display','none');
	$('#instructpage').css('display','none');
	$('#devicepage').css('display','none');
	$('#TabContent').css('display',"");
	$('#navL').css('display','');
	}
function altlerspan(){
	$('#leftContent').css("display","none");
	$('#graduatepage').css('display','none');
	$('#instructpage').css('display','none');
	$('#devicepage').css('display','none');
	$('#TabContent').css('display',"");
	$('#navL').css('display','');
	
	}
$('#menu .tag a').live('click',altlerspan);	
$('#menu li a').live('click',altler);
$('#startpage').live('click',function(){
$('#TabContent').css('display','none');
$('#graduatepage').css('display','none');
$('#devicepage').css('display','none');
$('#instructpage').css('display','none');
$('#leftContent').css("display","");
$('#navL').css('display','');
 
});
function direction()
{
    window.location.href='/cquenv';
	$('#leftContent').css('display',"none");
	$('#graduatepage').css('display','none');
	$('#instructpage').css('display','none');
	$('#devicepage').css('display','none');
	$('#TabContent').css('display',"");
	$('#navL').css('display','');
}
$('#direction').live('click',direction);

$('#graduates').live('click',function(){
	$('#leftContent').css('display',"none");
	$('#navL').css('display','none');
	$('#TabContent').css('display','none');
	$('#devicepage').css('display','none');
	$('#instructpage').css('display','none');
	$('#graduatepage').css('display',"");

	});
$('#device').live('click',function(){
	$('#leftContent').css('display','none');
	$('#graduatepage').css('display',"none");
	$('#TabContent').css('display','none');
	$('#instructpage').css('display','none');
	$('#navL').css('display','');
	$('#devicepage').css('display','');
	});
$('#notice').live('click',function(){
	$('#leftContent').css('display','none');
	$('#devicepage').css('display','none');
	$('#graduatepage').css('display',"none");
	$('#TabContent').css('display','none');
	$('#navL').css('display','');
	$('#instructpage').css('display','');});