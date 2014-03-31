/*
=============================================================
FlouCapt.js
=============================================================
author: Thomas Elain
=============================================================
date: 27/03/2014
=============================================================
version : 1.4
=============================================================
*/

// Time between the two images (in ms)
const TimeBtwTwoImg = 30000;
// Time with advertising (in ms)
const TimeWithAd = 10000;
// Time without advertising (in ms)
const TimeWithoutAd = 180000;
// Fading time for the offline message (in ms)
const FadingTimeOfflineMessage = 3000;
// Fading time for the advertising (in ms)
const FadingTimeAd = 300;
// Transition time between the beginning and the end of the fading effect of the two images (in ms)
const FadingTimeImages = 5000;

// Listeners
$(document).ready(init);
$(document).on('offline online', connected);

// Functions Inititialization
function init(evt) {
	setTimeout(refresh,TimeBtwTwoImg);
	setTimeout(hideAd, TimeWithAd);
	connected();
}

// Allows to refresh the capture image with fade effect
function refresh(evt) {
	$(".notShowed").attr("class","currentlyShowed");
	$(".showed").attr("class","notShowed");
	$(".currentlyShowed").attr("class","showed");
	$(".showed").css("background-image","url(../img/current.jpg" + "?" + Math.random()+")");
	
	setTimeout(refresh,TimeBtwTwoImg);
	
	$(".showed").css("opacity","1.0").css("display","block")
	$(".notShowed").fadeOut("FadingTimeImages",function() {
		$(".notShowed").css("z-index","-1");
		$(".showed").css("z-index","1");
	});
}

// Allows to hide the advertising
function hideAd(evt) {
	$("#ad").fadeOut("FadingTimeAd");
	setTimeout(showAd,TimeWithoutAd);
}

// Allows to show the advertising
function showAd(evt) {
	$("#ad").fadeIn("FadingTimeAd");
	setTimeout(hideAd,TimeWithAd);
}

// Allows to show a message when the connection between the client and the server is lost
function connected(evt) {
	if(navigator.onLine) {
		$("#message").fadeOut("FadingTimeOfflineMessage");
	}
	else {
		$("#message").fadeIn("FadingTimeOfflineMessage");
	}
}
